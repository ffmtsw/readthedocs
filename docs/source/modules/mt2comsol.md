# MT2COMSOL

MT2COMSOL is a **GUI-based front end** to prepare model-domain inputs for COMSOL, manage the COMSOL + LiveLink session from MATLAB, and launch the MT response-extraction workflow.

It focuses on:

- Estimating **skin depth** from the selected MT frequency range and a reference resistivity.
- Defining the model domain in **local Cartesian coordinates** and converting it to **geographic DEM limits**.
- Downloading and plotting **DEM / topobathymetry** data.
- Generating COMSOL-ready ASCII input files for topography, thin-layer conductance, site coordinates, and coastline support.
- Starting a COMSOL server session through **LiveLink for MATLAB**.
- Opening the next processing steps through the **Anisotropy Calculator** and **MT response-extraction** tools.

----


## Main features

### 1) Frequency and skin-depth estimation

- Define the **maximum MT frequency**.
- Define the **minimum MT frequency**.
- Define a **reference resistivity**.
- Automatically compute the corresponding:
  - **minimum skin depth** (highest frequency)
  - **maximum skin depth** (lowest frequency)

### 2) Reference coordinates and model-domain definition

- Enter the model center manually as:
  - **Central Latitude [deg]**
  - **Central Longitude [deg]**
- Or load the center automatically from an **MT structure** stored in a `*.mat` file.
- Define the local domain extents in kilometers:
  - **Easting min / max**
  - **Northing min / max**
- Convert those limits into:
  - **Latitude min / max**
  - **Longitude min / max**
  - **model area [km2]**

### 3) DEM download and visualization

- Download DEM data manually from the **GMRT Map Tool**.
- Download DEM data automatically from the GUI using the computed geographic limits.
- Choose:
  - **output format**
  - **download resolution**
  - whether to **plot the DEM after download**
- Open the selected working folder directly from the GUI.
- Plot an existing DEM / GeoTIFF file for quick inspection.

### 4) COMSOL input-file generation

- Launch the input-file generator for the current project folder.
- Prepare files used later by the COMSOL workflow, including:
  - `Topography.txt`
  - `ThinLayer.txt`
  - `Coordinates.txt`
  - `Coastline.txt` (if coastline support is selected)

### 5) COMSOL connection and MT response extraction

- Check whether **COMSOL** and **LiveLink for MATLAB** are available.
- Start or stop the GUI-side COMSOL session.
- Enable **MPH file selection** only when a valid session is active.
- Launch the MT response-extraction workflow from a selected COMSOL model.

### 6) Accessory tools

- Open the **Anisotropy Calculator** from the **Tools** menu.
- Open the module **Documentation** from the **Extras** menu.

----


## Main GUI components

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_gui.png"
       alt="Main GUI Components"
       width="100%">
</p>

### DEM and Model Domain Setup

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Max frequency"> **Max. Frequency [Hz]** (numeric edit field): Sets the highest MT frequency used to estimate the shallowest skin depth.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Min frequency"> **Min. Frequency [Hz]** (numeric edit field): Sets the lowest MT frequency used to estimate the deepest skin depth.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Resistivity"> **Resistivity [Ohmm]** (numeric edit field): Defines the reference resistivity used for the skin-depth estimate.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Skin depth min"> **Skin depth min [km]** (read-only numeric field): Displays the estimated minimum skin depth.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Skin depth max"> **Skin depth max [km]** (read-only numeric field): Displays the estimated maximum skin depth.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Central latitude"> **Central Latitude [deg]** (numeric edit field): Sets the reference latitude of the model domain.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Central longitude"> **Central Longitude [deg]** (numeric edit field): Sets the reference longitude of the model domain.

- <img src="../_static/icons/button.svg" class="icon" alt="Use center from MT structure"> **Use Center from MT Structure** (button): Loads a `*.mat` file, reads the variable `mt`, and uses its center as the domain reference.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Easting min"> **Easting min. [km]** (numeric edit field): Minimum x-extent relative to the reference center.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Easting max"> **Easting max. [km]** (numeric edit field): Maximum x-extent relative to the reference center.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Northing min"> **Northing min. [km]** (numeric edit field): Minimum y-extent relative to the reference center.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Northing max"> **Northing max. [km]** (numeric edit field): Maximum y-extent relative to the reference center.

