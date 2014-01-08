from django.forms.widgets import HiddenInput
from django.test import TestCase
from model_mommy import mommy
from apps.core.forms import BoardPositionForm
from apps.core.models import Board, Step, Story, BoardPosition


class OnBoardFormTestCase(TestCase):

    def setUp(self):
        self.board = mommy.make(Board)
        self.step2 = Step.objects.create(board=self.board, name='step 2')
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)
        self.story = mommy.make(Story)


    def test_fiels_on_form(self):
        self.form = BoardPositionForm(initial={'story': self.story.id})
        self.assertEqual(self.form.base_fields.keys(), ['story', 'board'])

    def test_story_field_must_be_hidden(self):
        self.form = BoardPositionForm(initial={'story': self.story.id})
        self.assertIsInstance(self.form.base_fields['story'].widget, HiddenInput)

    def test_board_field_must_have_all_board_choices(self):
        self.form = BoardPositionForm(initial={'story': self.story.id})
        board = self.form.base_fields['board']
        self.assertQuerysetEqual(Board.objects.all(), board.queryset, lambda obj:obj)

    def test_should_create_a_board_position(self):
        self.form = BoardPositionForm( data={'story': self.story.id, 'board': self.board.id})
        position = self.form.on_board()
        self.assertIsInstance(position, BoardPosition)

    def test_initial_step_must_be_a_default_status_of_position(self):
        self.form = BoardPositionForm( data={'story': self.story.id, 'board': self.board.id})
        position = self.form.on_board()
        position.status = self.board.step_set.get(initial=True)