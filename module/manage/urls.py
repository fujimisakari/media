# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from module.manage.view_book import book_add, book_edit, book_edit_list, book_delete, book_delete_checked, book_search
from module.manage.view_top import top_add, top_edit, top_edit_list, top_delete, top_delete_checked, top_search
from module.manage.view_ajax import getSubcategoryList, getTitleList, getVolumeList, getWriterList
from module.manage.view_upload import uploader
from module.manage.view_analysis import analysis

urlpatterns = patterns(
    '',
    url(r'^$', top_add, 'manage_index'),
    url(r'^top/$', top_add, 'manage_top'),
    url(r'^top/add/$', top_add, 'manage_top_add'),
    url(r'^top/add/(?P<set_type>\w+)/$', top_add, 'manage_top_add'),
    url(r'^top/search/(?P<set_type>\w+)/$', top_search, 'manage_top_search'),
    url(r'^top/edit/(?P<set_type>\w+)/$', top_edit_list, 'manage_top_edit_list'),
    url(r'^top/edit/(?P<set_type>\w+)/(?P<id>\d+)/$', top_edit, 'manage_top_edit'),
    url(r'^top/edit/(?P<set_type>\w+)/(?P<id>\d+)/delete/$', top_delete, 'manage_top_delete'),
    url(r'^top/edit/(?P<set_type>\w+)/delete_checked/$', top_delete_checked, 'manage_top_delete_checked'),
    url(r'^book/$', book_add, 'manage_book_add'),
    url(r'^book/add/$', book_add, 'manage_book_add'),
    url(r'^book/add/(?P<set_type>\w+)/$', book_add, 'manage_book_add'),
    url(r'^book/search/(?P<set_type>\w+)/$', book_search, 'manage_book_search'),
    url(r'^book/edit/(?P<set_type>\w+)/$', book_edit_list, 'manage_book_edit_list'),
    url(r'^book/edit/(?P<set_type>\w+)/(?P<id>\d+)/$', book_edit, 'manage_book_edit'),
    url(r'^book/edit/(?P<set_type>\w+)/(?P<id>\d+)/delete/$', book_delete, 'manage_book_delete'),
    url(r'^book/edit/(?P<set_type>\w+)/delete_checked/$', book_delete_checked, 'manage_book_delete_checked'),
    url(r'^ajax/book_title/$', getTitleList, 'getTitleList'),
    url(r'^ajax/book_subcategory/$', getSubcategoryList, 'getSubcategoryList'),
    url(r'^ajax/book_volume/$', getVolumeList, 'getVolumeList'),
    url(r'^ajax/book_writer/$', getWriterList, 'getWriterList'),
    url(r'^uploader/(?P<set_type>\w+)/$', uploader, 'manage_upload'),
    url(r'^analysis/(?P<set_type>\w+)/$', analysis, 'manage_analysis'),
)
