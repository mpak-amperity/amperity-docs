# -*- coding: utf-8 -*-
#
# MARKUP documentation build configuration file.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

sys.path.append(os.path.abspath('../../_ext'))


# might be needed for Canny, if yes, should be here
# import jwt
# 
# canny_private_key = 'bd4601a9-32d6-8632-ac89-cd091e213c0b'
# 
# def create_canny_token(user):
#   user_data = {
#     'avatarURL': user.avatar_url, # optional but preferred
#     'email': user.email,
#     'id': user.id,
#     'name': user.name,
#   }
#   return jwt.encode(user_data, canny_private_key, algorithm='HS256')
# 


# -- General configuration -----------------------------------------------------


# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# 
# Cannot do this just yet:
# extensions = ['sphinx.ext.todo', 'recommonmark']
# because it breaks the search when RST and MD files are in the same location by truncating a SINGLE CHARACTER from the search result link :(
extensions = ['sphinx.ext.todo']

# autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', '../../_templates']

# The suffix of source filenames.
source_suffix = ['.rst']

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'AmpIQ'
#copyright = u''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '0.0.1'
# The full version, including alpha/beta/rc tags.
# release = '0.0.1-1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'friendly'

# highlight_language = 'ruby'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# A string of reStructuredText that will be included at the beginning of every source file that is read.
rst_prolog = """
.. include:: ../../tokens/external_links.txt
.. include:: ../../tokens/images.txt
.. include:: ../../tokens/internal_links.txt
.. include:: ../../tokens/names.txt
"""

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'amperity'
#html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../../_themes/']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "AmpIQ"

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = "../../images/logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "https://amperity-static-assets.s3-us-west-2.amazonaws.com/resources/img/favicon-16x16.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# This setting overrides a version # stamp inserted at the bottom of every
# page. It's just a hack, but it's the hack that achieves the desired behavior.
# html_last_updated_fmt = 'current version of MARKUP documentation'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
   '**': ['localtoc.html'],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#    '404': '/internal/404.html',
html_additional_pages = {
    'channel_active_campaign': 'channel_active_campaign.html',
    'channel_adobe_marketo': 'channel_adobe_marketo.html',
    'channel_amazon_s3': 'channel_amazon_s3.html',
    'channel_attentive_mobile': 'channel_attentive_mobile.html',
    'channel_azure_blob_storage': 'channel_azure_blob_storage.html',
    'channel_braze': 'channel_braze.html',
    'channel_cheetah_digital': 'channel_cheetah_digital.html',
    'channel_cordial': 'channel_cordial.html',
    'channel_criteo': 'channel_criteo.html',
    'channel_facebook_ads': 'channel_facebook_ads.html',
    'channel_google_ads': 'channel_google_ads.html',
    'channel_google_cloud_storage': 'channel_google_cloud_storage.html',
    'channel_google_customer_match': 'channel_google_customer_match.html',
    'channel_hubspot': 'channel_hubspot.html',
    'channel_klaviyo': 'channel_klaviyo.html',
    'channel_listrak': 'channel_listrak.html',
    'channel_microsoft_ads': 'channel_microsoft_ads.html',
    'channel_sailthru': 'channel_sailthru.html',
    'channel_salesforce_marketing_cloud': 'channel_salesforce_marketing_cloud.html',
    'channel_sftp': 'channel_sftp.html',
    'channel_snapchat': 'channel_snapchat.html',
    'channel_tiktok_ads': 'channel_tiktok_ads.html',
    'customer_lifetime_value': 'customer_lifetime_value.html',
    'destination_facebook_ads': 'destination_facebook_ads.html',
}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sourcelink = False

# This is set to "False" because we don't want to show the default copyright, but
# do want to show the custom string defined by the "copyright" general setting (above).

html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.

# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'AmpIQ'


# Edit this page on GitHub link
html_context = {
    "display_github": True, # Integrate GitHub
    "github_path": "https://github.com/amperity/amperity-docs/tree/main/amperity_ampiq/source/", # Path in the checkout to the docs root
}
