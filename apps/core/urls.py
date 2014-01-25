from django.conf.urls import patterns, url
from apps.boards.views import BoardListView, BoardDetailView, BoardReportView
from apps.issues.views import IssueDetailView, IssueAdvanceView, IssueOnBoardView

urlpatterns = patterns('',
    url(r'^$', BoardListView.as_view(), name='board-list'),
)
