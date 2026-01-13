# nEMesis

nEMesis is a **next‑generation ElectroMagnetic evaluation and signal‑interpretation suite** built around the FFMT ecosystem.  
It provides a single entry point to manage **processing tasks**, explore **recorded time‑series**, run **post‑processing workflows**, and perform **temporal analyses**.

- **Version:** 3.0  
- **Release date:** 01‑Jan‑2026  
- **Authors:** César Castro, Philip Hering, Andreas Junge (2020–2026)  
- **Powered with:** FFMT and MAnTiS


----


## What you can do in nEMesis

nEMesis groups its functionality into four main modules (buttons in the main window):

### 1) Task Manager
Create, organize, and execute processing tasks.  
This is the control center for reproducible workflows where you define what to process, how to process it, and where outputs are stored.

- Launches: `nEMesis_TaskManager`

### 2) Recording Database
Browse and inspect recorded time‑series data and metadata, with fast navigation across stations/runs.  
Use it to locate recordings, verify availability, and check acquisition spans before or after processing.

- Launches: `nEMesis_RecordingDatabase`

### 3) Post Processing
Run analysis steps on already processed results (e.g., derived products, QC summaries, comparisons).  
This is where you turn “processed outputs” into interpretable figures and deliverables.

- Launches: `nEMesis_PostProcessing`

### 4) Temporal Analysis
Investigate how signals, noise conditions, and transfer‑function behavior evolve over time.  
Use it for stability checks, time‑lapse studies, and monitoring‑style workflows.

- Launches: `nEMesis_TemporalAnalysis`


----


## Settings (required before using the modules)

nEMesis expects two folders to be configured.  
If they are missing, the app displays an error alert at startup.

### A) Calibration folder
Stores calibration files and instrument‑specific resources used by the processing pipeline.

**GUI path:** `Settings → Calibration → Set Folder`  
**Open folder:** `Settings → Calibration → Open Folder`

Internally, the path is saved in:
- `Settings/path_calibration.mat` (variable: `path`)

### B) Processing Results folder
Stores processing outputs and any intermediate/derived products used by Post‑Processing and Temporal Analysis.

**GUI path:** `Settings → Results → Set Folder`  
**Open folder:** `Settings → Results → Open Folder`

Internally, the path is saved in:
- `Settings/path_processing.mat` (variable: `path`)

```{note}
At startup, nEMesis verifies that both saved paths exist and are valid directories.
If one is missing or points to a non‑existing folder, you will see an error message such as:
“Calibration Files is not added to path” or “Processing Results is not added to path”.
```


----


## Main window overview

The nEMesis start window is intentionally minimal:

- **Top menu**
  - **Settings**
    - Calibration (Set/Open Folder)
    - Results (Set/Open Folder)
  - **Extras**
    - Information
    - FFMT (Launch, Website)

- **Main panel**
  - Buttons to launch the four modules:
    - Task Manager
    - Recording Database
    - Post Processing
    - Temporal Analysis

- **Footer**
  - Version label and release date
  - Author line
  - “powered with MAnTiS” tag


----


## Quick start

### Step 1 — Configure folders
1. Open nEMesis.
2. Set the required paths:
   - `Settings → Calibration → Set Folder`
   - `Settings → Results → Set Folder`

### Step 2 — Start a workflow
Pick one entry point depending on what you want to do:

- **Need to define a processing run?** → open **Task Manager**
- **Need to find / inspect recordings first?** → open **Recording Database**
- **Already processed and want figures / QC?** → open **Post Processing**
- **Want time‑evolution / monitoring style analysis?** → open **Temporal Analysis**


----


## Extras

### Information
`Extras → Information` opens a quick info dialog with:
- the nEMesis tagline,
- version and release date,
- authorship,
- contact email.

### FFMT website
`Extras → FFMT → Website` opens the FFMT webpage in your browser.

```{note}
The website link is opened via MATLAB's `web()` function.
```


----


## Troubleshooting

### Startup warning about missing folders
If you see an error dialog during startup, it usually means one of the saved folder paths is missing or invalid.

Fix:
1. Go to `Settings → Calibration → Set Folder` and select the correct folder.
2. Go to `Settings → Results → Set Folder` and select the correct folder.
3. Restart nEMesis.

### Nothing happens when clicking a module button
Make sure the corresponding module entry function is on the MATLAB path, e.g.:
- `nEMesis_TaskManager`
- `nEMesis_RecordingDatabase`
- `nEMesis_PostProcessing`
- `nEMesis_TemporalAnalysis`

If a module is missing from path, MATLAB will throw an error when the button callback runs.


----


## Contact

- Email: `ffmtsoftware@gmail.com`
