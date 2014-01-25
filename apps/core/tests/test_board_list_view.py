from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.boards.views import BoardListView
from apps.core.models import Board
from apps.issues.models import Issue


class BoardListViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.request = self.factory.get('/')
        self.response = BoardListView.as_view()(self.request, pk=self.board.pk)

    def test_should_use_the_correctly_template(self):
        self.assertIn('core/board_list.html', self.response.template_name)

    def test_should_have_stories_in_icebox_on_context(self):
        self.assertIn('icebox', self.response.context_data)
        self.assertQuerysetEqual(self.response.context_data['icebox'],
                                 Issue.objects.filter(boardposition=None),
                                 lambda obj:obj)
