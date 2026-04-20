# ============================================================================
# Sphinx configuration file for the FFMT documentation
# ============================================================================
# This file defines the global behaviour of the documentation build:
# project metadata, enabled extensions, HTML theme, static assets,
# and MyST Markdown parsing options.
# ============================================================================


# ----------------------------------------------------------------------------
# Project information
# ----------------------------------------------------------------------------
# Basic metadata shown in the generated documentation.
project = "FFMT"
author = "Cesar Daniel Castro, Maria Kamila Diaz, Philip Hering, Andreas Junge"
release = "1.0"
language = "en"


# ----------------------------------------------------------------------------
# Sphinx extensions
# ----------------------------------------------------------------------------
# myst_parser      : Enables MyST Markdown support (.md files with directives,
#                    roles, fenced blocks, etc.).
# sphinx_copybutton: Adds a copy button to code blocks.
# sphinx_design    : Adds layout/design components such as cards, grids, tabs,
#                    and other modern UI elements for documentation pages.
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]


# ----------------------------------------------------------------------------
# Template and source exclusions
# ----------------------------------------------------------------------------
# templates_path: Folder containing custom HTML templates, if any.
# exclude_patterns: Files/folders ignored by Sphinx during the build.
templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]


# ----------------------------------------------------------------------------
# Source file suffix mapping
# ----------------------------------------------------------------------------
# IMPORTANT:
# Use a dictionary so Sphinx knows which parser to use for each file type.
# If a plain list is used instead, Sphinx treats all listed files as
# reStructuredText, which can break MyST Markdown directives.
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}


# ----------------------------------------------------------------------------
# HTML theme
# ----------------------------------------------------------------------------
# Theme used for the generated HTML documentation.
html_theme = "sphinx_rtd_theme"

# Title shown in the browser tab and some theme headers.
html_title = "FFMT"

# Theme options for sphinx_rtd_theme.
html_theme_options = {
    "logo_only": True,
    "collapse_navigation": False,
    "navigation_depth": 6,
    "titles_only": False,
    "sticky_navigation": True,
}


# ----------------------------------------------------------------------------
# Static files
# ----------------------------------------------------------------------------
# html_static_path: Folder copied to the build output for custom static assets
# such as CSS, JavaScript, logos, icons, and images.
html_static_path = ["_static"]

# Logo shown in the documentation sidebar/header.
html_logo = "_static/images/general/logo_ffmt.png"

# Browser favicon.
html_favicon = "_static/images/general/logo_ffmt.png"

# Custom CSS file loaded after the theme CSS.
html_css_files = ["custom.css"]


# ----------------------------------------------------------------------------
# MyST configuration
# ----------------------------------------------------------------------------
# Optional MyST syntax extensions used throughout the Markdown documentation.
myst_enable_extensions = [
    "colon_fence",  # Allows ::: fenced directives in addition to ``` fences.
    "deflist",      # Enables definition lists.
    "fieldlist",    # Enables field lists.
    "tasklist",     # Enables GitHub-style task lists.
    "html_image",   # Converts isolated raw <img> tags into Sphinx image nodes.
    "attrs_inline", # Enables inline attribute syntax like {#id .class}.
]
