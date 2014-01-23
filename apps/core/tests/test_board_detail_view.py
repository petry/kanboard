from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.core.models import Board, Issue, Step
from apps.core.views import BoardDetailView


class BoardDetailViewTest(TestCase):
    urls = 'apps.core.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.issue = mommy.make(Issue)
        self.request = self.factory.get('/boards/1/')

    def test_should_use_the_correctly_template(self):
        self.response = BoardDetailView.as_view()(self.request, pk=self.board.pk)
        self.assertIn('core/board_detail.html', self.response.template_name)

    def test_should_not_have_panel_size_class_on_context_if_board_doesnt_have_a_step(self):
        mommy.make(Step, board=self.board)
        self.response = BoardDetailView.as_view()(self.request, pk=self.board.pk)
        self.assertTrue(self.response.context_data.has_key('panel_size_class'))

    def test_should_have_panel_size_class_on_context_if_step_exists(self):
        self.response = BoardDetailView.as_view()(self.request, pk=self.board.pk)
        self.assertFalse(self.response.context_data.has_key('panel_size_class'))