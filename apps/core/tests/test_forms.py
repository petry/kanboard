from django.core.urlresolvers import reverse
from django.forms.widgets import HiddenInput
from django.test import TestCase, RequestFactory
from mock import patch
from model_mommy import mommy
from apps.core.forms import OnBoardForm
from apps.core.models import Board, Step, Story, BoardPosition
from apps.core.views import StoryAdvanceView


class OnBoardFormTestCase(TestCase):

    def setUp(self):
        self.form = OnBoardForm()
        self.board = mommy.make(Board)
        self.step2 = Step.objects.create(board=self.board, name='step 2')
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)
        self.story = mommy.make(Story)

    def test_fiels_on_form(self):
        self.assertEqual(self.form.base_fields.keys(), ['story', 'board'])

    def test_story_field_must_be_hidden(self):
        self.assertIsInstance(self.form.base_fields['story'].widget, HiddenInput)

    def test_board_field_must_have_all_board_choices(self):
        board = self.form.base_fields['board']
        self.assertQuerysetEqual(Board.objects.all(), board.queryset, lambda obj:obj)
