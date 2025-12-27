# ReadTS

**Purpose:** Read, inspect, and quickly explore magnetotelluric (MT) time series using a MATLAB App, with fast navigation, time/frequency plots, basic filtering, and exports.

----

## What ReadTS is

ReadTS is a **viewer and lightweight QC tool** for time series. It focuses on:

- Loading multiple stations and quickly comparing channels.
- Navigating long recordings with a time slider + chunk controls.
- Switching between **time domain** and **frequency domain** views.
- Applying **basic filters** for quick inspection (LP/HP/notch).
- Exporting figures and sending data to the MATLAB Workspace.

----

## Main features

### 1) Load one (single-) or multiple time series (multi-station)

Currently supported instruments/formats:

- **Metronix Geophysics**: ADU-07 / ADU-07e / ADU-08e / ADU-10e / ADU-11e (`.ats`)
- **Phoenix Geophysics**:
  - MTU V5-2000 (`.tsh`, `.tsl`)
  - MTU5-A / V8 (`.tsn`)
  - MTU5-C / MTU8-A (folder-based, `*.td*`)
- **LEMI**:
  - 417 (folder-based, `*.B*` / `*.T*`)
  - 420 / 424 (folder-based, `*.TXT`)
  - 423 (single file, `*.B423`)
- **GEOMAGNET**:
  - GEOMAG-02 (folder-based, `*.dat`)
- **GFZ**:
  - SPAM-IV (folder-based, `*.raw`)
- **Intermagnet**:
  - JSON (`*.json`)
  - SEC (`*.sec`)
- **Zonge**:
  - ZEN / GDP (`*.z3d`)
- **FFMT synthetic**
  - Synthetic `ts (*.mat)` (FFMT time series structure)

### 2) Plot modes

- **Time domain view**: stacked plots for Ex, Ey, Bx, By, Bz.
- **Frequency domain view**: power spectra (linear/log x and y supported through menus).
- **Spectrogram view**: time–frequency power view (STFT-based).

### 3) Fast navigation

- **Time slider** to jump anywhere in the recording span.
- **Previous / Next** buttons to move chunk-by-chunk.
- **Start time text box** to jump to an exact timestamp.
- **Window length** (spinner) and **time unit** (drop-down) to define the displayed chunk size.
- Optional **Timer limit** toggle (toolbar) to prompt for start/end range when loading (supported by some loaders).

### 4) Lightweight filtering for inspection

- Quick notch filters for common powerline/industrial interference:
  - 50 Hz
  - 60 Hz
  - 16.3 Hz
- **Advanced** filter dialog (LP/HP/BP/Line, harmonics option).

### 5) Export & interoperability

- Export current plot as:
  - `*.fig`
  - `*.png`
- Send active `ts` structure to MATLAB Workspace
- “Reset” menu:
  - Reset only the time series to the original loaded backup
  - Reset the entire window/GUI

----

## Main GUI components (quick map)

Below, “(icon)” placeholders refer to your `_static/icons/*.svg` set.

- <img src="../_static/icons/spinner.svg" class="icon" alt="Window length"> **Window length (spinner)**: Sets the duration of the displayed chunk (numeric value).

- <img src="../_static/icons/drop_down.svg" class="icon" alt="Window units"> **Unit (drop-down)**: Sets the unit for the window length: `sec / min / hr / day`.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Start time"> **Start time (edit field)**: Jump to a specific timestamp (UTC) by typing a date string.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="End time"> **End time (read-only)**: Displays the computed end time for the current window.

- <img src="../_static/icons/button.svg" class="icon" alt="Previous"> **Previous (button)**: Moves to the previous chunk.

- <img src="../_static/icons/button.svg" class="icon" alt="Next"> **Next (button)**: Moves to the next chunk.

- <img src="../_static/icons/numeric_slider.svg" class="icon" alt="Navigation"> **Time navigation (slider)**: Jump anywhere across the global span of loaded time series.

### Toolbar tools (top)

- <img src="../_static/icons/readts/timer-off.png" class="icon" alt="Timer" style="height:1.1em; width:auto; vertical-align:middle;"> **Timer** (toggle): Enable/disable “time limit mode” for loaders that support it.
- 
- <img src="../_static/icons/readts/information.png" class="icon" alt="Info" style="height:1.1em; width:auto; vertical-align:middle;"> **Info** (push): Open the station metadata window.
- 
- <img src="../_static/icons/readts/map.png" class="icon" alt="Map" style="height:1.1em; width:auto; vertical-align:middle;"> **Map** (push): Plot station locations on a geobubble map.
- 
- <img src="../_static/icons/readts/detrend.png" class="icon" alt="Detrend" style="height:1.1em; width:auto; vertical-align:middle;"> **Detrend** (toggle): Detrend the displayed segment (time domain).
- 
- <img src="../_static/icons/readts/time.png" class="icon" alt="Time Domain" style="height:1.1em; width:auto; vertical-align:middle;"> **Time domain** (toggle): Time-domain plotting.
- 
- <img src="../_static/icons/readts/frequency.png" class="icon" alt="Frequency Domain" style="height:1.1em; width:auto; vertical-align:middle;"> **Frequency domain** (toggle): Spectra plotting.

