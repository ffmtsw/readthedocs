# `model` — Resistivity model structure

The `model` structure is the standard FFMT container for **3-D resistivity models** used in model building, visualization, forward modeling, and inversion workflows (e.g., ModEM grids).
It stores both the **model geometry** (mesh vectors and 3-D grids) and the **physical property volumes**
(resistivity and masks), with optional support for **topography/DEM integration**.

This page describes the expected design of `model` as used throughout FFMT.

---

## How `model` is created

`model` is initialized using:

```matlab
model = allocate_model();
```

After allocation, the geometry and property volumes are typically populated by dedicated tools
(e.g., mesh builders, importers, GUI workflows), for example:

- mesh construction and padding (inner mesh + padding cells),
- assignment of background resistivity and anomalies,
- optional integration of topography from a DEM,
- export to modeling/inversion formats.

---

## What `model` represents

A single `model` instance represents a **rectilinear 3-D grid** defined by node vectors in X/Y/Z:

- `model.x_vect`, `model.y_vect`, `model.z_vect` define the **mesh nodes** (cell boundaries),
- `model.X`, `model.Y`, `model.Z` are 3-D `ndgrid` arrays derived from these vectors,
- `model.x_c`, `model.y_c`, `model.z_c` are **cell centers** for plotting and mapping,
- `model.V` is the main **resistivity volume** (most commonly stored as `log10(rho)`),
- `model.F` is a boolean mask/flag volume used by model-building and editing routines,
- optional topography fields enable consistent air/ground masking and export.

---

## Core geometry fields

### Node vectors (cell boundaries)

- `model.x_vect` : X nodes (km)
- `model.y_vect` : Y nodes (km)
- `model.z_vect` : Z nodes (km), negative downward

These vectors usually include both the **inner mesh** and **padding** extensions.

### 3-D grids

- `model.X`, `model.Y`, `model.Z` : 3-D grids created via `ndgrid(y_vect, x_vect, z_vect)`

> Note: many FFMT model tools follow the convention:
> `ndgrid(Y, X, Z)` so that array dimensions map as:
> `size(model.V) = [ny, nx, nz]`.

### Cell centers

- `model.x_c` : X cell centers (km)
- `model.y_c` : Y cell centers (km)
- `model.z_c` : Z cell centers (km)

Computed as midpoints of consecutive nodes:

```matlab
model.x_c = (model.x_vect(1:end-1) + model.x_vect(2:end))/2;
model.y_c = (model.y_vect(1:end-1) + model.y_vect(2:end))/2;
model.z_c = (model.z_vect(1:end-1) + model.z_vect(2:end))/2;
```

---

## Physical property volumes

### Resistivity volume

- `model.V` : resistivity volume (`log10(rho)`)

Typical initialization patterns:

- uniform background: `model.V = ones(size(model.X))*log10(bgrho);`
- imported model: `model.V` filled from interpolated/imported values

### Flags / masks

- `model.F` : logical mask the same size as `model.V` (e.g., marking edited/fixed cells)
- `model.C` : covariance mask (e.g., used for ModEM models)

Common default:

```matlab
model.F = false(size(model.V));
```

---

## Data/source bookkeeping

Many workflows track the origin of a model:

- `model.source` : string tag indicating where the model came from (e.g., `"MAT"`, `"ModEM"`)
- `model.data`   : logical flag indicating whether the model is being loaded from data (vs created from scratch)

This enables consistent handling of:
- models built inside FFMT,
- models imported from third-party tools,
- models built from auxiliary grids (e.g., special-purpose parameterizations).

---

## Topography and DEM integration

FFMT supports optional inclusion of topography by discretizing a DEM into extra thin layers near the surface.

Typical fields used in topography workflows:

### Topography flags and cached products
- `model.topo`   : logical flag indicating whether topography is active
- `model.Ztopo`  : 3-D grid containing the thin-layer Z discretization used to represent topography
- `model.LRdem`  : low-resolution DEM resampled/interpolated onto the model X/Y grid (km)
- `model.dem`    : original DEM values (high resolution), usually stored in km
- `model.xdem`, `model.ydem` : DEM coordinate vectors or grids used for reconstruction/plotting
- `model.zdem`   : cached reference value (e.g., maximum DEM elevation)

### Conventions
- DEM data are often converted to km (e.g., dividing meters by 1000).
- Thin layers are created with constant thickness (commonly `info.zsize(end)` in the mesh settings).
- After topography insertion, `model.z_vect` and the 3-D grids are updated to include the new layers.

---

## Coordinate conventions

While the exact convention can vary per dataset, FFMT model workflows typically follow:

- X/Y in **kilometers** relative to a chosen center (dataset-dependent),
- Z in **kilometers**, with negative values downward (subsurface),
- vectors represent **nodes** (cell boundaries), and derived `_c` fields represent cell centers.

If station coordinates are rotated (e.g., to match a modeling coordinate system), site coordinates are typically
rotated consistently using the same reference and angle used to build the mesh.

---

## Minimal example (conceptual)

```matlab
model = allocate_model();

% Geometry (example nodes, km)
model.x_vect = (-10:1:10).';
model.y_vect = (-10:1:10).';
model.z_vect = (0:-0.5:-20).';

% Create grids (FFMT convention: ndgrid(y, x, z))
[model.Y, model.X, model.Z] = ndgrid(model.y_vect, model.x_vect, model.z_vect);

% Cell centers
model.x_c = (model.x_vect(1:end-1) + model.x_vect(2:end))/2;
model.y_c = (model.y_vect(1:end-1) + model.y_vect(2:end))/2;
model.z_c = (model.z_vect(1:end-1) + model.z_vect(2:end))/2;

% Background resistivity (log10 Ohm·m)
bgrho = 100; % Ohm·m
model.V = ones(size(model.X)) * log10(bgrho);
model.F = false(size(model.V));

% Source bookkeeping
model.source = "MAT";
model.data   = false;
model.topo   = false;
```

---

## See also

- [`ts`](ts) — time series structure (raw recordings)
- [`mt`](mt) — transfer function structure (frequency-domain responses)
- [`study`](study) — modeling study structure (synthetics and scenario management)

