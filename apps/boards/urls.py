from django.conf.urls import patterns, url
from apps.boards.views import BoardListView, BoardDetailView, BoardReportView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', BoardDetailView.as_view(), name='board-detail'),
    url(r'^(?P<pk>\d+)/report/$', BoardReportView.as_view(), name='board-report'),
)
