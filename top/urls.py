from django.conf.urls.defaults import *
from django.conf import settings
from top.views import whatnew_list


urlpatterns = patterns('',
    (r'^$', whatnew_list, {}, 'whatnew'),
)


