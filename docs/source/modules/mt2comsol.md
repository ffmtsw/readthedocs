MT2COMSOL is the graphical entry point for preparing topography/bathymetry-based
COMSOL inputs, managing the COMSOL + LiveLink connection from MATLAB, and
launching MT-response extraction workflows.

It is designed to guide the user through a practical sequence:

* define the frequency range and estimate skin depth,
* define the model reference coordinates and spatial extents,
* compute geographic limits,
* download or inspect a DEM,
* generate COMSOL input files,
* start a COMSOL session, and
* extract MT responses from an ``.mph`` model.

The overall structure of this page follows the same user-oriented module style
used in the existing FFMT documentation for modules such as ReadTS and nEMesis.

* * *

.. figure:: ../_static/images/mt2comsol/mt2comsol_gui.png
   :width: 100%
   :align: center
   :alt: MT2COMSOL main GUI

   Main GUI of ``MT2COMSOL``.

* * *

Main features
-------------

1) DEM and model-domain setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The upper half of the GUI is dedicated to defining the physical and spatial
context of the model domain. From here, the user can:

* define the frequency range of interest,
* estimate minimum and maximum skin depth from a reference resistivity,
* define a geographic reference center,
* define Cartesian model extents in kilometers,
* compute the corresponding geographic limits, and
* configure DEM download options.

This section is meant to help the user build a domain that is consistent with
both the MT target depth range and the intended COMSOL model size.

2) DEM download and quick visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MT2COMSOL provides two ways to interact with terrain data:

* open the GMRT website manually for DEM download, and
* download the DEM directly from the GUI using the computed geographic limits.

A quick plotting utility is also available to inspect an existing DEM or
GeoTIFF before generating the COMSOL input files.

3) COMSOL input-file generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The GUI can launch the input-file preparation workflow used to build the ASCII
files required by the COMSOL model setup. This includes topography,
conductance/thin-layer information, station coordinates, and optional coastline
support files.

4) COMSOL connection control
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

MT2COMSOL checks whether COMSOL Server and LiveLink for MATLAB are available,
and provides a switch to start or stop the COMSOL session from inside the GUI.
The connection state is reflected by status lamps and by enabling/disabling the
controls that depend on an active COMSOL session.

5) MT response extraction
^^^^^^^^^^^^^^^^^^^^^^^^^

Once a COMSOL session is active, the GUI enables the response-extraction step.
This allows the user to select an ``.mph`` file and launch the workflow that
retrieves magnetotelluric responses from the COMSOL model.

* * *

Main GUI components
-------------------

The MT2COMSOL interface is divided into two main blocks:

* ``DEM and Model Domain Setup``
* ``Modeling Workflow``

DEM and Model Domain Setup
^^^^^^^^^^^^^^^^^^^^^^^^^^

Frequency and Skin Depth
~~~~~~~~~~~~~~~~~~~~~~~~

* ``Max. Frequency [Hz]`` (numeric field): Highest MT frequency used to estimate
  the shallowest skin depth.

* ``Min. Frequency [Hz]`` (numeric field): Lowest MT frequency used to estimate
  the deepest skin depth.

* ``Resistivity [Ohm m]`` (numeric field): Reference resistivity used for the
  skin-depth estimate.

* ``Skin depth min [km]`` (read-only): Estimated minimum skin depth associated
  with the highest frequency.

* ``Skin depth max [km]`` (read-only): Estimated maximum skin depth associated
  with the lowest frequency.

The skin-depth values are updated automatically whenever the frequency range or
reference resistivity changes.

Reference Coordinates
~~~~~~~~~~~~~~~~~~~~~

* ``Central Latitude [deg]`` (numeric field): Reference latitude of the model
  center.

* ``Central Longitude [deg]`` (numeric field): Reference longitude of the model
  center.

* ``Use Center from MT Structure`` (button): Loads an ``mt`` structure from a
  ``.mat`` file and uses its center as the domain reference coordinates.

This is useful when the COMSOL model should be centered directly on an existing
MT survey.

Domain Extents
~~~~~~~~~~~~~~

* ``Easting min. [km]`` (numeric field): Minimum x extent relative to the
  reference center.

* ``Easting max. [km]`` (numeric field): Maximum x extent relative to the
  reference center.

* ``Northing min. [km]`` (numeric field): Minimum y extent relative to the
  reference center.

* ``Northing max. [km]`` (numeric field): Maximum y extent relative to the
  reference center.

* ``Calculate Limits`` (button): Converts the Cartesian domain extents into
  geographic limits and computes the total area.

Geographic Limits
~~~~~~~~~~~~~~~~~

