# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.book.views',
    url(r'^$', 'index', name='book_index'),
    url(r'^search/$', 'search', name='book_search'),
    url(r'^detail/(?P<book_id>\d+)/$', 'detail', name='book_detail'),
    url(r'^category/(?P<category_id>\d+)/$', 'category', name='book_category'),
    url(r'^subcategory/(?P<category_id>\d+)/(?P<subcategory_id>\d+)/$', 'subcategory', name='book_subcategory'),
    url(r'^preview/(?P<book_id>\d+)/(?P<volume>\d+)/$', 'preview', name='book_preview'),
)