### Plot panel context menu

Right-click on the plot panel to access quick scaling helpers:

- **E-channels → Same as Ex / Same as Ey**
- **B-channels → Same as Bx / Same as By / Same as Bz**

----

## Load data (details)

ReadTS uses two loading patterns, depending on how the instrument stores its data.

### Pattern A — Select a folder (directory-based recording)

Use this when the data are stored as **multiple files per run**, often with metadata and channel files inside a folder.

**GUI path:** `File → Load → ...` then choose the directory in the dialog.

- Metronix ADU family (`*.ats` stored as a folder collection)
- Phoenix MTU5-C / MTU8-A (folder with `*.td*`)
- LEMI 417 / 420 / 424 (folder with `*.B*`, `*.T*`, or `*.TXT`)
- Zonge ZEN (`*.z3d`)
- GFZ SPAM-IV (`*.raw`)
- GEOMAG-02 (`*.dat`)
- Intermagnet SEC (`*.sec`)
- FFMT synthetic `ts (*.mat)` (depending on your local layout)

```{note}
Some loaders can optionally use “timer mode”:
if the **Timer** toggle is ON, ReadTS may ask for start/end times and load only that interval (when supported by the loader).
```

### Pattern B — Select a file (single-file entry point)

Use this when a single file is enough to locate and load everything.

**GUI path:** `File → Load → ...` then choose the file in the dialog.

- Phoenix MTU V5-2000 (`.tsh` / `.tsl`)
- Phoenix MTU5-A / V8 (`.tsn`)
- LEMI 423 (`.B423`)
- Intermagnet JSON (`.json`)

```{tip}
If the dialog seems “wrong” (folder vs file), it usually means the instrument expects the other loading pattern.
```

### What happens after load

When loading succeeds, ReadTS will:

1. Merge the new station into `app.ts` (active data).
2. Also store a backup in `app.tmp` (original data).
3. Populate the stations list in **Plot → Stations**.
4. Compute global time span from station `tstart`/`tend`.
5. Update the slider tick labels and plot the initial chunk.

```{warning}
If a station fails to merge, it usually indicates a structural mismatch in the returned `station` struct (fields missing or inconsistent).
The error dialog displays the MATLAB report to help debugging.
```

----

## Navigate & inspect

### Window length and units

- The spinner sets a numeric value.
- The drop-down sets the unit (`sec/min/hr/day`).
- Internally, ReadTS converts this into seconds and uses it to compute the chunk end time.

### Slider behavior

- The slider is normalized to the global time range:
  - left = earliest `tstart`
  - right = latest `tend`
- Moving the slider updates:
  - `Start Date and Time (UTC)`
  - `End Date and Time (UTC)`
  - the plot (time or frequency)

### Previous / Next behavior

- Previous: subtract one window length from the current `Start time`.
- Next: add one window length.
- ReadTS automatically clamps to the global bounds (no out-of-range indexing).

----

## Plot modes (details)

### Time domain

- Plots 5 channels in a tiled layout:
  - Ex
  - Ey
  - Bx
  - By
  - Bz
- Multiple stations overlay per channel.
- Optional detrending (toolbar **Detrend** toggle).

### Frequency domain (power spectra)

- Computes FFT of the displayed chunk for each station.
- Supports:
  - frequency [Hz] or period [s]
  - logarithmic or linear x-axis
- Overlays stations per channel.

```{note}
Frequency-domain plot uses the displayed chunk length. Shorter windows increase variance and reduce frequency resolution.
```

### Spectrogram view

- Computes STFT-based spectrogram on the active chunk.
- Uses adaptive window settings to keep the display stable across different chunk durations.

```{tip}
Spectrograms are excellent for identifying transient interference that does not show up clearly in a single averaged spectrum.
```

----

## Filtering (details)

### Quick notch filters

Menu: **Filter → Power Line**

- Applies a bandstop around the selected line frequency.
- Includes an option to remove harmonics (used in the “Line” filter mode).

### Advanced filtering

Menu: **Filter → Advanced**

- LP: low-pass
- HP: high-pass
- BP: band-pass
- Line: notch / band-stop (optionally apply harmonics)

```{warning}
Because filtering uses `filtfilt`, short chunks or strong discontinuities can create edge artifacts.
If you see weird boundary behavior, increase the window length or check the raw signal.
```

