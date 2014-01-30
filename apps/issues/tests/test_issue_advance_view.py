from django.core.urlresolvers import reverse
from mock import patch
from model_mommy import mommy
from apps.boards.models import Board, Step, BoardPosition
from apps.core.tests.utils import LoggedTestCase
from apps.issues.models import Issue
from apps.issues.views import IssueAdvanceView


class IssueAdvanceViewTest(LoggedTestCase):

    def get_view(self):
        return IssueAdvanceView.as_view()

    def setUp(self):
        super(IssueAdvanceViewTest, self).setUp()
        self.board = mommy.make(Board)
        self.step2 = Step.objects.create(board=self.board, name='step 2')
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)
        self.issue = mommy.make(Issue)
        self.position = BoardPosition.objects.create(
            issue=self.issue,
            board=self.board,
            status=self.step1
        )

    def test_should_redirect_to_board(self):
        response = self.view(self.request, pk=self.issue.pk)
        self.assertEqual(response.url, reverse('board-detail', kwargs={'pk': self.board.id}))
        self.assertEqual(dict(response.items())['Location'], reverse('board-detail', kwargs={'pk': self.board.id}))

    def test_redirect_shoul_not_be_permanent(self):
        response = self.view(self.request, pk=self.issue.pk)
        self.assertEqual(response.status_code, 302)

    @patch('apps.boards.models.BoardPosition.go')
    def test_should_advance_position(self, mock):
        self.view(self.request, pk=self.issue.pk)
        self.assertTrue(mock.called)
