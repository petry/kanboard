from django.conf.urls import patterns, url
from apps.core.views import BoardDetailView, BoardListView, BoardReportView
from apps.issues.views import IssueDetailView, IssueAdvanceView, IssueOnBoardView

urlpatterns = patterns('',
    url(r'^$', BoardListView.as_view(), name='board-list'),
    url(r'^board/(?P<pk>\d+)/$', BoardDetailView.as_view(), name='board-detail'),
    url(r'^board/(?P<pk>\d+)/report/$', BoardReportView.as_view(), name='board-report'),
)
