# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'INSPIRE'
copyright = '2024, Jia Zhao'
author = 'Jia Zhao'

release = 'v1.0.0'
version = 'v1.0.0'

# -- General configuration

extensions = [
    'nbsphinx',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

def setup(app):
    app.add_css_file('my_theme.css')

html_static_path = ['_static'] 
