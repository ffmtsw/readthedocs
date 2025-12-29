# `mt` — Transfer function structure

The `mt` structure is the standard FFMT container for **site-specific magnetotelluric transfer functions**
and derived MT response quantities in the frequency domain. It is designed to store results from:

- **data-derived transfer functions** (estimated from time series processing or imported from EDI), and
- **model-derived responses** (e.g., imported from forward/inversion software).

In practice, `mt` is the main structure used for MT visualization, QC/editing, export/import, and comparison
between observed and modeled responses.

---

## How `mt` is created

`mt` is initialized using:

```matlab
mt = allocate_mt();
```

Optionally, an "advanced" mode adds extra fields related to 1-D forward/inverse modeling:

```matlab
mt = allocate_mt('advanced');
```

The allocator pre-defines a standardized set of fields so that plotting and downstream tools can assume a
consistent layout.

---

## What `mt` represents

A single `mt` instance typically corresponds to **one site** and contains:

- site metadata and coordinates (`site`, `lonlat`, `UTM`, `XY`, `z`),
- frequency / period vectors (`freq`, `per`, `nfreq`),
- impedance tensor components and errors (`Z**`, `Z**_Err`),
- apparent resistivity and phase (from impedance) (`rho**`, `phi**`, and errors `*_Err`),
- tipper components and errors (`txz`, `tyz`, `*_Err`),
- Phase Tensor (Φ) components and ellipse parameters (`phi11..phi22`, `phimax/phimin`, `alpha/beta`, and errors),
- Real/Imaginary Resistivity Tensors and derived ellipse parameters (`rt**`, `irt**`, `rpt**`, etc.),
- a metadata container `mt.info` storing units, rotations, static shift, and processing provenance.

---

## Metadata container: `mt.info`

`mt.info` is initialized as a nested structure intended to carry provenance and conventions.

### Assignment date
- `mt.info.date` : assignment date (string, default set to “today”)

### Electric field conventions
- `mt.info.E.unit` : electric-field unit (e.g., `"mV/km"`)
- `mt.info.E.rot`  : rotation angle / convention (deg)

### Magnetic field conventions (B)
- `mt.info.B.stat` : logical flag; using magnetic flux density (B)?
- `mt.info.B.unit` : B-field unit (e.g., `"nT"`, `"T"`)
- `mt.info.B.rot`  : rotation angle / convention (deg)

### Magnetic field conventions (H)
- `mt.info.H.stat` : logical flag; using magnetic field intensity (H)?
- `mt.info.H.unit` : H-field unit (e.g., `"A/m"`)
- `mt.info.H.rot`  : rotation angle / convention (deg)

### Impedance conventions
- `mt.info.Z.unit` : impedance unit (default set by allocator to `"mV/km/nT"`)
- `mt.info.Z.rot`  : rotation convention (e.g., +CW or -CCW; left empty by default)

### Static shift bookkeeping
- `mt.info.staticshift.xx`, `xy`, `yx`, `yy` : static-shift factors for impedance components
- `mt.info.staticshift.xz`, `yz`             : factors for tipper components (complex)

### Data origin and processing provenance
- `mt.info.source` : origin tag, e.g., `"edi"`, `"processing"`, `"ModEM"`, etc.

- `mt.info.processing.software` : software/tool name (e.g., `"FFMT"`)
- `mt.info.processing.version`  : processing pipeline version tag
- `mt.info.processing.mode`     : `"single-site"`, `"multi-site"`, etc.
- `mt.info.processing.job`      : job configuration snapshot (struct)
- `mt.info.processing.rem_ref`  : remote reference used? (logical)
- `mt.info.processing.rem_site` : remote site identifier (string)
- `mt.info.processing.distance` : distance between stations (km), numeric or vector

---

## Field overview

The fields below are the canonical list defined by `allocate_mt`.

### Site and coordinates

- `mt.site`   : site name or identifier
- `mt.lonlat` : `[lon lat]` in decimal degrees
- `mt.UTM`    : `[X Y]` in meters
- `mt.XY`     : local `[X Y]` in kilometers (relative to dataset center)
- `mt.z`      : elevation (m), positive above sea level

### Frequency axis

- `mt.nfreq` : number of frequencies
- `mt.freq`  : frequency vector (Hz)
- `mt.per`   : period vector (s)

### Impedance tensor (Z) and errors

- `mt.Zxx`, `mt.Zxy`, `mt.Zyx`, `mt.Zyy` : impedance components (complex)
- `mt.Zxx_Err`, `mt.Zxy_Err`, `mt.Zyx_Err`, `mt.Zyy_Err` : associated errors

### Apparent resistivity (ρa) and errors

