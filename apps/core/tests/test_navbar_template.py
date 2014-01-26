from django.contrib.auth import create_superuser
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from lxml import html
from apps.boards.models import Board
from apps.boards.views import BoardListView
from apps.issues.models import Issue


class BoardDetailViewTest(TestCase):
    urls = 'kanboard.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.request = self.factory.get('/')

    def test_should_have_a_login_link(self):
        response = BoardListView.as_view()(self.request, pk=self.board.pk)
        self.dom = html.fromstring(response.rendered_content)
        login = self.dom.cssselect('#user-menu a')[0]
        self.assertIn('href', login.attrib)
        self.assertEqual(login.attrib['href'], reverse('core-login'))

    def test_should_have_a_logout_link_when_logged(self):
        user = User.objects.create_superuser(
            username='test_user',
            email='test@mail',
            password='pass'
        )
        self.request.user = user
        self.request.session = {}
        response = BoardListView.as_view()(self.request, pk=self.board.pk)
        self.dom = html.fromstring(response.rendered_content)
        login = self.dom.cssselect('#user-menu a')[1]
        self.assertIn('href', login.attrib)
        self.assertEqual(login.attrib['href'], reverse('core-logout'))
