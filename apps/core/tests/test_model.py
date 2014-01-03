from django.test import TestCase
from django.db import models
from model_mommy import mommy

from apps.core.models import Story, Board, Step, Transition


class BaseModelTest(TestCase):
    def assert_field_in(self, field_name, model):
        self.assertIn(field_name, model._meta.get_all_field_names())


class BoardTestCase(BaseModelTest):
    def test_should_have_a_name(self):
        self.assert_field_in('name', Story)

    def test_name_should_be_a_char_field(self):
        member_field = Board._meta.get_field_by_name('name')[0]
        self.assertIsInstance(member_field, models.CharField)

    def test_board_instance_should_output_name(self):
        instance = mommy.make(Board)
        self.assertEqual(unicode(instance), instance.name)

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

    def test_story_instance_should_output_name(self):
        instance = mommy.make(Story)
        self.assertEqual(unicode(instance), instance.name)


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

    def test_board_instance_should_output_name(self):
        instance = mommy.make(Step)
        self.assertEqual(unicode(instance), instance.name)

class TransitionTestCase(BaseModelTest):
    def test_should_have_a_date(self):
        self.assert_field_in('date', Transition)

    def test_date_should_be_a_datetime_field(self):
        member_field = Transition._meta.get_field_by_name('date')[0]
        self.assertIsInstance(member_field, models.DateTimeField)

    def test_should_have_a_story(self):
        self.assert_field_in('story', Transition)

    def test_story_should_be_a_foreign_key(self):
        member_field = Transition._meta.get_field_by_name('story')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Story, member_field.related.parent_model)

    def test_should_have_a_step(self):
        self.assert_field_in('step', Transition)

    def test_next_should_be_a_foreign_key(self):
        member_field = Transition._meta.get_field_by_name('step')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Step, member_field.related.parent_model)
