from django.test import TestCase
from django.db import models
from model_mommy import mommy

from apps.core.models import Story, Board, Step, Transition



class BoardTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['boardposition', u'id', 'name', 'step'],
                         Board._meta.get_all_field_names())

    def test_name_should_be_a_char_field(self):
        member_field = Board._meta.get_field_by_name('name')[0]
        self.assertIsInstance(member_field, models.CharField)

    def test_board_instance_should_output_name(self):
        instance = mommy.make(Board)
        self.assertEqual(unicode(instance), instance.name)


class StoryTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['boardposition', u'id', 'name', 'transition'],
                         Story._meta.get_all_field_names())

    def test_name_should_be_a_char_field(self):
        member_field = Story._meta.get_field_by_name('name')[0]
        self.assertIsInstance(member_field, models.CharField)

    def test_story_instance_should_output_name(self):
        instance = mommy.make(Story)
        self.assertEqual(unicode(instance), instance.name)


class StepTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['board', 'boardposition', u'id', 'initial',
                          'name', 'next', 'step', 'transition'],
                         Step._meta.get_all_field_names()
        )


    def test_name_should_be_a_char_field(self):
        member_field = Step._meta.get_field_by_name('name')[0]
        self.assertIsInstance(member_field, models.CharField)

    def test_initial_should_be_a_char_field(self):
        member_field = Step._meta.get_field_by_name('initial')[0]
        self.assertIsInstance(member_field, models.BooleanField)

    def test_board_should_be_a_foreign_key(self):
        member_field = Step._meta.get_field_by_name('board')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Board, member_field.related.parent_model)

    def test_next_should_be_a_foreign_key(self):
        member_field = Step._meta.get_field_by_name('next')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Step, member_field.related.parent_model)

    def test_board_instance_should_output_name(self):
        instance = mommy.make(Step)
        self.assertEqual(unicode(instance), instance.name)


class TransitionTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['date', u'id', 'step', 'story'], Transition._meta.get_all_field_names())

    def test_date_should_be_a_datetime_field(self):
        member_field = Transition._meta.get_field_by_name('date')[0]
        self.assertIsInstance(member_field, models.DateTimeField)

    def test_story_should_be_a_foreign_key(self):
        member_field = Transition._meta.get_field_by_name('story')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Story, member_field.related.parent_model)

    def test_next_should_be_a_foreign_key(self):
        member_field = Transition._meta.get_field_by_name('step')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Step, member_field.related.parent_model)

    def test_board_instance_should_output_name(self):
        instance = mommy.make(Transition)
        self.assertEqual(unicode(instance), u"#{0} on {1}".format(instance.story.id, instance.step.name))
