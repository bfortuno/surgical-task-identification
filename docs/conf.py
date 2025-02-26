import os
import sys
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'nbsphinx',        # Enables Jupyter notebook rendering
    'sphinx_rtd_theme'
]

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'nbsphinx',
}
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
