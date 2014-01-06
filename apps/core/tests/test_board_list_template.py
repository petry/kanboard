from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from lxml import html
from apps.core.models import Board
from apps.core.views import BoardListView


class BoardDetailViewTest(TestCase):
    urls = 'apps.core.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.request = self.factory.get('/')

        response = BoardListView.as_view()(self.request, pk=self.board.pk)
        self.dom = html.fromstring(response.rendered_content)

    def test_should_have_kamboard_on_title(self):
        title = self.dom.cssselect('h1')[0]
        self.assertEqual(title.text, "Kamboard")

    def test_should_have_a_list_of_boards(self):
        board = self.dom.cssselect('.table-responsive tbody tr a')[0]
        self.assertEqual(board.text, self.board.name)

    def test_board_item_should_be_a_link_to_betailed_board(self):
        board = self.dom.cssselect('.table-responsive tbody tr a')[0]
        self.assertEqual(board.attrib['href'], reverse("board-detail", kwargs={"pk":self.board.id}))
