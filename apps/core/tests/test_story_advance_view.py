from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.core.models import Board, Step, Story, BoardPosition
from apps.core.views import StoryAdvanceView


class BoardListViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.board = mommy.make(Board)
        self.step2 = Step.objects.create(board=self.board, name='step 2')
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)
        self.story = mommy.make(Story)
        self.position = BoardPosition.objects.create(
            story=self.story,
            board=self.board,
            status=self.step1
        )

        self.request = self.factory.get('/boards/1/advance/')
        self.response = StoryAdvanceView.as_view()(self.request, pk=self.story.pk)

    def test_should_redirect_to_board(self):
        self.assertEqual(self.response.url, reverse('board-detail', kwargs={'pk': self.board.id}))
        self.assertEqual(dict(self.response.items())['Location'], reverse('board-detail', kwargs={'pk': self.board.id}))