- <img src="../_static/icons/button.svg" class="icon" alt="Calculate limits"> **Calculate Limits** (button): Converts the local extents into geographic limits and computes the total area.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Latitude min"> **Latitude min. [deg]** (read-only numeric field): Southern geographic limit of the DEM window.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Latitude max"> **Latitude max. [deg]** (read-only numeric field): Northern geographic limit of the DEM window.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Longitude min"> **Longitude min. [deg]** (read-only numeric field): Western geographic limit of the DEM window.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Longitude max"> **Longitude max. [deg]** (read-only numeric field): Eastern geographic limit of the DEM window.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Area"> **Area [km2]** (read-only numeric field): Displays the area of the selected domain.

- <img src="../_static/icons/drop_down.svg" class="icon" alt="Format"> **Format** (drop-down): Selects the DEM output format requested from the automatic download workflow.

- <img src="../_static/icons/drop_down.svg" class="icon" alt="Resolution"> **Resolution** (drop-down): Selects the DEM sampling density.

- <img src="../_static/icons/check_box.svg" class="icon" alt="Plot DEM"> **Plot DEM** (check box): If enabled, plots the DEM immediately after download.

- <img src="../_static/icons/button.svg" class="icon" alt="Select folder"> **Select Folder** (button): Chooses the working folder where DEM and COMSOL input files will be stored.

- <img src="../_static/icons/edit_field.svg" class="icon" alt="Folder"> **Folder** (read-only text field): Displays the selected project folder.

- <img src="../_static/icons/button.svg" class="icon" alt="Download DEM"> **Download DEM** (button): Downloads the DEM for the current geographic limits using the selected settings.

- <img src="../_static/icons/button.svg" class="icon" alt="Open folder"> **Open Folder** (button): Opens the selected working directory in the system file explorer.

### Modeling Workflow

- <img src="../_static/icons/panel.svg" class="icon" alt="Installation status"> **Installation** (status panel): Reports whether COMSOL and LiveLink for MATLAB are available.

- <img src="../_static/icons/button.svg" class="icon" alt="Manual DEM download"> **Download DEM** (button, DEM panel): Opens the GMRT website for manual DEM download.

- <img src="../_static/icons/button.svg" class="icon" alt="Plot DEM"> **Plot DEM** (button, DEM panel): Opens the DEM plotting utility.

- <img src="../_static/icons/button.svg" class="icon" alt="Create input files"> **Create Input Files** (button): Launches the COMSOL input-file generator for the selected project folder.

- <img src="../_static/icons/switch.svg" class="icon" alt="Start COMSOL session"> **Start COMSOL Session** (switch): Starts or resets the GUI-side COMSOL session.

- <img src="../_static/icons/lamp.svg" class="icon" alt="Inactive status"> **Status lamps** (red/green): Indicate whether a COMSOL connection is inactive or active.

- <img src="../_static/icons/button.svg" class="icon" alt="Select MPH file"> **Select MPH File** (button): Opens the MT response-extraction workflow. This button is enabled only when a valid COMSOL session is active.

### Menu entries

- <img src="../_static/icons/menu_bar.svg" class="icon" alt="Anisotropy calculator"> **Tools → Anisotropy Calculator**: Opens the anisotropy-tensor calculator.

- <img src="../_static/icons/menu_bar.svg" class="icon" alt="Documentation"> **Extras → Documentation**: Opens the online documentation page for MT2COMSOL.

----


## DEM and model-domain setup

### Frequency range and skin-depth estimate

The **Frequency and Skin Depth** panel is the natural starting point of the GUI. You provide:

- the highest frequency,
- the lowest frequency,
- and a reference resistivity,

and the GUI updates the expected shallow and deep skin-depth estimates automatically.

This is useful as a quick planning tool before defining the final domain size. It provides a first-order sense of the spatial scale that may be relevant to the model.

```{note}
The shallowest skin depth is linked to the **highest frequency**, while the deepest skin depth is linked to the **lowest frequency**.
```

### Reference coordinates

The **Reference Coordinates** panel defines the center of the working domain. You can either:

- type the latitude and longitude manually, or
- press **Use Center from MT Structure** to load the center automatically from a saved `mt` structure.

This center is later used to:

- define local x/y coordinates in kilometers,
- convert between local and geographic coordinates,
- and compute DEM download limits.

### Domain extents in kilometers

The **Domain Extents** panel defines the model size relative to the reference center. The four fields represent the minimum and maximum local limits:

- `xmin`, `xmax`
- `ymin`, `ymax`

all in **kilometers**.

These limits define the area that will later be converted into geographic coordinates for DEM download and topography preparation.

### Geographic limits and area

After defining the center and local extents, press **Calculate Limits**. The GUI converts the local domain into:

