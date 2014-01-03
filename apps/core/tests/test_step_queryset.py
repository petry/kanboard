from django.test import TestCase
from model_mommy import mommy
from apps.core.models import Board, Step


class StepQuerysetTest(TestCase):

    def test_should_find_all_steps_in_order(self):
        self.board = mommy.make(Board)
        self.step3 = Step.objects.create(board=self.board, name='step 3')
        self.step2 = Step.objects.create(board=self.board, name='step 2',
                                         next=self.step3)
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)

        self.assertEqual(self.board.steps(),
                         [self.step1, self.step2, self.step3])
        