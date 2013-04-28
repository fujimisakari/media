# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.conf import settings
from book.views import all_list, category, subcategory, detail, extend_detail, preview, search

urlpatterns = patterns('',
    (r'^$', all_list, {}, 'all_list'),
    (r'^search/$', search, {}, 'search'),
    (r'^(?P<category>\w+)/$', category, {}, 'category'),
    (r'^(?P<category>\w+)/(?P<subcategory>\w+)/$', subcategory, {}, 'subcategory'),
    (r'^(?P<category>\w+)/(?P<subcategory>\w+)/(?P<title>\w+)/$', detail, {}, 'detail'),
    (r'^(?P<category>\w+)/(?P<subcategory>\w+)/(?P<title>\w+)/(?P<volume>\d+)/$', preview, {}, 'preview'),
)
