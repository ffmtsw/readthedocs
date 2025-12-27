# ReadTS

**Purpose**: Read and explore magnetotelluric (MT) time series through a MATLAB App, with fast navigation, plotting, and basic exports.

----

## Main features

- **Load one or multiple time series** from the following instruments:
  - Metronix Geophysics    **ADU-07 / ADU-07e / ADU-08e / ADU-10e / ADU-11e** (`*.ats`)  
    *(folder selection)*
  - Phoenix Geophysics     **MTU V5-2000** (`*.tsh`, `*.tsl`)  
    *(file selection)*
  - Phoenix Geophysics     **MTU5-A / V8** (`*.tsn`)  
    *(file selection)*
  - Phoenix Geophysics     **MTU5-C / MTU8-A** (`*.td*`)  
    *(folder selection; optional time range if Timer is enabled)*
  - LEMI                   **417** (`*.B*`, `*.T*`)  
    *(folder selection)*
  - LEMI                   **420 / 424** (`*.TXT`)  
    *(folder selection)*
  - LEMI                   **423** (`*.B423`)  
    *(file selection)*
  - GEOMAGNET              **GEOMAG-02** (`*.dat`)  
    *(folder selection)*
  - GFZ                    **SPAM-IV** (`*.raw`)  
    *(folder selection)*
  - Intermagnet            **JSON** (`*.json`)  
    *(file selection)*
  - Intermagnet            **SEC** (`*.sec`)  
    *(file selection)*
  - Zonge International    **ZEN High-Res Receiver** (`*.z3d`)  
    *(folder selection)*
- **Time-domain view**: 5 stacked channels (**Ex, Ey, Bx, By, Bz**) with fast navigation.
- **Frequency-domain view**: power spectra with:
  - **Frequency [Hz]** or **Period [s]**
  - **Logarithmic** or **Linear** scaling
- **Spectrogram view** (STFT-based) for the active window.
- **Filtering**:
  - Power-line notch presets (**50/60/16.3 Hz**, with harmonics)
  - Advanced filters (LP / HP / BP / Notch)
- **Calibrate segment**: plot a window in field units (dipoles + coil calibration).
- **Station selection**: toggle visibility of individual loaded series.
- **Station map**: quick location overview (satellite basemap).
- **Metadata panel**: inspect station/instrument properties.
- **Export**: copy current plot into MATLAB figure (`*.fig`) or save as PNG (`*.png`).
- **Workspace export**: send active time series structure to the base workspace.
- **Reset**:
  - Reset active time series to the original backup.
  - Clear the window completely.

----

## Quick start (summary)

1. **Load data:** `File → Load` and select either a **folder** or a **file** (depends on instrument).
2. **Navigate:** use the **slider**, **Previous**, **Next**, or type a **Start time (UTC)**.
3. **View mode:** toggle **Time domain** or **Frequency domain**; optionally plot **Spectrograms**.
4. **Filter (optional):** apply **LP / HP / Notch**, then re-plot.
5. **Export:** save figures as **.fig / .png**, or **send** the series to **Workspace**.

----

## Load data

Depending on the instrument/manufacturer, ReadTS requires selecting either the **recording folder** or a **file**.

### Select folder (path)

Use folder selection when the acquisition produces multiple files per recording or when the reader expects a directory.

- Metronix Geophysics  **ADU-07 / 07e / 08e / 10e / 11e** (`*.ats`)  
  `File → Load → Metronix → ADU 07e/08e/10e/11e (*.ats)`

- Phoenix Geophysics   **MTU5-C / MTU8-A** (`*.td*`)  
  `File → Load → Phoenix Geophysics → MTU5-C / MTU8-A (*.td)`  
  If the **Timer** tool is enabled, ReadTS will ask for **Start time (UTC)** and **End time (UTC)** before loading.

- LEMI                 **417** (`*.B*`, `*.T*`)  
  `File → Load → LEMI → 417 Binary (*.B*)`

- LEMI                 **420 / 424** (`*.TXT`)  
  `File → Load → LEMI → 420 Text File (*.TXT)`  
  `File → Load → LEMI → 424 Text File (*.TXT)`

- GEOMAGNET            **GEOMAG-02** (`*.dat`)  
  `File → Load → GEOMAGNET → GEOMAG-02 (*.dat)`

- GFZ                  **SPAM-IV** (`*.raw`)  
  `File → Load → GFZ → SPAM-IV (*.raw)`

- Zonge International  **ZEN** (`*.z3d`)  
  `File → Load → Zonge → Zonge GDP (*.z3d)`

### Select file

Use file selection when the reader expects a single file input.

- Phoenix Geophysics   **MTU V5-2000** (`*.tsh`, `*.tsl`)  
  `File → Load → Phoenix Geophysics → MTU V5-2000 (*.tsh/*.tsl)`

- Phoenix Geophysics   **MTU5-A / V8** (`*.tsn`)  
  `File → Load → Phoenix Geophysics → MTU5-A / V8 (*.tsn)`

- LEMI                 **423** (`*.B423`)  
  `File → Load → LEMI → 423 Binary (*.B423*)`

- Intermagnet          **JSON** (`*.json`)  
  `File → Load → Intermagnet → JSON (*.json)`

- Intermagnet          **SEC** (`*.sec`)  
  `File → Load → Intermagnet → SEC (*.sec)`

```{note}
After a successful load, ReadTS:
(1) merges the station into the active list, (2) repopulates the Stations menu,
(3) initializes time controls (start/end fields + slider), and (4) refreshes the plot.
