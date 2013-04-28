# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    'top.views',
    url(r'^$', 'whatnew_list', name='top_whatnew'),
)