- `mt.rhoxx`, `mt.rhoxy`, `mt.rhoyx`, `mt.rhoyy` : apparent resistivity components (Ω·m)
- `mt.rhoxx_Err`, `mt.rhoxy_Err`, `mt.rhoyx_Err`, `mt.rhoyy_Err` : associated errors

### Impedance phase (φ) and errors

- `mt.phixx`, `mt.phixy`, `mt.phiyx`, `mt.phiyy` : phase components (deg)
- `mt.phixx_Err`, `mt.phixy_Err`, `mt.phiyx_Err`, `mt.phiyy_Err` : associated errors

### Tipper (T) and errors

- `mt.txz`, `mt.tyz` : tipper components (complex)
- `mt.txz_Err`, `mt.tyz_Err` : associated errors

### Phase Tensor (Φ) components and ellipse parameters

**Components**
- `mt.phi11`, `mt.phi12`, `mt.phi21`, `mt.phi22` : Φ tensor components
- `mt.phi11_Err`, `mt.phi12_Err`, `mt.phi21_Err`, `mt.phi22_Err` : associated errors

**Ellipse parameters**
- `mt.phimax`, `mt.phimin` : maximum/minimum phase tensor axes
- `mt.alpha`, `mt.beta`    : phase tensor strike/skew-style angles (convention-dependent)

- `mt.phimax_Err`, `mt.phimin_Err`, `mt.alpha_Err`, `mt.beta_Err` : associated errors

### Real resistivity tensor (RT) and ellipse parameters

**Components**
- `mt.rt11`, `mt.rt12`, `mt.rt21`, `mt.rt22` : real resistivity tensor components
- `mt.rt11_Err`, `mt.rt12_Err`, `mt.rt21_Err`, `mt.rt22_Err` : associated errors

**Ellipse parameters**
- `mt.resreal_max`, `mt.resreal_min`, `mt.resreal_alpha`, `mt.resreal_beta`
- `mt.resreal_max_Err`, `mt.resreal_min_Err`, `mt.resreal_alpha_Err`, `mt.resreal_beta_Err`

### Imaginary resistivity tensor (IRT) and ellipse parameters

**Components**
- `mt.irt11`, `mt.irt12`, `mt.irt21`, `mt.irt22` : imaginary resistivity tensor components
- `mt.irt11_Err`, `mt.irt12_Err`, `mt.irt21_Err`, `mt.irt22_Err` : associated errors

**Ellipse parameters**
- `mt.resimag_max`, `mt.resimag_min`, `mt.resimag_alpha`, `mt.resimag_beta`
- `mt.resimag_max_Err`, `mt.resimag_min_Err`, `mt.resimag_alpha_Err`, `mt.resimag_beta_Err`

### Resistivity phase tensor (RPT) and ellipse parameters

**Components**
- `mt.rpt11`, `mt.rpt12`, `mt.rpt21`, `mt.rpt22` : resistivity phase tensor components
- `mt.rpt11_Err`, `mt.rpt12_Err`, `mt.rpt21_Err`, `mt.rpt22_Err` : associated errors

**Ellipse parameters**
- `mt.resphase_max`, `mt.resphase_min`, `mt.resphase_alpha`, `mt.resphase_beta`
- `mt.resphase_max_Err`, `mt.resphase_min_Err`, `mt.resphase_alpha_Err`, `mt.resphase_beta_Err`

---

## Advanced mode fields

If `allocate_mt('advanced')` is used, the allocator adds:

### `mt.time`
- `mt.time` : initialized to `NaT` (MATLAB datetime “Not-a-Time”)

### `mt.inv1D`
A small container for 1-D inversion results:

- `mt.inv1D.d`   : depth vector (units defined by the inversion module)
- `mt.inv1D.rho` : resistivity model (Ω·m)

> Note: `allocate_mt('advanced')` also declares an additional field name `fwd1D`,
> but it is not explicitly initialized in the provided snippet.

---

## Minimal example

```matlab
mt = allocate_mt();

% Site
mt.site   = "SITE_001";
mt.lonlat = [-99.1332 19.4326];
mt.z      = 2240;

% Frequencies
mt.freq  = logspace(-3,3,40).';
mt.per   = 1./mt.freq;
mt.nfreq = numel(mt.freq);

% Impedance (example placeholders)
mt.Zxy = (1+1i) * ones(mt.nfreq,1);
mt.Zyx = (1-1i) * ones(mt.nfreq,1);
mt.Zxy_Err = 0.05 * abs(mt.Zxy);
mt.Zyx_Err = 0.05 * abs(mt.Zyx);

% Provenance
mt.info.source = "processing";
mt.info.processing.software = "FFMT";
```

---

## See also

- [`ts`](ts) — time series structure
- [`processing`](processing) — job/task processing containers
- [`model`](model) — resistivity model structure
- [`study`](study) — modeling study structure
