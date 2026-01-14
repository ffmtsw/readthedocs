# Task Manager

nEMesis Task Manager is the **task / job / site** orchestration layer for nEMesis processing workflows in MATLAB.
It lets you create processing `tasks` that contain one or more `jobs`, each `job` operating on one or more MT stations (single-site or multi-site) and one or more sampling-frequency groups.

The app focuses on:
- **Reproducibility:** every job stores its processing parameters.
- **Traceability:** outputs are organized by Task/Job and a timestamped report is saved.
- **Scalability:** tasks can be executed “Selected” or “All”, and extended with utility modules.

---

## Core concepts

### Task
A **Task** is the top-level container saved as a `.mat` file. It includes:
- Task metadata (`task.name`, creation/modification info)
- A list of **jobs**
- Global UI/state fields (if applicable)

### Job
A **Job** is a processing unit inside a task. Each job typically defines:
- A **time range** (`job.ts.t(1)` start, `job.ts.t(end)` end; MATLAB datenums)
- A **sampling-frequency group** (one job can include multiple frequency groups depending on your design)
- One or more **sites** (stations) to process (single-site or multi-site)
- Processing parameters (segmentation, overlap, filtering, ranking, etc.)

### Site
A **Site** (station) contains metadata required for processing:
- Site name / ID
- File paths / run selection
- Channels and instrument metadata (when applicable)
- Any constraints used by the downstream processing pipeline

---

## What the Task Manager does

When you execute a task/job, the app should:
- Generate processing outputs in an organized output directory
- Save a timestamped **Processing Report** (MAT-file) summarizing:
  - Task/job identifiers
  - Input time range and sites
  - Key parameter values
  - Execution logs / warnings (if tracked)
  - Paths to generated artifacts

Output naming is typically of the form:
- `Processing Report - <timestamp>.mat`
- plus any processing products your pipeline creates (e.g., intermediate spectra, transfer functions, EDI/FFMT outputs)

---

## Main GUI Components

### Top bar (menus)
- **File → Load**: load time series from supported formats/instruments.
- **File → Reset**: reset the app (clears tasks, jobs, tables).
- **Modules**: open related modules (e.g., Recording Database, Post-processing).
- **Utilities → Tasks**: helper functions (Auto Tasks, Merge Tasks, SingleSite→MultiSite, etc.).

### Main panels
- **Task selector**: `TasklistDropDown` + Task/Job counters.
- **table_job**: editable table with per-job parameters.
- **table_site**: editable table with per-site parameters.
- **ProcessingParametersPanel**: segmentation, overlap, filters, ranking, etc.
- **Results / status**: `StatusLabel` + “Processing” icon feedback.

---

## Data model (what is stored in the `.mat` task file)

A typical structure is:

- `task.name` — task name (string)
- `task.job(i)` — i-th job struct
  - `task.job(i).name` — job name / label
  - `task.job(i).ts.t` — time vector (MATLAB datenum)
  - `task.job(i).sites` — list/struct array of selected sites
  - `task.job(i).params` — processing parameters (segmentation, overlap, etc.)

> Note: field names can vary across versions. The key idea is that **every parameter required to reproduce the run**
> is stored inside the task/job structure.

---

## Typical workflow (end-to-end)

1. **Create a new task** (e.g., `+` button).
2. **Load time series** (`File → Load → Instrument`).
3. **Review / edit site metadata** in `table_site`.
4. **Create or select a job** in `table_job`.
5. **Assign site(s) to the job** (e.g., “Set site”).
6. **Tune processing parameters** (frequency, segmentation, overlap, ranking, filtering).
7. **Save the task** to a `.mat` file.
8. **Execute**
   - **Selected**: run the highlighted job(s)
   - **All**: run all jobs in the task
9. **Inspect outputs** + the saved processing report.

---

## Job table (`table_job`) — recommended columns

