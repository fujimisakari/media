# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.top.views',
    url(r'^$', 'index', name='top_index'),
)
