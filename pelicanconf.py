#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Elida et Florian'
SITENAME = "Le blog voyage d'Elida et Florian"
SITEURL = ''

PATH = 'content'
PAGE_PATHS = ['pages']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('thibali', 'https://www.thibali.fr'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme and localization
THEME = './theme'
I18N_GETTEXT_LOCALEDIR = './theme/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%A %d %b %Y'
I18N_TEMPLATES_LANG = 'fr_FR'
LOCALE = 'fr_FR'


# logo path, needs to be stored in PATH Setting
LOGO = '/images/logo.svg'

# plugin for images, tags, and more
PLUGIN_PATHS = ['plugins']
PLUGINS = ['liquid_tags.img', 
		       'liquid_tags.figure',
           'liquid_tags.leafletkmlmap', 
           'i18n_subsites', 
           'tipue_search',
           'representative_image',
           'photos',
           'neighbors']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
STATIC_PATHS = ['images', 'maps', 'videos', 'sounds']

# set this to False when debugging plugins
LOAD_CONTENT_CACHE = True

# navigation and content options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False

MENUITEMS = [
  ('Archive', 'archives.html'),
  ('Flux RSS', 'feeds/all.rss.xml')
]

# this generate all main pages from the site, such as the index
DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
]

# photos plugin (for galleries)
# see https://github.com/getpelican/pelican-plugins/tree/master/photos
PHOTO_LIBRARY = 'photo_galleries'
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 80)
PHOTO_SQUARE_THUMB = True
PHOTO_WATERMARK = True
PHOTO_WATERMARK_TEXT = SITENAME
PHOTO_WATERMARK_IMG = ''
PHOTO_EXIF_KEEP = False
PHOTO_EXIF_REMOVE_GPS = True
PHOTO_EXIF_COPYRIGHT = 'CC-BY-NC-ND'
PHOTO_EXIF_AUTOROTATE = True
PHOTO_RESIZE_JOBS = -1