Common job columns include:
- **Job name**
- **Start time** / **End time** (MATLAB time or human-readable mapping)
- **Sampling frequency group**
- **Sites count**
- **Overlap / segmentation parameters**
- **Filter settings**
- **Ranking settings**
- **Output folder** (optional)
- **Enabled** (optional boolean to skip jobs)

If you keep the UI table editable, ensure edits are mirrored back into the `task.job(i)` struct.

---

## Site table (`table_site`) — recommended columns

Common site columns include:
- **Site ID / name**
- **Instrument / format**
- **Folder / file path**
- **Channel availability**
- **Coordinates** (if needed by mapping tools)
- **Start/stop availability** (optional)
- **Flags / notes** (e.g., “bad coil”, “partial data”, etc.)

---

## Processing parameters (what matters most)

### Segmentation
Key values typically include:
- Window length rule (fixed samples or frequency-adaptive)
- Detrending strategy
- Handling of gaps / discontinuities

### Overlap
Overlap controls how consecutive windows share samples. Common patterns:
- 0% overlap (fast, less redundancy)
- 50% overlap (common compromise)
- >50% overlap (more redundancy, higher compute cost)

### Filtering
Typical options:
- FIR band-pass or low/high-pass as a function of a target frequency band
- Notch filters (if required by known noise sources)

### Ranking / selection
Often you compute transfer-function estimates from a subset of “best” windows:
- Rank windows by a metric (e.g., coherence, robust residual, SNR proxy)
- Keep top X% (e.g., top 50%)
- Fit a smoothing model (e.g., local polynomial) and select estimates closest to the fit

---

## Execution modes

### Execute Selected
Runs only the currently selected job(s). Use when iterating on parameters.

### Execute All
Runs the entire task. Use after your configuration is stable.

### Parallelization (optional)
If your pipeline supports it, execution can be wrapped in `parfor` at:
- Site level (sites in a job)
- Window/segment level (inside a site)
- Frequency-band level (if your architecture allows)

---

## Utilities (Tasks menu)

Typical utilities you may expose:
- **Auto Tasks**: generate jobs automatically from a folder structure or metadata rules.
- **Merge Tasks**: combine two tasks into a single task file.
- **SingleSite → MultiSite**: convert two single-site tasks into a multi-site combined task (useful for remote reference workflows).
- **Validate overlaps**: find job pairs that overlap in time by at least a user-defined threshold and auto-generate combined tasks.

---

## Common pitfalls and best practices

- **Always save tasks before running**: it preserves a stable snapshot of your configuration.
- **Keep job time ranges explicit**: avoid implicit “latest data” assumptions.
- **Version your task format**: add `task.version` and migrate fields when needed.
- **Log everything**: paths, warnings, excluded segments, and the exact parameter values used.

---

## Troubleshooting checklist

- Job runs but outputs are empty:
  - confirm time range overlaps available data
  - confirm site paths are correct
  - check channel mapping (Ex/Ey/Hx/Hy/Hz)

- Job fails quickly:
  - inspect the MATLAB command window for the first thrown error
  - verify the “active” job has valid parameters
  - try running a single site/job first

- Inconsistent results across runs:
  - ensure ranking selection is deterministic (seed random components)
  - ensure you are not mixing different calibration versions

---

## Quick Start (paste this at the top of the repo)

1. Open `nEMesis_TaskManager`.
2. Create a new task (`+`).
3. Load time series (`File → Load → Instrument`).
4. Review site metadata in `table_site`.
5. Add site(s) to a job (`Set site`).
6. Tune processing parameters (frequency, segmentation, overlap, ranking).
7. Save the task to `.mat`.
8. Execute (Selected/All).
9. Inspect the output folder and the generated `Processing Report - <timestamp>.mat`.

---
---

## Tutorials

These short, practical walkthroughs match the intended “Task → Job → Site” workflow. They assume the app is already open.

