from django.test import TestCase
from model_mommy import mommy
from apps.core.forms import BoardPositionForm
from apps.core.models import Board, Step, Issue, BoardPosition, Transition


class OnBoardFormTestCase(TestCase):

    def setUp(self):
        self.board = mommy.make(Board)
        self.step2 = Step.objects.create(board=self.board, name='step 2')
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)
        self.issue = mommy.make(Issue)

    def test_shoul_have_only_board_field(self):
        self.form = BoardPositionForm()
        self.assertEqual(self.form.base_fields.keys(), ['board'])

    def test_board_field_must_have_all_board_choices(self):
        self.form = BoardPositionForm()
        board = self.form.base_fields['board']
        self.assertQuerysetEqual(Board.objects.all(), board.queryset, lambda obj: obj)

    def test_board_should_return_none_if_form_is_invalid(self):
        self.form = BoardPositionForm(data={'issue': self.issue.id, 'board': ""})
        position = self.form.on_board()

    def test_should_create_a_board_position(self):
        self.form = BoardPositionForm(data={'issue': self.issue.id, 'board': self.board.id})
        position = self.form.on_board()
        self.assertIsInstance(position, BoardPosition)

    def test_initial_step_must_be_a_default_status_of_position(self):
        self.form = BoardPositionForm(data={'issue': self.issue.id, 'board': self.board.id})
        position = self.form.on_board()
        position.status = self.board.step_set.get(initial=True)

    def test_should_create_a_transition(self):
        self.form = BoardPositionForm(data={'issue': self.issue.id, 'board': self.board.id})
        self.form.on_board()
        self.assertTrue(
            Transition.objects.filter(issue=self.issue, step=self.step1).exists()
        )