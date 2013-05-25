# -*- coding: utf-8 -*-

import socket
from settings.base_settings import *

HOSTNAME = socket.gethostname()

# 本番サーバーのdevではoauth認証を行うようにする
DEBUG = True
TEMPLATE_DEBUG = DEBUG
AUTO_LOGIN = DEBUG

# 本番環境以外ではmemcachedは使用しない
CACHES = {}


#==================================================
# DB設定(本番サーバー内でのdev環境用)
#==================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': '',
        'PORT': '',
    }
}


#==================================================
# media設定
#==================================================

# import os
# # ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
# # MEDIA_ROOT = os.path.join(ROOT_PATH, '../static')
# # MEDIA_URL = '/static'

# MEDIA_CSS = '/static/css/import.css'
# MEDIA_JS = '/static/js/import.js'
# MEDIA_IMG = '/static/img'
