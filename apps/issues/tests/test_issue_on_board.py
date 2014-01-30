from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import RequestFactory
from mock import patch
from model_mommy import mommy
from apps.boards.models import Board, Step, BoardPosition
from apps.core.tests.utils import LoggedTestCase
from apps.issues.models import Issue
from apps.issues.views import IssueOnBoardView


class IssueOnBoardViewTest(LoggedTestCase):

    def get_view(self):
        return IssueOnBoardView.as_view()

    def setUp(self):
        self.board = mommy.make(Board, id=34)
        self.step2 = Step.objects.create(board=self.board, name='step 2')
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)
        self.issue = mommy.make(Issue)

        self.view = self.get_view()
        user = User.objects.create_superuser(
            username='test_user',
            email='test_email',
            password='test'
        )
        self.factory = RequestFactory()
        self.request = self.factory.post('/some-url/', data={'board': self.board.id})
        self.request.user = user
        self.request.session = {}

    def test_should_redirect_to_board(self):
        response = self.view(self.request, pk=self.issue.pk)
        self.assertEqual(response.url, reverse('board-detail', kwargs={'pk': self.board.id}))
        self.assertEqual(dict(response.items())['Location'], reverse('board-detail', kwargs={'pk': self.board.id}))

    def test_redirect_should_not_be_permanent(self):
        response = self.view(self.request, pk=self.issue.pk)
        self.assertEqual(response.status_code, 302)

    @patch('apps.boards.forms.BoardPositionForm.on_board')
    def test_on_board_function_must_be_called(self, mock):
        mommy.make(BoardPosition, board=self.board, issue=self.issue)
        self.view(self.request, pk=self.issue.pk)
        self.assertTrue(mock.called)

    def test_redirect_if_not_logged(self):
        self.assertRedirectIfNotLogged()
