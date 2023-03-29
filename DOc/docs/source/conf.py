# Configuration file for the Sphinx documentation builder.
#
root_doc = 'index'
master_doc = 'index'

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = ''
copyright = '2022, Aurelius Atlas Enterprise'
author = 'Americo'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
]

source_suffix = ['.rst', '.md']
templates_path = ['_templates']
exclude_patterns = []

intersphinx_mapping = {
    'sphinx': ('https://github.com/aureliusenterprise/helm-governance/blob/main/README.md', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#alabaster is the other theme
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
html_logo = '_static/logo/logo1.png'
html_favicon = '_static/favicon/fav.png'

#
#html_style = 'theme1.css'

def setup(app): 
    app.add_stylesheet('theme1.css')
