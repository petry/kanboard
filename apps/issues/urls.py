from django.conf.urls import patterns, url
from apps.issues.views import IssueDetailView, IssueAdvanceView, IssueOnBoardView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', IssueDetailView.as_view(), name='issue-detail'),
    url(r'^(?P<pk>\d+)/advance/$', IssueAdvanceView.as_view(), name='issue-advance'),
    url(r'^(?P<pk>\d+)/onboard/$', IssueOnBoardView.as_view(), name='issue-onboard'),
)
