from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.boards.models import Board, BoardPosition
from apps.boards.views import BoardReportView
from apps.core.tests.utils import LoggedTestCase
from apps.issues.models import Issue
from apps.teams.models import Team


class BoardReportViewTest(LoggedTestCase):
    urls = 'kanboard.urls'

    def setUp(self):
        super(BoardReportViewTest, self).setUp()
        self.team = Team.objects.create(name='test-team')
        self.team.users.add(self.user)
        self.board = mommy.make(Board, team=self.team)


    def get_view(self):
        return BoardReportView.as_view()

    def test_should_use_the_correctly_template(self):
        self.response = self.view(self.request, pk=self.board.pk)
        self.assertIn('boards/board_report.html', self.response.template_name)

    def test_should_have_board_on_context(self):
        self.response = self.view(self.request, pk=self.board.pk)
        self.assertTrue(self.response.context_data.has_key('board'))
        self.assertEqual(self.response.context_data['board'], self.board)


    def test_should_have_Issued_from_that_board(self):
        issue_in_board = mommy.make(Issue, boardposition__board=self.board)
        mommy.make(BoardPosition, board=self.board, issue=issue_in_board)
        self.response = BoardReportView.as_view()(self.request, pk=self.board.pk)

        self.assertIn(issue_in_board, self.response.context_data['object_list'])

    def test_should_hot_have_issues_from_Another_board(self):
        issue_in_other_board = mommy.make(Issue, boardposition__board=self.board)
        self.response = BoardReportView.as_view()(self.request, pk=self.board.pk)
        self.assertNotIn(issue_in_other_board, self.response.context_data['object_list'])

    def test_redirect_if_not_logged(self):
        self.assertRedirectIfNotLogged()