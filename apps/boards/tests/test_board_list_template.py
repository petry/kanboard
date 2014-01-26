from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from lxml import html
from apps.boards.views import BoardListView
from apps.core.models import Board
from apps.issues.models import Issue


class BoardDetailViewTest(TestCase):
    urls = 'kanboard.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.request = self.factory.get('/')

        response = BoardListView.as_view()(self.request, pk=self.board.pk)
        self.dom = html.fromstring(response.rendered_content)

    def test_should_have_a_list_of_boards(self):
        board = self.dom.cssselect('.table-responsive tbody tr a')[0]
        self.assertEqual(board.text, self.board.name)

    def test_board_item_should_be_a_link_to_betailed_board(self):
        board = self.dom.cssselect('.table-responsive tbody tr a')[0]
        self.assertEqual(board.attrib['href'], reverse("board-detail", kwargs={"pk": self.board.id}))

    def test_issue_should_have_icebox_panel_when_has_issue_without_board(self):
        mommy.make(Issue)
        response = BoardListView.as_view()(self.request, pk=self.board.pk)
        dom = html.fromstring(response.rendered_content)

        title = dom.cssselect('.icebox .panel h3.panel-title')[0]
        self.assertEqual(title.text, "ICEBOX")

    def test_issue_should_be_on_icebox_when_it_any_other_board(self):
        issue = mommy.make(Issue)
        response = BoardListView.as_view()(self.request, pk=self.board.pk)
        dom = html.fromstring(response.rendered_content)
        panel = dom.cssselect('.icebox .panel .panel-body')[0]
        title = panel.cssselect('.issue-item.badge')[0]
        self.assertEqual(title.text.strip(), "#{0} {1}".format(issue.id, issue.name))