- latitude min / max,
- longitude min / max,
- and total area in square kilometers.

These fields are read-only because they are derived values.

```{tip}
A practical workflow is: first define the local domain in kilometers, then use **Calculate Limits**, and only then proceed to download the DEM.
```

### DEM download settings

The **DEM Download Settings** panel controls the automatic DEM request. You can define:

- the file format,
- the resolution,
- whether the DEM should be plotted after download,
- and the destination folder.

The folder selected here is reused later by the input-file generator.

```{warning}
In the current GUI workflow, automatic DEM download is effectively implemented for **GeoTIFF** output. If another format is selected, the GUI reports that it is not yet supported.
```

----


## DEM utilities

### Download DEM (manual GMRT access)

The **Download DEM** button in the **DEM** panel opens the **GMRT Map Tool** in your web browser. This is useful when you want to download the terrain manually instead of using the automatic workflow.

```{note}
The GUI displays an information message recommending **GeoTIFF** files for the downstream MT2COMSOL workflow.
```

### Plot DEM

The **Plot DEM** button opens the DEM plotting utility. This is intended for quick visual inspection of an existing DEM or GeoTIFF file before running the model-building workflow.

----


## Quick start (step-by-step tutorials)

### Tutorial 1 — Define the frequency range and inspect skin depth

1. Open the **Frequency and Skin Depth** panel.
2. Enter:
   - **Max. Frequency [Hz]**
   - **Min. Frequency [Hz]**
   - **Resistivity [Ohmm]**
3. Inspect the automatically updated:
   - **Skin depth min [km]**
   - **Skin depth max [km]**

```{tip}
Use this first estimate as a planning guide for choosing reasonable domain extents before downloading the DEM.
```

### Tutorial 2 — Define the reference center and local model extents

1. In **Reference Coordinates**, either:
   - type **Central Latitude / Longitude**, or
   - click **Use Center from MT Structure** and select a `*.mat` file containing `mt`
2. In **Domain Extents**, define:
   - **Easting min / max [km]**
   - **Northing min / max [km]**
3. Click **Calculate Limits**.
4. Inspect the resulting:
   - geographic limits,
   - and **Area [km2]**.

```{note}
The geographic limits are computed from the local x/y box and the selected reference center. They are not meant to be edited directly from this panel.
```

### Tutorial 3 — Download a DEM automatically from the GUI

1. Define the domain as described above.
2. In **DEM Download Settings**, choose:
   - **Format**
   - **Resolution**
   - whether **Plot DEM** should be enabled
3. Click **Select Folder** and choose the project directory.
4. Click **Download DEM**.
5. If successful, the DEM is saved in the selected folder.

```{warning}
The automatic download workflow requires valid latitude/longitude limits and a valid destination folder. If either is missing, the GUI will stop and show a warning dialog.
```

### Tutorial 4 — Open the GMRT website and download manually

1. In the **DEM** panel, click **Download DEM**.
2. Your browser opens the **GMRT Map Tool**.
3. Download the terrain product manually.
4. Prefer **GeoTIFF** output for the standard MT2COMSOL workflow.

### Tutorial 5 — Create COMSOL input files

1. Make sure a valid **project folder** is selected.
2. Click **Create Input Files**.
3. Follow the dialogs of the input-file workflow.
4. The project folder will be populated with COMSOL-ready ASCII files.

```{tip}
This is the main preparation step before building the COMSOL model itself.
```

### Tutorial 6 — Start a COMSOL session

1. Go to the **COMSOL Connection** panel.
2. Move **Start COMSOL Session** to **On**.
3. Wait for the server launch and MATLAB connection.
4. Confirm that:
   - the green lamp is active,
   - and **Select MPH File** is enabled.

```{note}
If MATLAB is already connected to a COMSOL server, the GUI keeps the session active instead of failing.
```

### Tutorial 7 — Extract MT responses from an MPH file

1. Start a valid COMSOL session.
2. Click **Select MPH File**.
3. Choose the COMSOL model file.
4. Continue with the response-extraction workflow.

```{warning}
If the button is disabled, the COMSOL connection has not been initialized yet. Start the session first.
```

### Tutorial 8 — Open auxiliary tools

- Use **Tools → Anisotropy Calculator** to open the anisotropy-tensor utility.
- Use **Extras → Documentation** to open the online MT2COMSOL documentation.

----


## COMSOL workflow

### Installation status

The **Installation** panel checks whether the environment can see:

- the COMSOL server executable,
- and **LiveLink for MATLAB**.