### Tutorial 1 — Create your first Task and Job
1. Click **`+`** (or **New Task**) and name the task (e.g., `Test_Task_01`).
2. Confirm the task appears in **`TasklistDropDown`**.
3. In **`table_job`**, add a new row (or use the app’s “Add Job” control).
4. Set:
   - **Job name** (e.g., `Job_01`)
   - **Start time / End time** (or the time-range selector used by your build)
   - **Sampling-frequency group** (if your UI exposes it per job)

### Tutorial 2 — Load data and attach Site(s) to the Job
1. Go to **File → Load → (Instrument/Format)** and select the folder/files.
2. Verify the loaded stations appear in **`table_site`**.
3. Select the job in **`table_job`**.
4. Use **Set site** (or equivalent) to attach one or more sites to the selected job.
5. (Optional) Edit **`table_site`** fields such as site ID, paths, notes, channel availability, etc.

### Tutorial 3 — Configure segmentation and overlap
1. Open **Processing Parameters** (segmentation/overlap panel).
2. Choose a segmentation strategy:
   - **Fixed window length** (samples/seconds), or
   - **Frequency-adaptive windows** (shorter for high f, longer for low f).
3. Set **overlap** (e.g., 0%, 50%).
4. If available, set gap handling options (skip, interpolate, split around gaps).
5. Save the task after changes.

### Tutorial 4 — Run “Execute Selected” (recommended for iteration)
1. Highlight the job you want to test in **`table_job`**.
2. Click **Execute Selected**.
3. Watch the status area (**StatusLabel / processing indicator**).
4. After completion, open the output folder and locate:
   - `Processing Report - <timestamp>.mat`
   - Any pipeline products (spectra, TFs, EDI/FFMT outputs, etc.)
5. If results look off, adjust parameters and repeat.

### Tutorial 5 — Run “Execute All” (full batch)
1. Ensure **all jobs** you want are correctly configured (time ranges, sites, params).
2. Save the task to `.mat`.
3. Click **Execute All**.
4. Verify each job produced its own report/output folder structure.

### Tutorial 6 — Convert two Single-Site tasks into one Multi-Site task (remote reference)
This is typically used to generate a combined task for A vs. B processing.
1. Open **Utilities → Tasks → SingleSite → MultiSite** (or your equivalent menu item).
2. Select two task files (e.g., `task_A.mat` and `task_B.mat`).
3. Choose:
   - The **minimum overlap** required (e.g., 6 hours)
   - Any naming convention for the new combined task
4. Run the utility and verify a new task is saved (e.g., `task_A_vs_B.mat`).
5. Open the combined task in the Task Manager and confirm both site sets are present.

### Tutorial 7 — Merge two tasks into one
1. Open **Utilities → Tasks → Merge Tasks**.
2. Select the two `.mat` task files to merge.
3. Decide how to resolve conflicts (if prompted):
   - Keep both job names (auto-rename collisions), or
   - Prefer one task’s metadata.
4. Save the merged task and verify that the resulting `task.job` list contains all expected jobs.

### Tutorial 8 — Validate overlaps and auto-generate combined tasks
If your workflow supports automatically creating A vs. B pairs based on time overlap:
1. Open **Utilities → Tasks → Validate overlaps** (name may vary).
2. Select the folder containing candidate task files.
3. Set the **minimum overlap duration** (e.g., 12 hours).
4. Run the tool:
   - It scans `job.ts.t(1)` and `job.ts.t(end)` for overlaps.
   - It generates combined tasks for every valid A vs. B pair.
5. Review the generated task files and spot-check their job time ranges.

---

*Last updated:* 2026-01-13


## GUI overview

The Task Manager window is designed around a **three-level hierarchy**:

- **Tasks** → the *container* (a `.mat` file) that groups related processing work.
- **Jobs** → the *units of work* inside a task (typically split by sampling rate, time range, processing approach, etc.).
- **Sites** → the *stations* (single-site or multi-site sets) attached to a job.

Most actions in the GUI follow the same pattern: **select an item in the current level** (task/job/site) and then use the **toolbar icon buttons** to add/edit/remove/duplicate/validate/run/export.

---

## Toolbar icon buttons

