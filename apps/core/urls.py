from django.conf.urls import patterns, url
from apps.core.views import BoardDetailView, IssueDetailView, BoardListView, IssueOnBoardView, IssueAdvanceView

urlpatterns = patterns('',
    url(r'^$', BoardListView.as_view(), name='board-list'),
    url(r'^board/(?P<pk>\d+)/$', BoardDetailView.as_view(), name='board-detail'),
    url(r'^issue/(?P<pk>\d+)/$', IssueDetailView.as_view(), name='issue-detail'),
    url(r'^issue/(?P<pk>\d+)/advance/$', IssueAdvanceView.as_view(), name='issue-advance'),
    url(r'^issue/(?P<pk>\d+)/onboard/$', IssueOnBoardView.as_view(), name='issue-onboard'),
)