Depending on the result, the GUI displays either:

- a ready/active message, or
- a warning indicating which component was not detected.

### Create input files

The **Create Input Files** button launches the workflow to prepare topography, bathymetry, coastline, station coordinates, and thin-layer conductance files for COMSOL using the function `MT2COMSOL_TopoBathy.m`. This step is the bridge between DEM preparation and COMSOL model building.

It guides the user through an interactive sequence that can include:

- Loading a **low-resolution DEM**.
- Optionally merging a **high-resolution DEM**.
- Using an existing **MT site variable**, or generating stations automatically.
- Cropping the final DEM domain.
- Optionally tapering topography radially.
- Extracting and selecting **coastline contours**.
- Generating **station support points**.
- Building the **topography** and **thin-layer conductance** files required by COMSOL.
- Optionally including a **sediment conductance** contribution.

The routine exports four main ASCII files:

- `Topography.txt`
- `ThinLayer.txt`
- `Coordinates.txt`
- `Coastline.txt` (if coastline contours are selected)

It can also save:

- `mt2comsol.mat` (if stations are generated automatically)
- `info.mat` or `info.txt`

### Optional predefined model-property clouds

Besides the topography and thin-layer files generated by `MT2COMSOL_TopoBathy.m`, COMSOL can also use an additional **point cloud** to define preassigned subsurface electrical properties.

This type of file is useful when the user wants to prescribe a model directly from external geometry or property distributions, instead of defining the entire structure manually inside COMSOL.

The file is typically organized as a cloud of points with coordinates in:

- `x` [m]
- `y` [m]
- `z` [m]

followed by either:

- a **single scalar property**, such as resistivity or conductivity, or
- the components of a **conductivity / resistivity tensor**, for example:
  - `sigma_xx`
  - `sigma_yy`
  - `sigma_zz`
  - `sigma_xy`
  - `sigma_xz`
  - `sigma_yz`

This allows the user to describe:

- isotropic models from scalar conductivity or resistivity,
- anisotropic models from tensor components,
- predefined 3-D structures derived from external modelling workflows.

A common workflow is to create this point cloud in **MT2ModEM**, where the user can draw geometries, insert bodies, and assign electrical properties before exporting the result for COMSOL.

By default, this file is typically named:

- `SupportPoints.txt`

```{note}
`SupportPoints.txt` is not generated automatically by `MT2COMSOL_TopoBathy.m` as part of the standard DEM workflow. It is an optional complementary input used when the user wants to impose predefined material-property distributions in COMSOL.
```

```{tip}
This approach is especially useful for building starting models that contain synthetic reservoirs, conductive bodies, anisotropic domains, or other predefined structures that are easier to construct outside COMSOL.
```

### MT2COMSOL_TopoBathy overview

#### DEM input from GeoTIFF or MATLAB DEM

The workflow supports two DEM entry paths:

- **GeoTIFF DEMs** (`*.tif`)
- **MATLAB DEM structures** (`*.mat`, containing variable `dem`)

For GeoTIFF workflows, the routine expects at least one **low-resolution DEM** and optionally a **high-resolution DEM**.

#### Flexible topography / bathymetry handling

For each DEM, the user can decide whether to preserve:

- **Topography**
- **Bathymetry**
- **Both**

This is useful when preparing models for:

- continental domains,
- coastal domains,
- ocean-influenced MT forward modelling.

#### Optional MT site input

The workflow can either:

- read an existing `mt` structure from a MAT-file, or
- generate a new station grid automatically.

If no MT site variable is provided, the routine creates a synthetic site distribution and saves it as `mt2comsol.mat`.

#### DEM refinement and domain control

The routine can:

- merge low- and high-resolution DEMs,
- crop the final model domain,
- apply a radial taper to positive topography,
- convert geographic grids into centered Cartesian coordinates.

#### Coastline and support-point generation

The workflow can extract zero-level contours from the DEM and export them as coastline support points.
It can also generate circular support-point clouds around stations to improve local topographic control near MT sites.

#### Thin-layer conductance generation

The routine builds a thin-layer conductance model that combines:

- a user-defined background resistivity,
- ocean conductance derived from bathymetry,
- optional sediment conductance.

----


### Before you start

Before running `MT2COMSOL_TopoBathy.m`, make sure you have:

- a project folder where the output files will be written,
- at least one DEM:
  - a low-resolution GeoTIFF, or
  - a MATLAB DEM structure,
- optionally:
  - a high-resolution GeoTIFF,
  - an MT structure stored in a MAT-file,
  - a sediment-thickness raster if you want to include sediments.

