from django.conf.urls import patterns, url
from apps.core.views import BoardDetailView, StoryDetailView, BoardListView

urlpatterns = patterns('',
    url(r'^$', BoardListView.as_view(), name='board-list'),
    url(r'^boards/(?P<pk>\d+)/$', BoardDetailView.as_view(), name='board-detail'),
    url(r'^story/(?P<pk>\d+)/$', StoryDetailView.as_view(), name='story-detail'),
    url(r'^story/(?P<pk>\d+)/advance/$', StoryDetailView.as_view(), name='story-advance'),
)