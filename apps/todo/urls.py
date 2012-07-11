from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

from apps.todo.views import *
from apps.todo.models import *


urlpatterns = patterns('apps.todo.views',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/?$', TodoItemUpdateView.as_view(), name='todoitem'),
    url(r'^new/?$', TodoItemCreateView.as_view(), name='newitem'),
)
