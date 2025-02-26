# Configuration file for the Sphinx documentation builder.

import os
import sys
import sphinx_rtd_theme

# -- Project Information -----------------------------------------------------

project = 'Surgical Task Identification'
copyright = '2025, Benjamin Fortuno'
author = 'Benjamin Fortuno'

# The full version, including alpha/beta/rc tags
release = 'v1.0'

# -- General Configuration ---------------------------------------------------

# Add extensions for Jupyter notebook rendering and MathJax support
extensions = [
    'nbsphinx',                      # Enables rendering Jupyter notebooks
    'sphinx.ext.mathjax',            # MathJax for LaTeX-style equations
    'sphinx_rtd_theme',              # ReadTheDocs theme
    # 'sphinx_gallery.load_style'       # Loads CSS for notebook galleries
]

# Paths to ignore (avoid processing temporary files)
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'notebooks/*_empty.ipynb']

# Templates path (optional)
templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------

# Set theme to ReadTheDocs style
html_theme = 'sphinx_rtd_theme'

# Path for static files (CSS, images)
html_static_path = ['_static']

# Specify master document
master_doc = 'index'

# Code highlighting settings
highlight_language = 'python3'

# -- Jupyter Notebook Execution Configuration --------------------------------

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]

# Disable execution of notebooks on build (set to 'always' if needed)
nbsphinx_execute = 'never'

# Add Google Colab Badge to notebooks
nbsphinx_prolog = r"""
.. raw:: html

   <div class="admonition note">
       <p><strong>Open in Google Colab:</strong></p>
       <p><a href="https://colab.research.google.com/github/YOUR_GITHUB_USERNAME/surgical-task-identification/blob/main/{{ env.docname }}.ipynb">
       <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
       </a></p>
   </div>
"""

# Enable table of contents in sidebar
html_sidebars = {
    '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']
}

# Allow larger Jupyter cell outputs in documentation
nbsphinx_allow_errors = True
