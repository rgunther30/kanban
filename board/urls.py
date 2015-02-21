__author__ = 'scribe'

from django.conf.urls import patterns, url
from board import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^todo/(?P<Todo_id>\d+)/$', views.TodoView, name ='todo'),
    url(r'^InProgress/(?P<InProgress_id>\d+)/$', views.InProgressView, name='InProgress'),
    url(r'^finished/(?P<Finished_id>\d+)/$', views.FinishedView, name='finished'),
)

