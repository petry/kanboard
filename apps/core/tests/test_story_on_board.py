from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from mock import patch
from model_mommy import mommy
from apps.core.models import Board, Step, Issue, BoardPosition
from apps.core.views import IssueAdvanceView, IssueOnBoardView


class IssueOnBoardViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.board = mommy.make(Board, id=34)
        self.step2 = Step.objects.create(board=self.board, name='step 2')
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)
        self.issue = mommy.make(Issue)

        self.request = self.factory.post('/issue/1/on_board/', data={'board': self.board.id})

    def test_should_redirect_to_board(self):
        response = IssueOnBoardView.as_view()(self.request, pk=self.issue.pk)
        self.assertEqual(response.url, reverse('board-detail', kwargs={'pk': self.board.id}))
        self.assertEqual(dict(response.items())['Location'], reverse('board-detail', kwargs={'pk': self.board.id}))

    def test_redirect_shoulf_not_be_permanent(self):
        response = IssueOnBoardView.as_view()(self.request, pk=self.issue.pk)
        self.assertEqual(response.status_code, 302)

    @patch('apps.core.forms.BoardPositionForm.on_board')
    def test_on_board_function_must_be_called(self, mock):
        mommy.make(BoardPosition, board=self.board, issue=self.issue)
        response = IssueOnBoardView.as_view()(self.request, pk=self.issue.pk)
        self.assertTrue(mock.called)