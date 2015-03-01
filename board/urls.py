__author__ = 'scribe'

from django.conf.urls import patterns, url
from board import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView, name='index'),
    url(r'^task/(?P<key>\d+)/$', views.TaskView, name ='task')
)