```{note}
The routine is highly interactive. Several choices are made through dialog windows, including DEM source, plotting, cropping, tapering, coastline selection, support points, and thin-layer settings.
```

```{warning}
If you choose the sediment option, the current implementation expects a raster file named `sediments_centered_0.tif` to be available to MATLAB.
```

----


### General workflow

The complete workflow can be summarized as follows:

1. Select the **project folder**.
2. Decide whether to **plot diagnostic results**.
3. Choose the DEM source:
   - **GeoTIF**
   - **Matlab DEM**
4. Load the **low-resolution DEM**.
5. Optionally load the **high-resolution DEM**.
6. Optionally load an **MT site variable**.
7. Build the **final DEM**.
8. Optionally **crop** the final DEM.
9. Optionally apply a **radial taper** to topography.
10. Extract and select **zero-level coastline contours**.
11. Define station coordinates:
    - from the existing `mt` structure, or
    - from an automatically generated grid.
12. Optionally generate **support points around stations**.
13. Export **Topography.txt** and **Coordinates.txt**.
14. Define background resistivity and build the **thin-layer conductance**.
15. Optionally include **sediment conductance**.
16. Export **ThinLayer.txt** and, if selected, **Coastline.txt**.
17. Save or print an **info** summary.

----


#### Step 1: Start the workflow and select the project folder

Run the function from MATLAB:

```matlab
MT2COMSOL_TopoBathy
```

If no input argument is provided, the routine first asks you to select the **project folder** where all output files will be saved.

```{tip}
Create one dedicated folder per COMSOL model setup. This keeps the exported ASCII files, station files, and metadata together.
```

----


#### Step 2: Choose whether to plot diagnostic results

After selecting the project folder, the routine asks:

- **Do you want to plot the results?**

If you choose:

- **Yes**: the workflow generates multiple diagnostic figures during DEM preparation, conductance generation, and contour selection.
- **No**: the workflow still runs, but no intermediate figures are shown.

```{note}
For first-time use, it is strongly recommended to choose **Yes**. The diagnostic plots are useful for checking DEM orientation, coastline extraction, station positions, and conductance maps.
```

----


#### Step 3: Select the DEM source

The next dialog lets you select the DEM source file type:

- **GeoTIF**
- **Matlab DEM**

##### Option A — GeoTIF

Choose this option if your terrain model is stored as one or more GeoTIFF files.

The routine then asks you to select:

1. a **low-resolution GeoTIFF**,
2. optionally a **high-resolution GeoTIFF**.

For each DEM, the routine also asks whether:

- topography should be preserved,
- bathymetry should be preserved.

##### Option B — Matlab DEM

Choose this option if you already have a MATLAB `.mat` file containing a variable named `dem`.

The structure is expected to contain fields such as:

- `HRdem`
- `unit`
- `R`
- `LAT`
- `LON`

```{warning}
If the selected MAT-file does not contain a variable named `dem`, the workflow stops and shows an error dialog.
```

----


#### Step 4: Load the low-resolution DEM

The low-resolution DEM defines the outer modelling region.

After choosing the file, the routine:

- reads the raster,
- fills missing values,
- optionally suppresses topography and/or bathymetry,
- applies Gaussian smoothing,
- converts coordinates to a centered Cartesian grid in kilometers.

If plotting is enabled, the DEM is displayed as a topobathymetry map.

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_plot_lr_dem.png"
       alt="Low-resolution DEM"
       width="70%">
</p>

```{note}
The low-resolution DEM is always required in the GeoTIFF workflow. It defines the background domain even when a high-resolution DEM is also used.
```

----


#### Step 5: Optionally load the high-resolution DEM

If you are working with a region of special interest, you can also load a **high-resolution DEM**.

This inner DEM is merged with the low-resolution DEM during the final-domain construction step.

Typical use cases include:

- volcanic edifices,
- coastal sectors with sharp bathymetric gradients,
- local high-priority target areas around MT sites.

The routine merges the low- and high-resolution DEMs on a combined grid using scattered interpolation.

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_plot_hr_dem.png"
       alt="High-resolution DEM"
       width="70%">
</p>

```{tip}
Use the high-resolution DEM only where it adds real value. Very large HR domains increase memory usage and may not significantly improve the COMSOL model.
```

----


#### Step 6: Optionally load an MT site variable

The routine next asks whether you want to load an existing MT site variable from a MAT-file.

If the selected file contains a variable named `mt`, the station coordinates are extracted and used directly.