* ``Latitude min. [deg]`` (read-only): Southern geographic limit.

* ``Latitude max. [deg]`` (read-only): Northern geographic limit.

* ``Longitude min. [deg]`` (read-only): Western geographic limit.

* ``Longitude max. [deg]`` (read-only): Eastern geographic limit.

* ``Area [km2]`` (read-only): Estimated model area based on the selected x/y
  limits.

These values are computed from the reference coordinates and the Cartesian
model extents.

DEM Download Settings
~~~~~~~~~~~~~~~~~~~~~

* ``Format`` (drop-down): DEM output format requested from GMRT.

* ``Resolution`` (drop-down): DEM sampling resolution.

* ``Plot DEM`` (checkbox): If enabled, plots the DEM after download.

* ``Select Folder`` (button): Defines the destination folder for downloaded DEM
  files and generated outputs.

* ``Folder`` (read-only text field): Displays the currently selected output
  folder.

* ``Download DEM`` (button): Downloads the DEM for the computed geographic
  limits using the selected format and resolution.

* ``Open Folder`` (button): Opens the selected destination folder in the system
  file explorer.

Modeling Workflow
^^^^^^^^^^^^^^^^^

Installation
~~~~~~~~~~~~

This panel reports whether COMSOL and LiveLink for MATLAB were detected.
Depending on the environment, the panel shows either:

* a positive installation message, or
* a warning indicating that COMSOL, LiveLink, or both were not detected.

DEM
~~~

* ``Download DEM`` (button): Opens the GMRT website in the browser for manual
  DEM download.

* ``Plot DEM`` (button): Launches a quick DEM plotting utility.

This panel is useful when the user wants to inspect terrain data before
starting the COMSOL input-file workflow.

Model Input Files
~~~~~~~~~~~~~~~~~

* ``Create Input Files`` (button): Launches the topography/thin-layer workflow
  that generates the COMSOL support files.

This is the main entry point for preparing the ASCII files required by the
model setup.

COMSOL Connection
~~~~~~~~~~~~~~~~~

* ``Start COMSOL Session`` (switch): Starts or resets the COMSOL session from
  inside MATLAB.

* Left lamp: OFF / inactive session state.

* Right lamp: ON / active COMSOL connection state.

When the session is active, controls that depend on COMSOL become available.

Results
~~~~~~~

* ``Extract MT responses`` (label): Indicates the final workflow stage.

* ``Select MPH File`` (button): Selects a COMSOL ``.mph`` model and launches
  MT response extraction.

This button is disabled until a valid COMSOL session is active.

Menu entries
^^^^^^^^^^^^

Tools
~~~~~

* ``Anisotropy Calculator``: Opens the MT2COMSOL anisotropy calculator.

Extras
~~~~~~

* ``Documentation``: Opens the MT2COMSOL documentation page in the browser.

* * *

DEM and model-domain workflow
-----------------------------

Frequency range and skin-depth estimate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start by defining the maximum frequency, minimum frequency, and a reference
resistivity. MT2COMSOL uses these values to compute a first-order estimate of
how shallow and how deep the model should remain meaningful for the intended MT
response range.

This estimate does not replace a full sensitivity analysis, but it is a useful
practical guide when choosing the vertical and lateral domain size.

Reference center
^^^^^^^^^^^^^^^^

Next, define the geographic center of the model. This can be done either:

* manually, by typing latitude and longitude, or
* automatically, by loading an ``mt`` structure and using its center.

Using the survey center is recommended when the COMSOL model is meant to be
aligned with an existing MT array.

Cartesian model extents
^^^^^^^^^^^^^^^^^^^^^^^

Enter the x and y domain limits in kilometers relative to the selected
reference center. These values define the lateral size of the model in local
Cartesian coordinates.

Once the extents are defined, click ``Calculate Limits`` to obtain the
corresponding latitude/longitude window and the total model area.

DEM download settings
^^^^^^^^^^^^^^^^^^^^^

After the geographic limits are available, define the DEM format, sampling
resolution, destination folder, and whether the DEM should be plotted
immediately after download.

At this stage, the GUI is ready to retrieve terrain data directly from GMRT or
use an already available DEM in a later workflow.

* * *

COMSOL workflow
---------------

Installation check
^^^^^^^^^^^^^^^^^^

When the GUI starts, MT2COMSOL checks whether the required COMSOL components
can be detected:

* COMSOL Server executable
* LiveLink for MATLAB

This status is reported in the ``Installation`` panel.

Start COMSOL session
^^^^^^^^^^^^^^^^^^^^

