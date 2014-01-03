from django.test import TestCase
from django.db import models

from apps.core.models import Story, Board, Step


class BaseModelTest(TestCase):
    def assert_field_in(self, field_name, model):
        self.assertIn(field_name, model._meta.get_all_field_names())


class BoardTestCase(BaseModelTest):
    def test_should_have_a_name(self):
        self.assert_field_in('name', Story)

    def test_name_should_be_a_char_field(self):
        member_field = Board._meta.get_field_by_name('name')[0]
        self.assertIsInstance(member_field, models.CharField)


class StoryTestCase(BaseModelTest):
    def test_should_have_a_name(self):
        self.assert_field_in('name', Story)

    def test_name_should_be_a_char_field(self):
        member_field = Story._meta.get_field_by_name('name')[0]
        self.assertIsInstance(member_field, models.CharField)

    def test_should_have_a_board(self):
        self.assert_field_in('board', Story)

    def test_board_should_be_a_foreign_key(self):
        member_field = Story._meta.get_field_by_name('board')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Board, member_field.related.parent_model)


class StepTestCase(BaseModelTest):
    def test_should_have_a_name(self):
        self.assert_field_in('name', Step)

    def test_name_should_be_a_char_field(self):
        member_field = Step._meta.get_field_by_name('name')[0]
        self.assertIsInstance(member_field, models.CharField)

    def test_should_have_a_board(self):
        self.assert_field_in('board', Step)

    def test_board_should_be_a_foreign_key(self):
        member_field = Step._meta.get_field_by_name('board')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Board, member_field.related.parent_model)

    def test_should_have_a_next(self):
        self.assert_field_in('next', Step)

    def test_next_should_be_a_foreign_key(self):
        member_field = Step._meta.get_field_by_name('next')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Step, member_field.related.parent_model)
