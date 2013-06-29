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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
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

    'debug_toolbar',
    'south',
    'module.book',
    'module.top',
    'module.manage',
    'module.common',
)

# debug_toolbar用
INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    #'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    #'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
    # 'HIDE_DJANGO_SQL': False,
    #'TAG': 'div',
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'module.context_processors.common_context',
    'module.context_processors.book_context',
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

# data path
CSV_DATA_PATH = os.path.join(ROOT_PATH, '../data/')
BOOK_DATA_PATH = os.path.join(ROOT_PATH, '../bookshelf/')
THUMBNAIL_DATA_PATH = os.path.join(ROOT_PATH, '../static/img/thumbnail/')

# search
# HYPER_ESTRAIER_INDEX = os.path.join(ROOT_PATH, 'templates/static/media/book/casket/')

# upload
FILE_UPLOAD_MAX_MEMORY_SIZE = u'314572800'
FILE_UPLOAD_TEMP_DIR = os.path.join(ROOT_PATH, 'templates/static/media/tmp')

# paging
LIST_COUNT = 5
NUM_IN_RSS = 8
NUM_IN_LIST_PAGE = 40
NUM_IN_DETAIL_PAGE = 20
NUM_IN_WHATNEW_LIST = 20
NUM_IN_MANAGE_LIST = 50
ALL_LIST_LIMIT = 32

# conmmon
MEDIA_TITLE = "MEDIA SERVER"
MEDIA_CSS = '/css/import.css'
MEDIA_JS = '/js/import.js'
MEDIA_FOTTER = '2011 fujimisakari.com'

# book
BOOK_PDF = '_pc.pdf'
BOOK_IPAD = '_ipad.epub'
BOOK_IPHONE = '_iphone.epub'
BOOK_DATA = '_data.zip'
BOOK_THUMBNAIL = 'thumbnail.jpg'
BOOK_VOLUME_THUMBNAIL = '_thumbnail.jpg'
BOOK_THUMB_HEIGHT = '110'
BOOK_THUMB_WIDTH = '80'

# info type
SUCCESS = 1
ERROR = 2
ATTENTION = 3

# manage msg
MSG_ADD = u'登録しました'
MSG_REGIST = u'登録しました'
MSG_EDIT = u'編集しました'
MSG_DELET = u'削除しました'
MSG_CHECKED_DELET = u'チェック項目を削除しました'
ERROR_MSG_ADD = u'入力値が正常でないため、登録が行えませんでした'
ERROR_MSG_EDIT = u'入力値が正常でないため、編集が行えませんでした'
ERROR_MSG_FILEPATH = u'カテゴリまたはサブカテゴリの組み合わせが正しくありません'
MSG_UPLOAD = u'アップロードしました'
ERROR_MSG_UPLOAD_FILEPATH = u'カテゴリ、サブカテゴリ、タイトルの組み合わせが正しくありません'
ERROR_MSG_UPLOAD = u'入力値が正常でないため、アップロードが行えませんでした'

TITLE_MAP = {'whatnew': u'新着情報',
             'book': u'BOOK',
             'detail': u'BOOK詳細',
             'category': u'カテゴリ',
             'subcategory': u'サブカテゴリ',
             'writer': u'著者',
             'publisher': u'出版社',
             }