Use the session switch in the ``COMSOL Connection`` panel to start the COMSOL
server and connect MATLAB through LiveLink. If the connection is successful,
MT2COMSOL updates the status lamps and enables the response-extraction button.

If the session is turned off from the GUI, the interface is reset visually.
Depending on the system state, an external COMSOL server process may still need
to be closed manually.

Extract MT responses
^^^^^^^^^^^^^^^^^^^^

After the COMSOL session is active, click ``Select MPH File`` in the
``Results`` panel to choose the COMSOL model file and launch the MT-response
extraction workflow.

This is the final stage of the main GUI workflow.

* * *

Quick start (step-by-step tutorials)
------------------------------------

Tutorial 1 — Define the frequency range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open ``MT2COMSOL``.
2. In ``Frequency and Skin Depth``, enter:

   * ``Max. Frequency [Hz]``
   * ``Min. Frequency [Hz]``
   * ``Resistivity [Ohm m]``

3. Verify that ``Skin depth min [km]`` and ``Skin depth max [km]`` update
   correctly.
4. Use these values as a first guide for the intended model depth range.

Tutorial 2 — Define the model center
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. In ``Reference Coordinates``, either type the central latitude/longitude
   manually or click ``Use Center from MT Structure``.
2. If using an MT structure, select a ``.mat`` file containing the variable
   ``mt``.
3. Verify that the center coordinates are updated in the GUI.

Tutorial 3 — Define domain extents and compute geographic limits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. In ``Domain Extents``, enter:

   * ``Easting min. [km]``
   * ``Easting max. [km]``
   * ``Northing min. [km]``
   * ``Northing max. [km]``

2. Click ``Calculate Limits``.
3. Verify the resulting values in ``Geographic Limits``.
4. Check the estimated total area.

Tutorial 4 — Download a DEM from the GUI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. In ``DEM Download Settings``, choose the output format and resolution.
2. Click ``Select Folder`` and choose a destination directory.
3. Optionally enable ``Plot DEM``.
4. Click ``Download DEM``.
5. Inspect the downloaded files in the selected folder.

Tutorial 5 — Create COMSOL input files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Make sure a valid output folder is selected.
2. Click ``Create Input Files``.
3. Follow the dialogs used by the input-file workflow.
4. Inspect the generated ASCII support files in the project folder.

A dedicated tutorial for this workflow is provided separately in the
MT2COMSOL documentation because it includes multiple options such as DEM
source selection, station generation, coastline extraction, thin-layer
construction, and optional sediment conductance.

Tutorial 6 — Start COMSOL and connect MATLAB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Check the ``Installation`` panel.
2. In ``COMSOL Connection``, switch ``Start COMSOL Session`` to ON.
3. Wait for the GUI to finish launching the COMSOL server and LiveLink.
4. Confirm that the ON lamp becomes active.

Tutorial 7 — Extract MT responses from an MPH file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Start a valid COMSOL session.
2. In ``Results``, click ``Select MPH File``.
3. Choose the target ``.mph`` file.
4. Follow the extraction workflow.

* * *

Troubleshooting
---------------

COMSOL or LiveLink was not detected
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the ``Installation`` panel reports missing components, verify that:

* COMSOL is installed,
* the COMSOL server executable is available on the MATLAB path or can be
  detected by the environment, and
* LiveLink for MATLAB is installed and visible to MATLAB.

Cannot start COMSOL session
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the session switch fails to start the connection:

1. verify that the detected COMSOL installation includes both Server and
   LiveLink,
2. check whether another session is already connected,
3. confirm that the COMSOL server executable can be launched from the system,
4. restart MATLAB and try again.

``Select MPH File`` is disabled
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This button is enabled only when the COMSOL session is active. Start a valid
COMSOL session first.

DEM download fails
^^^^^^^^^^^^^^^^^^

Check the following:

* the geographic limits were computed correctly,
* latitude min is smaller than latitude max,
* longitude min is smaller than longitude max,
* the selected output folder exists.

Cannot create input files
^^^^^^^^^^^^^^^^^^^^^^^^^

Make sure that:

* a valid project/output folder is selected,
* the DEM source is available,
* the input-file workflow completes without cancellation,
* all required auxiliary files are accessible.

No valid destination folder
^^^^^^^^^^^^^^^^^^^^^^^^^^^

If MT2COMSOL reports an invalid destination folder:

1. click ``Select Folder``,
2. choose an existing directory,
3. verify that the path appears in the folder field,
4. try the action again.

* * *

Related pages
-------------

* ``MT2COMSOL DEM workflow``
* ``MT2COMSOL input-file tutorial``
* ``MT2COMSOL anisotropy calculator``
* ``MT2COMSOL response extraction``
