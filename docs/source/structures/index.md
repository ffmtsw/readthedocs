# Structures

FFMT relies on a small set of **standard MATLAB structures** to keep data and metadata consistent across modules.
These containers define *how information is stored, passed, and interpreted* across the workflow: from raw time series, to transfer functions, to model construction and synthetic studies.

Below is a short overview of the main structures. Use the linked pages for details.

---

## ``ts`` — Time series container

The ``ts`` structure stores **raw (or lightly processed) electromagnetic time series** together with all metadata required to interpret the recording correctly.
It bundles the time vector, sampling rate, channel names/mapping, site coordinates, sensor/dipole geometry, gap tracking, and calibration information.

Typical use: loaders → QC → filtering/decimation → segmentation/spectral estimation.

[Open: ``ts``](ts)

---

## ``mt`` — Transfer function container

The ``mt`` structure stores **frequency-domain MT responses** (transfer functions) and their uncertainties, together with derived quantities used for interpretation and visualization.
It is designed to support consistent plotting, QC/editing masks, export (e.g., EDI), and comparison against modeled responses.

Typical use: spectral estimation → regression → QC/editing → export/import → interpretation.

[Open: ``mt``](mt)

---

## ``processing`` — Processing configuration and runtime products

The processing structures organize **how** time series are transformed into transfer functions.
In FFMT, this is commonly expressed through batching containers (``task``) and per-configuration definitions (``job``), plus auxiliary processing parameters (segmentation, overlap, filtering, ranking, robust regression settings).

Typical use: define jobs/tasks → run processing → produce ``mt`` outputs.

[Open: ``processing``](processing)

---

## ``model`` — Resistivity model container

The ``model`` structure represents a **3-D resistivity model** (mesh vectors/grids and physical-property volumes) prepared for visualization and for interfacing with modeling/inversion tools.
It may include padding, masks, and optional topography integration via DEM resampling.

Typical use: build mesh → assign resistivity → add topo (optional) → export/use for forward/inversion.

[Open: ``model``](model)

---

## ``study`` — Synthetic / forward-modeling study container

The ``study`` structure groups modeling outputs in a way that is easy to query by **frequency, polarization, and site**.
It typically links a ``model`` definition with predicted responses stored in an MT-compatible format, enabling systematic comparison between scenarios and against observations.

Typical use: run forward modeling → store synthetics → compare with observed ``mt``.

[Open: ``study``](study)

---

```{toctree}
:maxdepth: 1
:caption: Structure pages

ts
mt
processing
model
study
