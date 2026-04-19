# MT2COMSOL GUI

MT2COMSOL is a **GUI-based front end** to prepare model-domain inputs for COMSOL, manage the COMSOL + LiveLink session from MATLAB, and launch the MT response-extraction workflow.

It focuses on:

- Estimating **skin depth** from the selected MT frequency range and a reference resistivity.
- Defining the model domain in **local Cartesian coordinates** and converting it to **geographic DEM limits**.
- Downloading and plotting **DEM / topobathymetry** data.
- Generating COMSOL-ready ASCII input files for topography, thin-layer conductance, site coordinates, and coastline support.
- Starting a COMSOL server session through **LiveLink for MATLAB**.
- Opening the next processing steps through **Anisotropy Calculator** and **response extraction** tools.

![MT2COMSOL main GUI](../_static/modules/mt2comsol_gui.png)

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

### DEM and Model Domain Setup

- **Max. Frequency [Hz]** (numeric edit field): Sets the highest MT frequency used to estimate the shallowest skin depth.

- **Min. Frequency [Hz]** (numeric edit field): Sets the lowest MT frequency used to estimate the deepest skin depth.

- **Resistivity [Ohmm]** (numeric edit field): Defines the reference resistivity used for the skin-depth estimate.

- **Skin depth min [km]** (read-only numeric field): Displays the estimated minimum skin depth.

- **Skin depth max [km]** (read-only numeric field): Displays the estimated maximum skin depth.

- **Central Latitude [deg]** (numeric edit field): Sets the reference latitude of the model domain.

- **Central Longitude [deg]** (numeric edit field): Sets the reference longitude of the model domain.

- **Use Center from MT Structure** (button): Loads a `*.mat` file, reads the variable `mt`, and uses its center as the domain reference.

- **Easting min. [km]** (numeric edit field): Minimum x-extent relative to the reference center.

- **Easting max. [km]** (numeric edit field): Maximum x-extent relative to the reference center.

- **Northing min. [km]** (numeric edit field): Minimum y-extent relative to the reference center.

- **Northing max. [km]** (numeric edit field): Maximum y-extent relative to the reference center.

- **Calculate Limits** (button): Converts the local extents into geographic limits and computes the total area.

- **Latitude min. [deg]** (read-only numeric field): Southern geographic limit of the DEM window.

- **Latitude max. [deg]** (read-only numeric field): Northern geographic limit of the DEM window.

- **Longitude min. [deg]** (read-only numeric field): Western geographic limit of the DEM window.

- **Longitude max. [deg]** (read-only numeric field): Eastern geographic limit of the DEM window.

- **Area [km2]** (read-only numeric field): Displays the area of the selected domain.

- **Format** (drop-down): Selects the DEM output format requested from the automatic download workflow.

- **Resolution** (drop-down): Selects the DEM sampling density.

- **Plot DEM** (check box): If enabled, plots the DEM immediately after download.

- **Select Folder** (button): Chooses the working folder where DEM and COMSOL input files will be stored.

- **Folder** (read-only text field): Displays the selected project folder.

- **Download DEM** (button): Downloads the DEM for the current geographic limits using the selected settings.

- **Open Folder** (button): Opens the selected working directory in the system file explorer.

### Modeling Workflow

- **Installation** (status panel): Reports whether COMSOL and LiveLink for MATLAB are available.

- **Download DEM** (button, DEM panel): Opens the GMRT website for manual DEM download.

- **Plot DEM** (button, DEM panel): Opens the DEM plotting utility.

- **Create Input Files** (button): Launches the COMSOL input-file generator for the selected project folder.

- **Start COMSOL Session** (slider switch): Starts or resets the GUI-side COMSOL session.

- **Status lamps** (red/green): Indicate whether a COMSOL connection is inactive or active.

- **Select MPH File** (button): Opens the MT response-extraction workflow. This button is enabled only when a valid COMSOL session is active.

### Menu entries

- **Tools → Anisotropy Calculator**: Opens the anisotropy-tensor calculator.

- **Extras → Documentation**: Opens the online documentation page for MT2COMSOL.

----


## DEM and model-domain setup

### Frequency range and skin-depth estimate

The **Frequency and Skin Depth** panel is the natural starting point of the GUI.
You provide:

- the highest frequency,
- the lowest frequency,
- and a reference resistivity,

and the GUI updates the expected shallow and deep skin-depth estimates automatically.

This is useful as a quick planning tool before defining the final domain size.
It gives a first-order idea of the spatial scale that may be relevant for the model.

```{note}
The shallowest skin depth is linked to the **highest frequency**, while the deepest skin depth is linked to the **lowest frequency**.
```

### Reference coordinates

The **Reference Coordinates** panel defines the center of the working domain.
You can either:

- type the latitude and longitude manually, or
- press **Use Center from MT Structure** to load the center automatically from a saved `mt` structure.

This center is later used to:

