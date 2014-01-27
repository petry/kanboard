from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.boards.models import Board, Step
from apps.boards.views import BoardDetailView
from apps.core.tests.utils import LoggedTestCase
from apps.issues.models import Issue


class BoardDetailViewTest(LoggedTestCase):
    urls = 'kanboard.urls'

    def setUp(self):
        super(BoardDetailViewTest, self).setUp()
        self.board = mommy.make(Board)
        self.issue = mommy.make(Issue)

    def test_should_use_the_correctly_template(self):
        self.response = BoardDetailView.as_view()(self.request, pk=self.board.pk)
        self.assertIn('boards/board_detail.html', self.response.template_name)

    def test_should_not_have_panel_size_class_on_context_if_board_doesnt_have_a_step(self):
        mommy.make(Step, board=self.board)
        self.response = BoardDetailView.as_view()(self.request, pk=self.board.pk)
        self.assertTrue(self.response.context_data.has_key('panel_size_class'))

    def test_should_have_panel_size_class_on_context_if_step_exists(self):
        self.response = BoardDetailView.as_view()(self.request, pk=self.board.pk)
        self.assertFalse(self.response.context_data.has_key('panel_size_class'))