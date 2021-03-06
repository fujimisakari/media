# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('module.top.urls')),
    url(r'^book/', include('module.book.urls')),
    url(r'^manage/', include('module.manage.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', kwargs={'template_name': 'root/login.html', 'extra_context': {'is_login_page': True}}, name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='auth_logout'),
    url(r'^change_passwd/$', 'django.contrib.auth.views.password_change', kwargs={'template_name': 'root/password_change_form.html', 'extra_context': {'is_passward_page': True}}, name='auth_password_change'),
    url(r'^change_passwd_done/$', 'django.contrib.auth.views.password_change_done', kwargs={'template_name': 'root/password_change_done.html', 'extra_context': {'is_passward_page': True}}, name='auth_password_change_done'),
    url(r'^admin/', include(admin.site.urls)),
)