If no MT structure is provided, the routine will later ask you to generate a station grid automatically.


```{note}
When an `mt` structure is used, station elevations are computed by interpolating the final DEM at the station positions.
```

----


#### Step 7: Build the final DEM

Once the DEM(s) and optional MT structure are loaded, the routine builds the **final DEM**.

This includes:

- selecting the reference center,
- merging LR and HR DEMs if both exist,
- rebuilding the grid,
- converting it to centered Cartesian coordinates.

The reference center is chosen as follows:

- from the `mt` structure if MT sites were provided,
- otherwise from the HR DEM center if an HR DEM exists,
- otherwise from the LR DEM center.

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_plot_final_xy.png"
       alt="Final DEM in centered Cartesian coordinates"
       width="70%">
</p>

----


#### Step 8: Optionally crop the DEM limits

The routine asks:

- **Change DEM limits?**

If you choose **Yes**, you can enter:

- `X min (km)`
- `X max (km)`
- `Y min (km)`
- `Y max (km)`

The DEM is then cropped to the closest available grid indices and all derived coordinate arrays are rebuilt.

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_window_crop_dem.png"
       alt="DEM cropping dialog"
       width="40%">
</p>

```{tip}
Cropping is useful to remove irrelevant outer areas and reduce the size of the exported topography and conductance grids.
```

----


#### Step 9: Optionally taper topography radially

The workflow then asks:

- **Apply radial taper to topography?**

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_option_taper.png"
       alt="Topography taper dialog"
       width="40%">
</p>

If you choose **Yes**, the routine requests two radii:

- **Inner radius**: full topography is preserved.
- **Outer radius**: topography is forced to zero.

A smooth cosine taper is applied only to **positive topography**.

Bathymetry remains unchanged.

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_window_taper.png"
       alt="Topography taper window"
       width="40%">
</p>

```{note}
This option is useful when you want to suppress distant topography gradually while preserving the central modeling area.
```

----


#### Step 10: Extract and select coastline contours

The routine extracts zero-level contours from the DEM and opens a contour-selection workflow.

Optional operations include:

- removing contour points outside a radius,
- resampling contour vertices at a chosen spacing,
- selecting only the contours you want to keep.

The selected contours can later be exported as:

- `Coastline.txt`

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_plot_contours.png"
       alt="All extracted zero-level contours"
       width="70%">
</p>

```{tip}
If your DEM contains multiple coastlines or islands, this step lets you keep only the geometries that are relevant for your COMSOL model.
```

----


#### Step 11: Define station coordinates

At this stage, the routine determines the station positions.

##### Case A — Existing MT structure

If an `mt` variable was loaded:

- station longitude/latitude are converted into centered Cartesian coordinates,
- station elevations are interpolated from the DEM,
- the coordinates are exported to `Coordinates.txt`.

##### Case B — Automatic station generation

If no MT structure was loaded, the routine creates stations interactively.

###### With a high-resolution DEM

You define:

- number of sites in **X**,
- number of sites in **Y**,
- buffer percentage inside the HR domain.

###### Without a high-resolution DEM

You define:

- number of sites in **X**,
- `X min`, `X max`,
- number of sites in **Y**,
- `Y min`, `Y max`.

The generated coordinates are projected onto the DEM. Invalid sites are removed, and the resulting station structure is saved as:

- `mt2comsol.mat`

```{warning}
Stations with invalid interpolated elevation, or stations that fall outside the DEM, are removed automatically.
```

----


#### Step 12: Optionally add support points around stations

The routine then asks:

- **Add support points around stations?**

If you choose **Yes**, you define:

- **Support radius (km)**
- **Lateral spacing (km)**

For each station, the routine generates a circular stencil of support points, projects them onto the DEM, removes invalid points, and appends them to the topography export.

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_option_support_points.png"
       alt="Support-point dialog"
       width="40%">
</p>

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_window_support_points.png"
       alt="Station support points around MT sites"
       width="40%">
</p>

```{tip}
Support points are useful when you want additional geometric control near MT sites without increasing the full DEM resolution everywhere.
```

----


#### Step 13: Export `Topography.txt` and `Coordinates.txt`

After DEM, station, support-point, and coastline preparation, the routine writes:

##### `Topography.txt`

This file contains:

- the DEM grid points,
- station coordinates,
- optional support points,
- optional coastline support points.

Coordinates are exported in:

- **meters** for X and Y,
- **meters** for elevation.

##### `Coordinates.txt`

This file contains the station coordinates used by the workflow.