The icon bar contains **mode buttons** (to switch what you are browsing) and **action buttons** (to operate on the currently selected items).  
If your build uses different icon names, keep the descriptions below and adjust only the button labels.

### Mode buttons (navigation)

| Button | What it shows | What it operates on |
|---|---|---|
| **Tasks** | The list of available tasks (open or recently used). | Task-level actions: create/open/save/rename/duplicate/export. |
| **Jobs** | The list of jobs inside the *currently selected task*. | Job-level actions: add/edit/remove/reorder/validate. |
| **Sites** | The list of sites/stations inside the *currently selected job*. | Site-level actions: add/import/remove/edit/reorder. |

**Typical workflow:** **Tasks → Jobs → Sites → Validate → Run → Export**.

### Action buttons (common)

Below is a recommended, ReadTheDocs-friendly description of the most common toolbar pushbuttons.

#### Task actions (when **Tasks** mode is active)

- **New Task**: Creates a new empty task structure with a default name and metadata fields.
- **Open Task**: Loads an existing task from a `.mat` file and populates Jobs/Sites views.
- **Save Task**: Saves the current task back to disk (overwrites the existing file).
- **Save As**: Saves the current task under a new file name/path.
- **Duplicate Task**: Creates a copy of the selected task (useful for “what-if” processing variants).
- **Export**: Exports a human-readable summary (e.g., `.json`/`.yaml`/`.txt` depending on your build) for sharing or logging.
- **Close Task**: Unloads the task from the GUI without deleting it from disk.

#### Job actions (when **Jobs** mode is active)

- **Add Job**: Inserts a new job into the selected task (you will then define time range, sampling rate(s), processing settings, etc.).
- **Edit Job**: Opens the job editor for the selected job (recommended before adding many sites).
- **Remove Job**: Deletes the selected job from the task (does not delete raw data on disk).
- **Duplicate Job**: Copies a job including its configuration (optionally with/without sites, depending on implementation).
- **Move Up / Move Down**: Reorders jobs (order can matter if you batch-run or export summaries in a specific sequence).
- **Validate Job**: Checks that required fields are set (time range, sampling rate(s), site list, paths, etc.) and reports issues.

#### Site actions (when **Sites** mode is active)

- **Add Site**: Adds a single site/station entry to the selected job.
- **Import Sites**: Bulk-imports sites from a list (e.g., text/CSV/EDI-derived station list), creating one entry per station.
- **Edit Site**: Edits metadata for the selected site (name, coordinates, channel mapping, instrument info, etc., depending on your build).
- **Remove Site**: Removes the selected site from the job.
- **Duplicate Site**: Copies a site entry (useful if multiple stations share the same channel setup or metadata pattern).
- **Reorder Sites**: Changes the order of stations (mainly for visual organization and deterministic exports).

### Processing buttons (run controls)

Many builds include run controls on the same toolbar:

- **Run Selected**: Executes processing for the selected task/job/site (based on the current mode).
- **Run All**: Executes all jobs (and all sites inside them) for the active task.
- **Stop / Abort**: Stops the current run safely (implementation-dependent; may wait for the current segment to finish).
- **Progress / Log**: Opens the run log and progress view (errors and warnings should be visible here).

### Quality-of-life buttons (optional but common)

- **Refresh**: Reloads the current view from the in-memory task structure.
- **Search / Filter**: Filters lists by name, sampling rate, time window, etc.
- **Info / Help**: Shows tooltips, version information, and links to documentation.
- **Settings**: Opens global preferences (default paths, naming conventions, validation rules).

---

## What “selecting” means in each view

- In **Tasks** view: selection determines *which task file* is active.
- In **Jobs** view: selection determines *which job* you are editing/validating/running.
- In **Sites** view: selection determines *which stations* are being added/edited/removed/run.

A frequent source of confusion is applying an action in the wrong mode.  
If a button appears disabled, switch to the correct view (**Tasks / Jobs / Sites**) and ensure an item is selected.

