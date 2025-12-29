# `ts` — Time series structure

The `ts` structure is the standard FFMT container for **electromagnetic time series** (time-domain recordings) and the metadata
It is designed to be created by loaders and then passed consistently to QC, filtering, decimation, segmentation, and TF estimation routines.

---

## What `ts` represents

A single `ts` instance typically corresponds to **one station recording** (or one merged run), containing:

- the recorded samples (`data`) and time vector (`t`),
- sampling information (`sr`) and number of samples (`sn`),
- channel naming and mapping (`chan`, `chanmap`, `**_ind`),
- station and acquisition metadata (`lat/lon/elev`, `device`, `serial`, `coil` IDs),
- acquisition geometry (dipole lengths `dipx/dipy` and rotations `erot/brot`),
- gap tracking and auxiliary header information (`gaps`),
- calibration responses and system metadata (`cal`).

In FFMT, `ts` is intended to be **self-contained**: it carries both data and the minimum metadata needed to process it correctly without relying on external state.

---

## How `ts` is created

`ts` is initialized using:

```matlab
ts = allocate_ts();
```

The allocator pre-defines all expected fields and sets default conventions for channel ordering, rotations, and boolean flags.

---

## Default conventions (from `allocate_ts`)

### Channel ordering and indices

FFMT assumes the canonical channel order:

- `Ex` → `ts.exind = 1`
- `Ey` → `ts.eyind = 2`
- `Bx` → `ts.bxind = 3`
- `By` → `ts.byind = 4`
- `Bz` → `ts.bzind = 5`

The channel map is initialized as:

```matlab
ts.chanmap = [ts.exind ts.eyind ts.bxind ts.byind ts.bzind];
```

### Rotations (geometry)

- `ts.erot = 0` : electric dipole rotation (N = 0°, E = 90°, W = -90°)
- `ts.brot = 0` : magnetic sensor rotation (N = 0°, E = 90°, W = -90°)

### Acquisition mode

- `ts.mode = 'single'`. Alternateively, it can be set to `merge` if more that one runs are merged/concatenated.

### Channel availability flags

By default, all channels are assumed to be present:

- `ts.exact = true`, `ts.eyact = true`, `ts.bxact = true`, `ts.byact = true`, `ts.bzact = true`
- `ts.actchan = [true true true true true]`

### Polarity reversal flags

By default, no polarity reversal is applied:

- `ts.exrev = false`, `ts.eyrev = false`
- `ts.bxrev = false`, `ts.byrev = false`, `ts.bzrev = false`

### Magnetic channel assignments (multi-station workflows)

FFMT includes bookkeeping fields to specify which station provides magnetic channels:

- `ts.bxmag = 1`, `ts.bymag = 1`  (assigned station for Bx/By)
- `ts.bxref = 1`, `ts.byref = 1`  (reference station for Bx/By)

---

## Field overview

The fields below are the canonical list defined by `allocate_ts`.  
Not every workflow uses all of them, but they are kept for consistency across instruments and modules.

### Identification and file info

- `ts.site` : site name (commonly used for folder naming)
- `ts.name` : station/site display name
- `ts.file` : file name
- `ts.path` : directory path
- `ts.ext`  : file extension (used to select a loader)

### Time and samples

- `ts.t`      : time vector (MATLAB `datenum`)
- `ts.tstart` : recording start time 
- `ts.tend`   : recording end time 
- `ts.start`  : processing start time (may differ from `tstart`)
- `ts.end`    : processing end time (may differ from `tend`)
- `ts.data`   : raw EM data (`[Ex Ey Bx By Bz]`)
- `ts.sr`     : sampling rate (Hz)
- `ts.sn`     : number of samples (`size(ts.data,1)`)
- `ts.unit`   : units for E and B channels
- `ts.gaps`   : gap marker vector
- `ts.nsec`   : number of recorded segments (common in Phoenix formats)

### Channel naming and mapping

- `ts.chan`    : channel names
- `ts.nchan`   : number of channels (`size(ts.data,2)`)
- `ts.exind`, `ts.eyind`, `ts.bxind`, `ts.byind`, `ts.bzind` : component indices
- `ts.chanmap` : channel order map (default `[1 2 3 4 5]`)

### Instrument and acquisition metadata

- `ts.serial` : instrument serial number
- `ts.device` : manufacturer / device name
- `ts.mode`   : acquisition mode (`'single'` by default)
- `ts.H`      : file header
- `ts.info`   : auxiliary info extracted from related files

### Location and geometry

- `ts.lat`, `ts.lon` : coordinates (degrees)
- `ts.elev`          : elevation (meters)
- `ts.dipx`, `ts.dipy` : dipole lengths (meters)
- `ts.coilx`, `ts.coily`, `ts.coilz` : coil IDs / serials / models
- `ts.erot`, `ts.brot` : rotation angles (degrees)

### Magnetic channel selection (multi-station)

- `ts.bxmag`, `ts.bymag` : which station provides Bx/By
- `ts.bxref`, `ts.byref` : which station is the reference Bx/By

### Channel activity and polarity

- `ts.exact`, `ts.eyact`, `ts.bxact`, `ts.byact`, `ts.bzact` : channel recorded flags
- `ts.actchan` : logical mask of active channels
- `ts.exrev`, `ts.eyrev`, `ts.bxrev`, `ts.byrev`, `ts.bzrev` : polarity reversal flags

---

## Calibration sub-structure: `ts.cal`

`ts.cal` stores calibration metadata and frequency-dependent responses.

Created fields:

- `ts.cal.sr`       : sampling rate (Hz)
- `ts.cal.unit.E`   : electric field unit
- `ts.cal.unit.B`   : magnetic field unit
- `ts.cal.freq`     : frequency vector (Hz)

Per-channel responses (amplitude and phase):

- `ts.cal.Ex.amp`, `ts.cal.Ex.phi`
- `ts.cal.Ey.amp`, `ts.cal.Ey.phi`
- `ts.cal.Bx.amp`, `ts.cal.Bx.phi`
- `ts.cal.By.amp`, `ts.cal.By.phi`
- `ts.cal.Bz.amp`, `ts.cal.Bz.phi`

Dipole lengths (for E-field scaling):

- `ts.cal.diplen.Ex`
- `ts.cal.diplen.Ey`

System metadata:

- `ts.cal.system`

---

## Minimal example

```matlab
ts = allocate_ts();

% Basic identity
ts.site   = "SITE_001";
ts.name   = "SITE_001";
ts.device = "Metronix ADU-07";
ts.serial = "A07-XXXX";

% Time series
ts.sr   = 512;
ts.data = randn(100000,5);
ts.sn   = size(ts.data,1);

% Time (datenum) example
t0 = datenum(2026,1,1,0,0,0);
ts.t = t0 + (0:ts.sn-1)'/ts.sr/86400;

% Location / geometry
ts.lat  = 19.4326;
ts.lon  = -99.1332;
ts.elev = 2240;
ts.dipx = 50;
ts.dipy = 50;
```
