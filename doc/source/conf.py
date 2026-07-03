# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = 'test-helper-by-delica'
copyright = '2026, Delica Leboe-McGowan'
author = 'Delica Leboe-McGowan'
release = '1.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['autodoc2', "myst_parser",
    'sphinx.ext.napoleon',  # For Google and NumPy style docstrings
    'sphinx.ext.githubpages',]

autodoc2_docstring_parser_regexes = [
    (r".*", "rst"),
]

autodoc_type_aliases = {
    'IOPair.IOPair': 'src.IOPair.IOPair'
}
primary_domain = 'py'

master_doc = "index"

suppress_warnings = ["ref.*"]

napoleon_google_docstring = False
napoleon_numpy_docstring = True

autodoc2_packages = [
    "../../src/IOPair.py",
"../../src/test_helper_funcs.py"
]
#templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
#html_static_path = ['_static']
# html_sidebars = {
#     '**': [
#         'globaltoc.html',
#     ]
# }

