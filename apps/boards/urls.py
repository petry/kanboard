from django.conf.urls import patterns, url
from apps.boards.views import BoardDetailView, BoardReportView, BoardListView

urlpatterns = patterns('',
    url(r'^$', BoardListView.as_view(), name='board-list'),
    url(r'^(?P<pk>\d+)/$', BoardDetailView.as_view(), name='board-detail'),
    url(r'^(?P<pk>\d+)/report/$', BoardReportView.as_view(), name='board-report'),
)
