from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^board/', include('board.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
