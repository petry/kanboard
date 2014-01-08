from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.core.models import Board, Story
from apps.core.views import BoardDetailView


class BoardDetailViewTest(TestCase):
    urls = 'apps.core.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.board = mommy.make(Board)
        self.story = mommy.make(Story)
        self.request = self.factory.get('/boards/1/')
        self.response = BoardDetailView.as_view()(self.request, pk=self.board.pk)

    def test_should_use_the_correctly_template(self):
        self.assertIn('core/board_detail.html', self.response.template_name)

    def test_should_have_stories_in_icebox_on_context(self):
        self.assertIn('icebox', self.response.context_data)
        self.assertQuerysetEqual(self.response.context_data['icebox'],
                                 Story.objects.filter(boardposition=None),
                                 lambda obj:obj)
