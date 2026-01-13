# Recording Database

The **Recording Database** is the central place in **nEMesis** to **browse, organize, and QC recorded time-series data** before turning them into processing tasks.
It is designed to make it easy to answer questions like:

- *What did we record, when, and with which instrument/sampling rate?*
- *Which stations overlap in time and can be used as remote references?*
- *Are there gaps, timing issues, clipped channels, or obvious contamination?*
- *Which recordings should become tasks for the Task Manager?*

---

## What the Recording Database does

### 1) Index recordings into a searchable catalog

The Recording Database builds (or loads) a catalog of recordings from your configured folders (see **Settings → Results**).
Each recording entry typically contains:

- Station / site name
- Instrument and format (e.g., Metronix ADU, Phoenix MTU, LEMI, etc.)
- Sampling rate(s)
- Start / end time (UTC)
- Channel list (Ex/Ey/Bx/By/Bz + optional auxiliaries)
- File path(s) and run identifiers
- Optional GPS / metadata fields (lat/lon/elevation, coil serials, dipole lengths)

```{note}
nEMesis is “powered with MAnTiS”, so the database is designed to integrate naturally with **task-based processing** workflows.
```

### 2) Help you choose valid processing + remote-reference pairs

Because MT processing depends heavily on **time overlap**, the database view is optimized for:

- spotting overlapping time spans across stations,
- quickly validating candidate remote references,
- ensuring compatible sampling rates and channel availability.

### 3) Lightweight QC and selection

The goal is *fast decisions*, not full processing. Typical QC actions:

- Preview short time windows (quick look)
- Verify channel presence and polarity
- Check for timing anomalies or obvious gaps
- Mark recordings as “usable / questionable / ignore”
- Add notes that persist with the catalog

---

## Typical workflow

1. Open **nEMesis → Recording Database**
2. Ensure your **Results** folder is configured:
   - `Settings → Results → Set Folder`
3. Load or build the catalog:
   - “Scan folder(s)” / “Update index” (exact wording depends on your build)
4. Search + filter recordings by:
   - station, date range, sampling rate, instrument, tags
5. Select recordings and:
   - send them to **Task Manager**, or
   - export a selection list for later processing

```{tip}
Use the Recording Database first, then create tasks. It prevents building tasks from bad or incompatible recordings.
```

---

## Main features

### A) Filters & search

Common filters include:

- Station / site name
- Date range (start/end)
- Sampling rate
- Instrument / manufacturer
- “Has channels” (Ex/Ey/Bx/By/Bz)
- “Has GPS”
- Tags (e.g., *remote*, *noisy*, *night*, *storm*)

### B) Recording preview (QC)

Depending on your build, preview tools may include:

- Time-domain quick plot (short window)
- Spectra / PSD quick plot
- Gap and continuity check
- Clipping / saturation detection (simple thresholds)

```{warning}
QC here is intended for **screening**. For final QC metrics and robust estimates, use FFMT/MAnTiS processing results.
```

### C) Selection and export

Typical outputs:

- Send selection to **Task Manager** (recommended)
- Export a CSV/TSV list of recordings
- Save an updated catalog file (so you don’t need to rescan every time)

---

## Data model (conceptual)

The database usually behaves like a table of entries:

- **Entry** = one recording unit (station + run + sampling rate)
- **Station** = a site label grouping multiple entries
- **Run** = a continuous (or mostly continuous) time interval
- **Channels** = Ex/Ey/Bx/By/Bz (+ optional)

This mapping is intentionally aligned with the **Task Manager** concept:

- a *task* can contain one or more jobs,
- a *job* typically corresponds to one sampling-rate group and one or more stations.

---

## Quick start tutorials

### Tutorial 1 — Build or refresh the catalog

1. Open **Recording Database**
2. Click **Scan / Update / Refresh** (your build may use different words)
3. Wait for indexing to finish
4. Confirm:
   - stations appear in the left list (or main table),
   - time spans and sampling rates are populated.

```{note}
If indexing returns an empty table, check your configured Results folder in **Settings → Results**.
```

### Tutorial 2 — Find good remote reference candidates

1. Select your target station (local site)
2. Set a **time overlap filter** (if available)
3. Sort by:
   - longest overlap,
   - closest distance (if GPS available),
   - matching sampling rate.
4. Preview a short window in both stations to check obvious issues
5. Send selected pair(s) to **Task Manager**

### Tutorial 3 — Export a selection list

1. Filter recordings down to a campaign window (e.g., specific week)
2. Select all visible entries
3. Use **Export → CSV/TSV** (or similar)
4. Store the exported list next to your processing folder for traceability

---

## Troubleshooting

### “No recordings found”

- Verify **Settings → Results → Set Folder** points to the correct directory.
- Ensure the folder actually contains the expected run structure/files.
- If your recordings are in subfolders, confirm that recursive scanning is enabled (if supported).

### “Times look wrong (shifted)”

- Check whether the instrument stores timestamps in local time vs UTC.
- Confirm that the loader is reading the correct header fields for your instrument format.
- If this affects only one station family, the loader may need a format-specific fix.

### “Stations overlap but processing fails later”

- Confirm sampling rate compatibility (or confirm that decimation is planned in Task Manager).
- Verify that the channels required for your processing approach exist (e.g., both Bx/By at remote sites).
- If the overlap is small, increase the overlap requirement for stable robust estimation.

---

## Related pages

- **Task Manager**: create and execute tasks/jobs based on selections.
- **Post Processing**: inspect and curate transfer-function results.
- **Temporal Analysis**: long-term trends, stability, and noise evolution.
