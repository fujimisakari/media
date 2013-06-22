# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from module.manage.view_book import book_index, book_regist, book_edit, book_delete, book_delete_checked, book_search
from module.manage.view_top import whatnew_index, whatnew_edit, whatnew_delete, whatnew_delete_checked, whatnew_search, whatnew_regist
from module.manage.view_ajax import get_title_list, get_subcategory_list, get_volume_list, get_writer_list, get_publisher_list
# from module.manage.view_upload import uploader
from module.manage.view_status import status

urlpatterns = patterns(
    '',
    url(r'^$', whatnew_index, name='manage_index'),
    url(r'^top/$', whatnew_index, name='manage_top_index'),
    url(r'^top/regist/$', whatnew_regist, name='manage_top_regist'),
    url(r'^top/edit/(?P<whatnew_id>\d+)/$', whatnew_edit, name='manage_top_edit'),
    url(r'^top/delete/(?P<whatnew_id>\d+)/$', whatnew_delete, name='manage_top_delete'),
    url(r'^top/delete_checked/$', whatnew_delete_checked, name='manage_top_delete_checked'),
    url(r'^top/search/$', whatnew_search, name='manage_top_search'),

    url(r'^book/(?P<set_type>\w+)/$', book_index, name='manage_book_index'),
    url(r'^book/regist/(?P<set_type>\w+)/$', book_regist, name='manage_book_regist'),
    url(r'^book/edit/(?P<set_type>\w+)/(?P<edit_id>\d+)/$', book_edit, name='manage_book_edit'),
    url(r'^book/delete/(?P<set_type>\w+)/(?P<del_id>\d+)/$', book_delete, name='manage_book_delete'),
    url(r'^book/delete_checked/(?P<set_type>\w+)/$', book_delete_checked, name='manage_book_delete_checked'),
    url(r'^book/search/(?P<set_type>\w+)/$', book_search, name='manage_book_search'),

    # url(r'^uploader/(?P<set_type>\w+)/$', uploader, 'manage_upload'),
    url(r'^status/$', status, name='manage_book_status'),

    url(r'^ajax/book_title/$', get_title_list, name='manage_get_title_list'),
    url(r'^ajax/book_subcategory/$', get_subcategory_list, name='manage_get_subcategory_list'),
    url(r'^ajax/book_volume/$', get_volume_list, name='manage_get_volume_list'),
    url(r'^ajax/book_writer/$', get_writer_list, name='manage_get_writer_list'),
    url(r'^ajax/book_publisher/$', get_publisher_list, name='manage_get_publisher_list'),
)
