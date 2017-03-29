from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
	url(r'^$', lecture_list, name='list'),
    url(r'^create/$', lecture_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', lecture_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', lecture_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', lecture_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]