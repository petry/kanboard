from django.conf.urls import patterns, url
from apps.core.views import BoardDetailView, StoryDetailView

urlpatterns = patterns('',
    #...
    url(r'^boards/(?P<pk>\d+)/$', BoardDetailView.as_view(), name='board-detail'),
    url(r'^story/(?P<pk>\d+)/$', StoryDetailView.as_view(), name='story-detail'),
)