```{note}
In the exported topography file, `DEM.dem0` is used. This means values below sea level are forced to zero in the topography export.
```

----


#### Step 14: Define the thin-layer conductance background

The routine then asks for:

- **Resistivity background (Ohm m)**

This value controls the background thin-layer conductance over land.

The current implementation uses:

- ocean resistivity = `0.3 Ohm m`
- thin-layer thickness = `100 m`

The conductance map is built as:

- **land**: `thinlayer / resistivity_bg`
- **ocean**: `abs(bathymetry) / resistivity_ocean`

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_window_bgr.png"
       alt="Background resistivity dialog"
       width="40%">
</p>

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_plot_conductance_from_dem.png"
       alt="Base conductance map from background and ocean bathymetry"
       width="70%">
</p>

----


#### Step 15: Optionally include sediment conductance

The workflow then asks:

- **Include sediment thickness?**

If you choose **Yes**, the routine reads a sediment-thickness raster and computes an additional conductance term.

This sediment conductance is then combined with the existing ocean/background conductance.

Diagnostic plots may include:

- sediment thickness,
- sediment conductance,
- total conductance.

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_option_sediment.png"
       alt="Sediment option dialog"
       width="40%">
</p>

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_plot_sediment_thickness.png"
       alt="Sediment thickness map"
       width="70%">
</p>

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_plot_conductance_from_sediment.png"
       alt="Sediment conductance map"
       width="70%">
</p>

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_plot_conductance_total.png"
       alt="Total conductance map"
       width="70%">
</p>

```{warning}
The sediment workflow assumes that the sediment raster is compatible with the DEM extent and coordinate system.
```

```{button-link} https://www.dropbox.com/your-real-link-here
:color: primary
:shadow:

Download `sediments_centered_0.tif`
```

----


#### Step 16: Resample and export `ThinLayer.txt`

Before export, the conductance model is resampled onto a coarser grid for COMSOL.

The current implementation uses:

- `NTX = 300`
- `NTY = 300`

If a high-resolution DEM exists, the conductance is sampled over both:

- the outer box,
- the inner high-resolution box.

The combined conductance points are interpolated onto a merged grid and then written to:

- `ThinLayer.txt`

If coastline contours were selected, coastline points are appended using background conductance values.


----


#### Step 17: Review and save the info summary

At the end of the workflow, the routine builds an `info` structure containing summary information such as:

- outer-box size,
- inner-box size,
- reference latitude and longitude,
- DEM elevation range,
- background resistivity,
- station metadata.

You can then choose to:

- save it as `info.mat`,
- save it as `info.txt`,
- print it to screen,
- close without saving.

<p align="center">
  <img src="../_static/images/mt2comsol/mt2comsol_option_info.png"
       alt="Info summary dialog"
       width="40%">
</p>

### Start COMSOL session

The **Start COMSOL Session** switch attempts to:

1. detect a valid COMSOL installation,
2. launch the COMSOL server,
3. prioritize the corresponding LiveLink MATLAB path,
4. connect MATLAB to COMSOL through `mphstart`.

When successful:

- the green lamp turns on,
- the red lamp turns gray,
- and **Select MPH File** becomes available.

When the switch is moved to **Off**, the GUI session is reset visually.

```{warning}
Setting the switch to **Off** resets the GUI-side session state, but it does **not** force-close an external COMSOL server process. If needed, that process must be closed manually.
```

### Extract MT responses

The **Select MPH File** button launches the transfer-function extraction workflow implemented in `MT2COMSOL_ExtractTF.m`.

This routine reads electromagnetic field solutions from a COMSOL `*.mph` model, interpolates them to user-defined MT site locations, and converts those fields into magnetotelluric transfer functions.

The workflow supports both:

- **2-D COMSOL models**
- **3-D COMSOL models**

Site coordinates can be provided in two ways:

- generated from a **regular grid**, or
- loaded from an existing **MT structure**.

The extraction workflow then:

1. loads the selected COMSOL model,
2. reads the available COMSOL solutions and frequencies,
3. asks the user to define the surface boundary used for field extraction,
4. evaluates the electric and magnetic fields on that surface,
5. interpolates those fields to the requested MT site locations,
6. builds the impedance tensor and tipper,
7. resolves any frequency mismatch between COMSOL solutions and the MT structure,
8. populates the final `mt` structure and computes derived quantities.

The resulting MT structure includes not only the extracted transfer functions, but also additional derived parameters such as:

- apparent resistivity and phase,
- phase tensor,
- CART / RT / RPT quantities.

