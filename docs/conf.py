# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django
sys.path.insert(0, os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'SkillBuilder.settings'
django.setup()

project = 'SkillBuilder'
copyright = '2023, Jeffrey Kwei Afutu'
author = 'Jeffrey Kwei Afutu'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.imgmath',
    'rst2pdf.pdfbuilder',
]

pdf_documents = [('index', u'SkillBuilder Documentation', u'SKILLBUILDER DOCUMENTATION', u'Jeffrey Kwei Afutu'),]

# LaTeX-related settings
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'preamble': '',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
