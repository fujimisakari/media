# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from module.manage.view_book import book_add, book_edit, book_list, book_delete, book_delete_checked, book_search
from module.manage.view_top import whatnew_add, whatnew_edit, whatnew_list, whatnew_delete, whatnew_delete_checked, whatnew_search
from module.manage.view_ajax import get_title_list, get_subcategory_list, get_volume_list, get_writer_list
# from module.manage.view_upload import uploader
from module.manage.view_analysis import analysis

urlpatterns = patterns(
    '',
    url(r'^$', whatnew_add, name='manage_index'),
    url(r'^top/add/$', whatnew_add, name='manage_top_whatnew_add'),
    url(r'^top/search/$', whatnew_search, name='manage_top_whatnew_search'),
    url(r'^top/list/$', whatnew_list, name='manage_top_whatnew_list'),
    url(r'^top/edit/(?P<whatnew_id>\d+)/$', whatnew_edit, name='manage_top_whatnew_edit'),
    url(r'^top/edit/delete/(?P<whatnew_id>\d+)/$', whatnew_delete, name='manage_top_whatnew_delete'),
    url(r'^top/edit/delete_checked/$', whatnew_delete_checked, name='manage_top_whatnew_delete_checked'),
    url(r'^book/add/$', book_add, name='manage_book_add'),
    url(r'^book/add/(?P<set_type>\w+)/$', book_add, name='manage_book_add'),
    url(r'^book/search/(?P<set_type>\w+)/$', book_search, name='manage_book_search'),
    url(r'^book/edit/(?P<set_type>\w+)/$', book_list, name='manage_book_edit_list'),
    url(r'^book/edit/(?P<set_type>\w+)/(?P<edit_id>\d+)/$', book_edit, name='manage_book_edit'),
    url(r'^book/edit/(?P<set_type>\w+)/(?P<del_id>\d+)/delete/$', book_delete, name='manage_book_delete'),
    url(r'^book/edit/(?P<set_type>\w+)/delete_checked/$', book_delete_checked, name='manage_book_delete_checked'),
    url(r'^ajax/book_title/$', get_title_list, name='manage_get_title_list'),
    url(r'^ajax/book_subcategory/$', get_subcategory_list, name='manage_get_subcategory_list'),
    url(r'^ajax/book_volume/$', get_volume_list, name='manage_get_volume_list'),
    url(r'^ajax/book_writer/$', get_writer_list, name='manage_get_writer_list'),
    # url(r'^uploader/(?P<set_type>\w+)/$', uploader, 'manage_upload'),
    url(r'^analysis/$', analysis, name='manage_analysis_book'),
)
