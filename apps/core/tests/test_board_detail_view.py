from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.core.models import Board, Issue
from apps.core.views import BoardDetailView


class BoardDetailViewTest(TestCase):
    urls = 'apps.core.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.issue = mommy.make(Issue)
        self.request = self.factory.get('/boards/1/')
        self.response = BoardDetailView.as_view()(self.request, pk=self.board.pk)

    def test_should_use_the_correctly_template(self):
        self.assertIn('core/board_detail.html', self.response.template_name)