The final result is saved as a `*.mat` file containing the variable:

- `mt`

```{note}
Site coordinates are handled internally in kilometers, while COMSOL coordinates are assumed to be defined in meters.
```

```{warning}
The extraction workflow is only available after a valid COMSOL session has been established. This is why **Select MPH File** remains disabled until the GUI successfully connects to COMSOL through LiveLink for MATLAB.
```

----


## Output files

### `Topography.txt`

Contains:

- DEM topography grid,
- station coordinates,
- optional support points,
- optional coastline points.

### `ThinLayer.txt`

Contains:

- resampled thin-layer conductance values used in COMSOL.

### `Coordinates.txt`

Contains:

- station coordinates exported in meters.

### `Coastline.txt`

Contains:

- selected coastline points, if coastline export was enabled.

### `mt2comsol.mat`

Contains:

- automatically generated `mt` structure,
- reference latitude and longitude.

### `info.mat` or `info.txt`

Contains:

- summary metadata of the generated modelling setup.

### `SupportPoints.txt`

Optional user-supplied point cloud for predefined scalar or tensor electrical properties in COMSOL.

----


## Troubleshooting

### DEM and TopoBathy issues

#### “Selected MAT file does not contain variable `dem`”

- Make sure the MATLAB DEM file contains a variable named `dem`.
- Confirm that `dem` includes the expected fields.

#### “Selected MAT file does not contain variable `mt`”

- Make sure the MT station file contains a variable named `mt`.
- Otherwise, continue without it and let the routine create a station grid automatically.

#### No valid stations remain after projection onto the DEM

- Check whether the station grid falls outside the DEM limits.
- Check whether the generated stations are located below sea level.
- Reduce the station window or adjust the HR-domain buffer.

#### Invalid taper radii

- Make sure the outer radius is larger than the inner radius.
- Both radii must be positive, and the inner radius can be zero.

#### DEM cropping gives an empty or unexpected result

- Make sure the requested X and Y limits overlap the DEM.
- Check the DEM coordinate orientation in the diagnostic figures.

#### Sediment conductance fails

- Make sure `sediments_centered_0.tif` is available.
- Confirm that the sediment raster overlaps the DEM geographic extent.

#### Exported files are not found in the project folder

- Check write permissions for the selected folder.
- If the main save attempt fails, the routine may fall back to the current MATLAB working directory.

#### DEM download fails

- Verify that **Latitude min/max** and **Longitude min/max** were computed correctly.
- Verify that the selected project folder exists.
- Prefer **GeoTIFF** format for the automatic workflow.

#### “The selected DEM format is not yet supported”

- In the current GUI implementation, choose **geotiff (.tif)** for automatic download.
- Other formats may appear in the drop-down, but they are not yet wired into the download workflow.

#### Skin depth does not update

- Check that frequency and resistivity values are positive.
- Ensure that **Min. Frequency** is not greater than **Max. Frequency**.

#### “Failed to create input files”

- Verify that the project folder exists and is writable.
- Check that the DEM and required auxiliary files are available.
- Review the detailed error message shown by the GUI.

#### “The selected MAT-file does not contain a variable named mt”

- The **Use Center from MT Structure** workflow expects a variable called `mt` inside the selected `*.mat` file.
- Rename or rebuild the file if needed.

### COMSOL connection and response extraction issues

#### “COMSOL and LiveLink for MATLAB were not detected”

- Verify that COMSOL is installed on the machine.
- Verify that **LiveLink for MATLAB** is installed and accessible from MATLAB.
- Check that the COMSOL server executable can be found by the current environment.

#### “No COMSOL installation with both Server and LiveLink was found”

- MATLAB may see a partial installation only.
- Confirm that the selected COMSOL version includes both:
  - server support,
  - and LiveLink for MATLAB.

#### The COMSOL session does not start

- Check whether the COMSOL server executable can be launched outside the GUI.
- Confirm that MATLAB can run `mphstart` successfully.
- If another session is already active, close it or reuse it intentionally.

#### “Select MPH File” stays disabled

- The button is enabled only after a successful COMSOL connection.
- Start the session first using **Start COMSOL Session**.
- If the connection fails, inspect the COMSOL / LiveLink installation.

```{tip}
For first-time setups, keep plotting enabled and save the final `info.txt`. This makes it much easier to trace domain size, reference coordinates, and output choices later.
```

```{note}
The current session-management utilities are strongly oriented toward a **Windows + MATLAB + COMSOL LiveLink** setup. This is especially relevant for server launching and folder opening.
```
