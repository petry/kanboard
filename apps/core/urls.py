from django.conf.urls import patterns, url
from apps.boards.views import BoardListView
from apps.core.forms import CustomAuthenticationForm

urlpatterns = patterns(
    '',
    url(r'^$', BoardListView.as_view(), name='board-list'),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^accounts/login/', 'login', name='core-login', kwargs={'authentication_form': CustomAuthenticationForm}),
    url(r'^accounts/logout/$', 'logout_then_login', name='core-logout'),
)
