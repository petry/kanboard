from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from lxml import html
from apps.boards.models import Board
from apps.boards.tests.test_board_list_view import LoggedTestCase
from apps.core.views import IndexView


class NavbarTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.request = self.factory.get('/')

    def test_should_have_a_login_link(self):
        response = IndexView.as_view()(self.request, pk=self.board.pk)
        self.dom = html.fromstring(response.rendered_content)
        login = self.dom.cssselect('#user-menu a')[0]
        self.assertIn('href', login.attrib)
        self.assertEqual(login.attrib['href'], reverse('core-login'))

class LoggedNavbarTestCase(LoggedTestCase):
    urls = 'kanboard.urls'

    def test_should_have_a_logout_link_when_logged(self):
        response = IndexView.as_view()(self.request, pk=self.board.pk)
        self.dom = html.fromstring(response.rendered_content)
        login = self.dom.cssselect('#user-menu a')[1]
        self.assertIn('href', login.attrib)
        self.assertEqual(login.attrib['href'], reverse('core-logout'))
