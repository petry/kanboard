from django.conf.urls import patterns, url
from apps.boards.views import BoardListView

urlpatterns = patterns('',
    url(r'^$', BoardListView.as_view(), name='board-list'),
)
