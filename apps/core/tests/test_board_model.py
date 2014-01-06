from django.db import models
from django.test import TestCase
from model_mommy import mommy
from apps.core.models import Board, Step


class ModelTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['boardposition', u'id', 'name', 'step'],
                         Board._meta.get_all_field_names())

    def test_name_should_be_a_char_field(self):
        member_field = Board._meta.get_field_by_name('name')[0]
        self.assertIsInstance(member_field, models.CharField)

    def test_board_instance_should_output_name(self):
        instance = mommy.make(Board)
        self.assertEqual(unicode(instance), instance.name)


class BoardTestCase(TestCase):

    def test_should_find_all_steps_in_order(self):
        self.board = mommy.make(Board)
        self.step3 = Step.objects.create(board=self.board, name='step 3')
        self.step2 = Step.objects.create(board=self.board, name='step 2',
                                         next=self.step3)
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)

        self.assertEqual(self.board.steps(),
                         [self.step1, self.step2, self.step3])