----

## Export (details)

### Export as *.fig

Menu: **Export → Figure → *.fig**

- Copies the current plot panel content into a docked MATLAB figure.
- Useful for later editing in MATLAB (labels, line style, etc.).

### Export as *.png

Menu: **Export → Figure → *.png**

- Opens a docked figure for resizing.
- Exports with high resolution (configured in code).
- Adds a subtle rectangle border for clean background consistency.

### Send to workspace

Menu: **Export → ts to Workspace**

- Exposes your active `ts` structure as a variable named `ts` in the MATLAB base workspace.
- Useful for quick scripting after inspection.

----

## Reset behavior

Menu: **File → Reset**

- **Time Series**: restore `app.ts` from the backup (`app.tmp`).
- **Window**: clear everything (time series arrays, plots, slider ticks, UI text fields).

```{note}
Reset is designed for fast “try again” cycles when you test filters and want to revert instantly to the original signals.
```

----

## Quick start (step-by-step tutorials)

### Tutorial 1 — Load data

1. Open **File → Load**.
2. Choose the right manufacturer/instrument menu.
3. Select **either a folder or a file** depending on the instrument (details below).
4. After successful load:
   - the station list appears in **Plot → Stations**
   - the time slider is populated
   - the first chunk is plotted automatically

```{tip}
If you load multiple stations, ReadTS will stack them together per channel and automatically assign colors.
Use **Plot → Stations** to toggle stations on/off without reloading.
```

### Tutorial 2 — Navigate in time (slider + chunk controls)

1. Set your window length:
   - adjust **Window length** spinner
   - choose units in **Unit** drop-down (`sec/min/hr/day`)
2. Jump to a specific time:
   - drag the **time slider**, or
   - type a timestamp in **Start Date and Time (UTC)**
3. Step chunk-by-chunk using:
   - **Previous**
   - **Next**

```{note}
When you change the window length, ReadTS automatically prevents going out of bounds.
If the requested window exceeds the end of the dataset, it shifts the window so the end matches the last available time.
```

### Tutorial 3 — Switch views: Time vs Frequency

Use the toolbar toggles:

- Click **Time domain** to show time series (Ex/Ey/Bx/By/Bz).
- Click **Frequency domain** to show power spectra.

Then choose the x-axis convention:

- **Plot → Spectra → Frequency [Hz]** or **Period [s]**
- **Plot → Spectra → Logarithmic** or **Linear**

```{tip}
For MT inspection, frequency view is often more intuitive for identifying powerline peaks, while period view is useful when thinking in “MT periods”.
```

### Tutorial 4 — Apply a quick notch filter (powerline)

1. Go to **Filter → Power Line**.
2. Select:
   - **50 Hz** (Europe)
   - **60 Hz** (Americas)
   - **16.3 Hz** (railway environments)
3. The plot refreshes automatically.

```{warning}
Filters in ReadTS are intended for **inspection**, not as a full processing step.
If you need reproducible, documented filtering as part of processing, do it in FFMT/nEMesis pipelines.
```

### Tutorial 5 — Advanced filtering (LP / HP / BP / Notch / Harmonics)

1. Go to **Filter → Advanced**.
2. Choose:
   - Filter type: LP / HP / BP / Line (notch)
   - Order and cutoff(s)
   - Optional harmonic removal for notches
3. Apply, then re-check plots in time and frequency domains.

```{note}
Internally, ReadTS uses `butter()` + `filtfilt()` for these filters.
This is great for quick visualization, but it can distort boundaries (edge effects) for short windows.
```

### Tutorial 6 — Export and share

- Export figures:
  - **Export → Figure → *.fig**
  - **Export → Figure → *.png**
- Send time series to Workspace:
  - **Export → ts to Workspace**

```{note}
The PNG export creates a temporary docked figure you can resize before saving, then writes with high resolution.
```

### Tutorial 7 — Station metadata and map

- Click **Info** (toolbar) to open station information (sampling rate, instrument fields, etc.).
- Click **Map** (toolbar) to see station positions (geobubble on satellite basemap).

## Troubleshooting

### “Nothing plots” or “empty signals”

- Ensure your selected station is checked in **Plot → Stations**.
- Confirm the selected time window overlaps the station recording span.
- Increase the window length (very short windows may become empty after clamping).

### Load errors

- Verify permissions for the selected folder/file.
- Confirm the instrument format matches the menu choice.
- If the error mentions merge/fields, validate that the loader returns consistent fields across stations.

### Map shows no points

- Verify `lat` and `lon` exist and are valid numbers for all loaded stations.
- Some instruments may not contain GPS metadata; you may need to enrich your `ts` structure externally.
