from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from mock import patch
from model_mommy import mommy
from apps.core.models import Board, Step, Story, BoardPosition
from apps.core.views import StoryAdvanceView, StoryOnBoardView


class StoryOnBoardViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.board = mommy.make(Board, id=34)
        self.step2 = Step.objects.create(board=self.board, name='step 2')
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)
        self.story = mommy.make(Story)

        self.request = self.factory.post('/story/1/on_board/', data={'board_id': self.board.id})

    def test_should_redirect_to_board(self):
        response = StoryOnBoardView.as_view()(self.request, pk=self.story.pk)
        self.assertEqual(response.url, reverse('board-detail', kwargs={'pk': self.board.id}))
        self.assertEqual(dict(response.items())['Location'], reverse('board-detail', kwargs={'pk': self.board.id}))

    def test_redirect_shoulf_not_be_permanent(self):
        response = StoryOnBoardView.as_view()(self.request, pk=self.story.pk)
        self.assertEqual(response.status_code, 302)