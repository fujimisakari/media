# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.book.views',
    url(r'^$', 'all_list', name='book_all_list'),
    url(r'^search/$', 'search', name='book_search'),
    url(r'^(?P<category>\w+)/$', 'category', name='book_category'),
    url(r'^(?P<category>\w+)/(?P<subcategory>\w+)/$', 'subcategory', name='book_subcategory'),
    url(r'^(?P<category>\w+)/(?P<subcategory>\w+)/(?P<title>\w+)/$', 'detail', name='book_detail'),
    url(r'^(?P<category>\w+)/(?P<subcategory>\w+)/(?P<title>\w+)/(?P<volume>\d+)/$', 'preview', name='book_preview'),
)
