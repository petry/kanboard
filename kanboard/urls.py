from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('apps.core.urls')),
    url(r'^boards/', include('apps.boards.urls')),
    url(r'^issues/', include('apps.issues.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
