from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.core.models import Board, BoardPosition
from apps.core.views import BoardReportView
from apps.issues.models import Issue


class BoardReportViewTest(TestCase):
    urls = 'apps.core.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.request = self.factory.get('/boards/1/report')

    def test_should_use_the_correctly_template(self):
        self.response = BoardReportView.as_view()(self.request, pk=self.board.pk)
        self.assertIn('core/board_report.html', self.response.template_name)

    def test_should_have_board_on_context(self):
        self.response = BoardReportView.as_view()(self.request, pk=self.board.pk)
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
