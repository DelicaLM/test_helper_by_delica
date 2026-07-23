# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import test_helper_by_delica

project = 'test-helper-by-delica'
copyright = '2026, Delica Leboe-McGowan'
author = 'Delica Leboe-McGowan'
release = test_helper_by_delica.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
#

extensions = ['autodoc2',
    'myst_parser',
    'sphinx.ext.napoleon',  # For Google and NumPy style docstrings
    'sphinx.ext.githubpages',]

autodoc2_docstring_parser_regexes = [
    (r".*", "rst"),
]

autodoc_type_aliases = {
    'IOPair.IOPair': 'test_helper_by_delica.IOPair.IOPair'
}
primary_domain = 'py'

master_doc = "index"

suppress_warnings = ["ref.*"]

napoleon_google_docstring = False
napoleon_numpy_docstring = True

autodoc2_packages = [
    "../../test_helper_by_delica/IOPair.py",
"../../test_helper_by_delica/test_helper_funcs.py",
    "../../examples/bool_function_examples.py",
"../../examples/int_function_examples.py",
"../../examples/list_function_examples.py",
"../../examples/string_function_examples.py",
"../../examples/object_function_examples.py",
"../../tests/test_test_helper_funcs.py"
]
#templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_theme_options = {
    "sidebarwidth": "350",
}
# html_theme_options = {
#     'sidebarwidth': '350px',
# }

#html_static_path = ['_static']
# html_sidebars = {
#     '**': [
#         'globaltoc.html',
#     ]
# }

