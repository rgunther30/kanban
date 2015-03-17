__author__ = 'scribe'

from django.conf.urls import patterns, url
from board import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView, name='index'),
    url(r'^add/$', views.AddTaskView, name='add'),
    url(r'^addcomment/$', views.AddCommentView, name='addcomment'),
    url(r'^edit/$', views.EditTaskView, name='edit'),
    url(r'^login/$','django.contrib.auth.views.login', {'template_name': 'board/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'board/logout.html'}, name='logout'),
    url(r'^profile/$', views.ProfileView, name='profile'),
    url(r'^about/$', views.AboutView, name='about'),
    url(r'^task/(?P<key>\d+)/$', views.TaskView, name ='task')
)

