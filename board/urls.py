__author__ = 'scribe'

from django.conf.urls import patterns, url
from board import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView, name='index'),
    url(r'^todo/(?P<pk>\d+)/$', views.InProgressView.as_view(), name ='todo'),
    url(r'^InProgress/(?P<InProgress_id>\d+)/$', views.InProgressView.as_view(), name='InProgress'),
    url(r'^finished/(?P<Finished_id>\d+)/$', views.FinishedView, name='finished'),
)

