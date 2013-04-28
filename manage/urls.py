# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.conf import settings
from manage.view_book import book_add, book_edit, book_edit_list, book_delete, book_delete_checked, book_search
from manage.view_top import top_add, top_edit, top_edit_list, top_delete, top_delete_checked, top_search
from manage.view_ajax import getSubcategoryList, getTitleList, getVolumeList, getWriterList
from manage.view_upload import uploader
from manage.view_analysis import analysis

urlpatterns = patterns('',
    (r'^$', top_add, {}, 'top'),
    (r'^top/$', top_add, {}, 'top'),
    (r'^top/add/$', top_add, {}, 'top_add'),
    (r'^top/add/(?P<set_type>\w+)/$', top_add, {}, 'top_add'),
    (r'^top/search/(?P<set_type>\w+)/$', top_search, {}, 'top_search'),
    (r'^top/edit/(?P<set_type>\w+)/$', top_edit_list, {}, 'top_edit_list'),
    (r'^top/edit/(?P<set_type>\w+)/(?P<id>\d+)/$', top_edit, {}, 'top_edit'),
    (r'^top/edit/(?P<set_type>\w+)/(?P<id>\d+)/delete/$', top_delete, {}, 'top_delete'),
    (r'^top/edit/(?P<set_type>\w+)/delete_checked/$', top_delete_checked, {}, 'top_delete_checked'),
    (r'^book/$', book_add, {}, 'book_add'),
    (r'^book/add/$', book_add, {}, 'book_add'),
    (r'^book/add/(?P<set_type>\w+)/$', book_add, {}, 'book_add'),
    (r'^book/search/(?P<set_type>\w+)/$', book_search, {}, 'book_search'),
    (r'^book/edit/(?P<set_type>\w+)/$', book_edit_list, {}, 'book_edit_list'),
    (r'^book/edit/(?P<set_type>\w+)/(?P<id>\d+)/$', book_edit, {}, 'book_edit'),
    (r'^book/edit/(?P<set_type>\w+)/(?P<id>\d+)/delete/$', book_delete, {}, 'book_delete'),
    (r'^book/edit/(?P<set_type>\w+)/delete_checked/$', book_delete_checked, {}, 'book_delete_checked'),
    (r'^ajax/book_title/$', getTitleList, {}, 'getTitleList'),
    (r'^ajax/book_subcategory/$', getSubcategoryList, {}, 'getSubcategoryList'),
    (r'^ajax/book_volume/$', getVolumeList, {}, 'getVolumeList'),
    (r'^ajax/book_writer/$', getWriterList, {}, 'getWriterList'),
    (r'^uploader/(?P<set_type>\w+)/$', uploader, {}, 'upload'),
    (r'^analysis/(?P<set_type>\w+)/$', analysis, {}, 'analysis'),
)
