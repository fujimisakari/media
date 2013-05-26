# -*- coding: utf-8 -*-

from settings.private_config import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
AUTO_LOGIN = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# テンプレートで使用
import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# インポートのパスを設定
import sys
sys.path.append(ROOT_PATH + '/module/')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',               # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': DB_NAME,               # Or path to database file if using sqlite3.
        'USER': DB_USER,                 # Not used with sqlite3.
        'PASSWORD': DB_PASS,             # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

import socket
HOSTNAME = socket.gethostname()
if HOSTNAME == PUBLIC_HOSTNAME:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
            'TIMEOUT': 3600 * 24,  # 24h
        },
    }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Tokyo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ja'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# STATIC_URL = '/static/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, '../static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = DJANGO_SECRET_KEY

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'hoge.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(ROOT_PATH, '../templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'south',
    'module.book',
    'module.top',
    'module.manage',
    'module.common',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'module.context_processors.common_context',
    'module.context_processors.book_context',
    'module.context_processors.manage_context',
    'module.context_processors.image_context',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#####################################################################
# csv data
CSV_DATA_PATH = os.path.join(ROOT_PATH, 'data/')

# search
# HYPER_ESTRAIER_INDEX = os.path.join(ROOT_PATH, 'templates/static/media/book/casket/')

# upload
FILE_UPLOAD_MAX_MEMORY_SIZE = u'314572800'
FILE_UPLOAD_TEMP_DIR = os.path.join(ROOT_PATH, 'templates/static/media/tmp')

# login
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
CHANGE_PASSWD = '/change_passwd/'

# paging
LIST_COUNT = 5
NUM_IN_RSS = 8
NUM_IN_LIST_PAGE = 30
NUM_IN_DETAIL_PAGE = 20
NUM_IN_WHATNEW_LIST = 20
NUM_IN_MANAGE_LIST = 50
ALL_LIST_LIMIT = 15

# conmmon
MEDIA_TITLE = "MEDIA SERVER"
MEDIA_BASE = '/'
# MEDIA_URL = '/static/'
MEDIA_DATA = '/static'
MEDIA_CSS = 'css/import.css'
MEDIA_JS = 'js/import.js'
MEDIA_FOTTER = '2011 Fujimo-net.com'

# book
BOOK_BASE = 'book/'
BOOK_DETAIL = 'detail/'
BOOK_SEARCH = 'book/search/'
BOOK_PDF = '_pc.pdf'
BOOK_IPAD = '_ipad.epub'
BOOK_IPHONE = '_iphone.epub'
BOOK_DATA = '_data.zip'
BOOK_THUMBNAIL = '1_thumbnail.jpg'
BOOK_VOLUME_THUMBNAIL = '_thumbnail.jpg'
BOOK_THUMB_HEIGHT = '110'
BOOK_THUMB_WIDTH = '77'

# movie
MOVIE_BASE = 'movie/'

# music
MUSIC_BASE = 'music/'

# manage
MANAGE_BASE = '/'
MANAGE_TOP = 'top/'
MANAGE_BOOK = 'manage/book/'
MANAGE_MOVIE = 'manage/movie/'
MANAGE_MUSIC = 'manage/music/'
MANAGE_UPLOAD = 'manage/uploader/'
MANAGE_ANALYSIS = 'manage/analysis/'
MANAGE_BOOK_PATH = os.path.join(ROOT_PATH, 'templates/static/media/book')
MANAGE_MOVIE_PATH = os.path.join(ROOT_PATH, 'templates/static/media/movie')
MANAGE_MUSIC_PATH = os.path.join(ROOT_PATH, 'templates/static/media/music')

# image
RECENT_BOOK = 'img/cnavi_tit_book.png'
RECENT_MOVIE = 'img/cnavi_tit_movie.png'
RECENT_MUSIC = 'img/cnavi_tit_music.png'
HEADER_TITLE = 'img/headertit_tit_01.png'
HEADER_TOP1 = 'img/headernavi_ico_top01.png'
HEADER_BOOK1 = 'img/headernavi_ico_book01.png'
HEADER_MOVIE1 = 'img/headernavi_ico_movie01.png'
HEADER_MUSIC1 = 'img/headernavi_ico_music01.png'
HEADER_MANAGE1 = 'img/headernavi_ico_manage01.png'
HEADER_UPLOAD = 'mg/headernavi_ico_upload.png'
HEADER_TOP2 = 'img/headernavi_ico_top02.png'
HEADER_BOOK2 = 'img/headernavi_ico_book02.png'
HEADER_MOVIE2 = 'img/headernavi_ico_movie02.png'
HEADER_MUSIC2 = 'img/headernavi_ico_music02.png'
HEADER_MANAGE2 = 'img/headernavi_ico_manage02.png'
NAVI_CATEAGORY = 'img/cnavi_tit_cate.png'
NAVI_MANAGE = 'img/cnavi_tit_manage.png'
NAVI_SUBCATEGORY = 'img/cnavi_tit_scate.png'
NAVI_SEARCH = 'img/cnavi_tit_search.png'
MAIN_ALL_LIST = 'img/cmain_tit_alist.png'
MAIN_WHATNEW = 'img/cmain_tit_whatnew.png'
MAIN_INFO = 'img/cmain_tit_info.png'
MAIN_SEARCH = 'img/cmain_tit_search.png'
MAIN_CATEGORY = 'img/cmain_tit_clist.png'
MAIN_SUBCATEGORY = 'img/cmain_tit_sclist.png'
MAIN_DETAIL = 'img/cmain_tit_dlist.png'
MAIN_PREVIEW = 'img/cmain_tit_prev.png'
MAIN_BACK = 'img/cmain_btn_back.png'
LOGIN_TITLE = 'img/login_tit_01.png'
CHPW_TITLE = 'img/chpw_tit_01.png'
