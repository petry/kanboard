from django.core.urlresolvers import reverse
from django.db import models
from django.test import TestCase
from model_mommy import mommy
from apps.boards.models import Board, Step
from apps.teams.models import Team


class ModelTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['boardposition', u'id', 'name', 'step', 'team'],
                         Board._meta.get_all_field_names())

    def test_name_should_be_a_char_field(self):
        field = Board._meta.get_field_by_name('name')[0]
        self.assertIsInstance(field, models.CharField)

    def test_team_should_be_a_foreign_key_to_team_model(self):
        field = Board._meta.get_field_by_name('team')[0]
        self.assertIsInstance(field, models.ForeignKey)
        self.assertEqual(field.related.parent_model, Team)

    def test_board_instance_should_output_name(self):
        instance = mommy.make(Board)
        self.assertEqual(unicode(instance), instance.name)


class BoardTestCase(TestCase):

    def setUp(self):
        self.board = mommy.make(Board)
        super(BoardTestCase, self).setUp()

    def test_should_output_absolute_url(self):
        self.assertEqual(
            self.board.get_absolute_url(),
            reverse('board-detail', kwargs={'pk': self.board.id})
        )

    def test_should_find_all_steps_in_order(self):
        self.step3 = Step.objects.create(board=self.board, name='step 3')
        self.step2 = Step.objects.create(board=self.board, name='step 2',
                                         next=self.step3)
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)

        self.assertEqual(self.board.steps(),
                         [self.step1, self.step2, self.step3])

