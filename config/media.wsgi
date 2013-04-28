# -*- mode: Python; -*-

import os
import sys

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(ROOT_PATH, '../')

sys.path.append(PROJECT_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
