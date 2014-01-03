from django.conf.urls import patterns, url
from apps.core.views import BoardDetailView

urlpatterns = patterns('',
    #...
    url(r'^boards/(?P<pk>\d+)/$', BoardDetailView.as_view(), name='board-detail'),
)