- define local x/y coordinates in kilometers,
- convert between local and geographic coordinates,
- and compute DEM download limits.

### Domain extents in kilometers

The **Domain Extents** panel defines the model size relative to the reference center.
The four fields represent the minimum and maximum local limits:

- `xmin`, `xmax`
- `ymin`, `ymax`

all in **kilometers**.

These limits define the area that will later be converted into geographic coordinates for DEM download and topography preparation.

### Geographic limits and area

After defining the center and local extents, press **Calculate Limits**.
The GUI converts the local domain into:

- latitude min / max,
- longitude min / max,
- and total area in square kilometers.

These fields are read-only because they are derived values.

```{tip}
A practical workflow is: first define the local domain in kilometers, then use **Calculate Limits**, and only after that proceed to DEM download.
```

### DEM download settings

The **DEM Download Settings** panel controls the automatic DEM request.
You can define:

- the file format,
- the resolution,
- whether the DEM should be plotted after download,
- and the destination folder.

The folder selected here is reused later by the input-file generator.

```{warning}
In the current GUI workflow, automatic DEM download is effectively implemented for **GeoTIFF** output.
If another format is selected, the GUI reports that it is not yet supported.
```

----


## DEM utilities

### Download DEM (manual GMRT access)

The **Download DEM** button in the **DEM** panel opens the **GMRT Map Tool** in your web browser.
This is useful when you want to download the terrain manually instead of using the automatic workflow.

```{note}
The GUI displays an information message recommending **GeoTIFF** files for the downstream MT2COMSOL workflow.
```

### Plot DEM

The **Plot DEM** button opens the DEM plotting utility.
This is intended for quick visual inspection of an existing DEM or GeoTIFF file before running the model-building workflow.

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

The **Create Input Files** button launches the topography / thin-layer preparation workflow for the selected project folder.
This step is the bridge between DEM preparation and COMSOL model building.

The detailed behavior of this workflow will be documented in the dedicated **input-files tutorial**.

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
Setting the switch to **Off** resets the GUI-side session state, but it does **not** force-close an external COMSOL server process.
If needed, that process must be closed manually.
```

### Extract MT responses

The **Select MPH File** button launches the MT response-extraction workflow.
This step is intentionally blocked until a valid COMSOL session is active.

That prevents users from attempting response extraction before the MATLAB–COMSOL connection is ready.

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
3. Click **Calculate Limits**
4. Inspect the resulting:
   - geographic limits,
   - and **Area [km2]**

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
The automatic download workflow requires valid latitude/longitude limits and a valid destination folder.
If either is missing, the GUI will stop and show a warning dialog.
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
A separate tutorial should document this workflow in detail with screenshots and example files.
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
If the button is disabled, the COMSOL connection has not been initialized yet.
Start the session first.
```

### Tutorial 8 — Open auxiliary tools

- Use **Tools → Anisotropy Calculator** to open the anisotropy-tensor utility.
- Use **Extras → Documentation** to open the online MT2COMSOL documentation.

----


## Troubleshooting

### “COMSOL and LiveLink for MATLAB were not detected”

- Verify that COMSOL is installed on the machine.
- Verify that **LiveLink for MATLAB** is installed and accessible from MATLAB.
- Check that the COMSOL server executable can be found by the current environment.

### “No COMSOL installation with both Server and LiveLink was found”

- MATLAB may see a partial installation only.
- Confirm that the selected COMSOL version includes both:
  - server support,
  - and LiveLink for MATLAB.

### The COMSOL session does not start

- Check whether the COMSOL server executable can be launched outside the GUI.
- Confirm that MATLAB can run `mphstart` successfully.
- If another session is already active, close it or reuse it intentionally.

### “Select MPH File” stays disabled

- The button is enabled only after a successful COMSOL connection.
- Start the session first using **Start COMSOL Session**.
- If the connection fails, inspect the COMSOL / LiveLink installation.

### DEM download fails

- Verify that **Latitude min/max** and **Longitude min/max** were computed correctly.
- Verify that the selected project folder exists.
- Prefer **GeoTIFF** format for the automatic workflow.

### “The selected DEM format is not yet supported”

- In the current GUI implementation, choose **geotiff (.tif)** for automatic download.
- Other formats may appear in the drop-down, but they are not yet wired into the download workflow.

### Skin depth does not update

- Check that frequency and resistivity values are positive.
- Ensure that **Min. Frequency** is not greater than **Max. Frequency**.

### “Failed to create input files”

- Verify that the project folder exists and is writable.
- Check that the DEM and required auxiliary files are available.
- Review the detailed error message shown by the GUI.

### “The selected MAT-file does not contain a variable named mt”

- The **Use Center from MT Structure** workflow expects a variable called `mt` inside the selected `*.mat` file.
- Rename or rebuild the file if needed.

```{note}
The current session-management utilities are strongly oriented toward a **Windows + MATLAB + COMSOL LiveLink** setup.
This is especially relevant for server launching and folder opening.
```
