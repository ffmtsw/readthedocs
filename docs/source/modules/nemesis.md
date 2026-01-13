# nEMesis

nEMesis stands for **n**ext‑generation **E**lectro**M**agnetic **e**valuation and **s**ignal‑**i**nterpretation **s**uite built around the FFMT ecosystem. It provides a single entry point for managing **processing tasks**, exploring **recorded time‑series**, running **post‑processing workflows**, and performing **temporal analyses**.

- **Version:** 3.0  
- **Release date:** 01‑Jan‑2026  
- **Authors:** César Castro, Philip Hering, Andreas Junge (2020–2026)  
- **Powered with:** FFMT and MAnTiS


----


## What you can do in nEMesis

nEMesis groups its functionality into four main modules:

### 1) Task Manager
Create, organize, and execute processing tasks.  
This is the control center for reproducible workflows, where you define what to process, how to process it, and where to store outputs.

- Launcher: `nEMesis_TaskManager`

### 2) Recording Database
Browse and inspect recorded time‑series data and metadata, with fast navigation across stations/runs.  
Use it to locate recordings, verify availability, and check acquisition spans before or after processing.

- Launcher: `nEMesis_RecordingDatabase`

### 3) Post Processing
Run analysis steps on already processed results (e.g., derived products, QC summaries, comparisons).  
This is where you turn “processed outputs” into interpretable figures and deliverables.

- Launcher: `nEMesis_PostProcessing`

### 4) Temporal Analysis
Investigate how signals, noise conditions, and transfer‑function behavior evolve over time.  
Use it for stability checks, time‑lapse studies, and monitoring‑style workflows.

- Launcher: `nEMesis_TemporalAnalysis`


----


## Before you start

### Step 1 — Configure folders
1. Open nEMesis.
2. Set the required paths:
   - `Settings → Calibration → Set Folder`: Internally, the path is saved in: `Settings/path_calibration.mat` (variable: `path`)
   - `Settings → Results → Set Folder`: Internally, the path is saved in: `Settings/path_processing.mat` (variable: `path`)

### Step 2 — Start a workflow
Pick one entry point depending on what you want to do:

- **Need to define a processing run?** → open **Task Manager**
- **Need to find / inspect recordings first?** → open **Recording Database**
- **Already processed and want figures / QC?** → open **Post Processing**
- **Want time‑evolution / monitoring style analysis?** → open **Temporal Analysis**


```{note}
At startup, nEMesis verifies that both saved paths exist and are valid directories.
If one is missing or points to a non‑existing folder, you will see an error message such as:
“Calibration Files is not added to path” or “Processing Results is not added to path”.
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
