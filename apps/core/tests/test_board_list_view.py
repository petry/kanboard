from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.core.models import Board
from apps.core.views import BoardListView


class BoardListViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.request = self.factory.get('/')
        self.response = BoardListView.as_view()(self.request, pk=self.board.pk)

    def test_should_use_the_correctly_template(self):
        self.assertIn('core/board_list.html', self.response.template_name)