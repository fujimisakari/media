# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'module.book.views',
    url(r'^$', 'index', name='book_index'),
    url(r'^detail/(?P<book_id>\d+)/$', 'detail', name='book_detail'),
    url(r'^category/(?P<category_id>\d+)/$', 'category', name='book_category'),
    url(r'^subcategory/(?P<category_id>\d+)/(?P<subcategory_id>\d+)/$', 'subcategory', name='book_subcategory'),
    url(r'^download/(?P<category_id>\d+)/(?P<subcategory_id>\d+)/(?P<book_id>\d+)/(?P<volume>\d+)/$', 'download', name='book_download'),
    url(r'^search/$', 'search', name='book_search'),
)
