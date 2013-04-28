# -*- coding: utf-8 -*-

# Django settings for media project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'media'             # Or path to database file if using sqlite3.
DATABASE_USER = 'fujimo'             # Not used with sqlite3.
DATABASE_PASSWORD = 'fujimo@'         # Not used with sqlite3.
DATABASE_HOST = 'localhost'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = '5432'             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
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

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.join(BASE_DIR, 'templates'), 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
# MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'q2vga9)jy-7d4n0!e^m%3xs@75bvg5+uw@0#gq$$+!vp+rpx7@'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'media.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.formtools',
    'book',
    'top',
    'manage',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'context_processors.common_context',
    'context_processors.book_context',
    'context_processors.movie_context',
    'context_processors.music_context',
    'context_processors.manage_context',
    'context_processors.image_context',
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
# search
HYPER_ESTRAIER_INDEX = os.path.join(BASE_DIR, 'templates/static/media/book/casket/')

# upload
FILE_UPLOAD_MAX_MEMORY_SIZE = u'314572800'
FILE_UPLOAD_TEMP_DIR = os.path.join(BASE_DIR, 'templates/static/media/tmp')

# login
LOGIN_REDIRECT_URL = '/media/'
LOGIN_URL = '/media/login/'
LOGOUT_URL = '/media/logout/'
CHANGE_PASSWD = '/media/change_passwd/'

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
MEDIA_BASE = '/media/'
MEDIA_URL = '/static/'
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
MANAGE_BASE = 'manage/'
MANAGE_TOP = 'manage/top/'
MANAGE_BOOK = 'manage/book/'
MANAGE_MOVIE = 'manage/movie/'
MANAGE_MUSIC = 'manage/music/'
MANAGE_UPLOAD = 'manage/uploader/'
MANAGE_ANALYSIS = 'manage/analysis/'
MANAGE_BOOK_PATH = os.path.join(BASE_DIR, 'templates/static/media/book')
MANAGE_MOVIE_PATH = os.path.join(BASE_DIR, 'templates/static/media/movie')
MANAGE_MUSIC_PATH = os.path.join(BASE_DIR, 'templates/static/media/music')

# image
RECENT_BOOK = '/images/cnavi_tit_book.png'
RECENT_MOVIE = '/images/cnavi_tit_movie.png'
RECENT_MUSIC = '/images/cnavi_tit_music.png'
HEADER_TITLE = '/images/headertit_tit_01.png'
HEADER_TOP1 = '/images/headernavi_ico_top01.png'
HEADER_BOOK1 = '/images/headernavi_ico_book01.png'
HEADER_MOVIE1 = '/images/headernavi_ico_movie01.png'
HEADER_MUSIC1 = '/images/headernavi_ico_music01.png'
HEADER_MANAGE1 = '/images/headernavi_ico_manage01.png'
HEADER_UPLOAD = '/images/headernavi_ico_upload.png'
HEADER_TOP2 = '/images/headernavi_ico_top02.png'
HEADER_BOOK2 = '/images/headernavi_ico_book02.png'
HEADER_MOVIE2 = '/images/headernavi_ico_movie02.png'
HEADER_MUSIC2 = '/images/headernavi_ico_music02.png'
HEADER_MANAGE2 = '/images/headernavi_ico_manage02.png'
NAVI_CATEAGORY = '/images/cnavi_tit_cate.png'
NAVI_MANAGE = '/images/cnavi_tit_manage.png'
NAVI_SUBCATEGORY = '/images/cnavi_tit_scate.png'
NAVI_SEARCH = '/images/cnavi_tit_search.png'
MAIN_ALL_LIST = '/images/cmain_tit_alist.png'
MAIN_WHATNEW = '/images/cmain_tit_whatnew.png'
MAIN_INFO = '/images/cmain_tit_info.png'
MAIN_SEARCH = '/images/cmain_tit_search.png'
MAIN_CATEGORY = '/images/cmain_tit_clist.png'
MAIN_SUBCATEGORY = '/images/cmain_tit_sclist.png'
MAIN_DETAIL = '/images/cmain_tit_dlist.png'
MAIN_PREVIEW = '/images/cmain_tit_prev.png'
MAIN_BACK = '/images/cmain_btn_back.png'
LOGIN_TITLE = '/images/login_tit_01.png'
CHPW_TITLE = '/images/chpw_tit_01.png'
