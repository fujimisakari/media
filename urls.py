from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib.auth.views import login, logout_then_login, password_change, password_change_done

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/', include('top.urls')),
    (r'^media/book/', include('book.urls')),
    # (r'^media/music/', include('music.urls')),
    # (r'^media/movie/', include('movie.urls')),
    (r'^media/manage/', include('manage.urls')),
    (r'^media/login/$', login),
    (r'^media/logout/$', logout_then_login),
    (r'^media/change_passwd/$', password_change, {'post_change_redirect': '/media/change_passwd_done/'}),
    (r'^media/change_passwd_done/$', password_change_done),
    (r'^media/admin/(.*)', admin.site.root),
)

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#    )
