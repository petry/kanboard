from django.test import TestCase
from django.db import models
from model_mommy import mommy

from apps.core.models import Board, Step, Transition
from apps.issues.models import Issue


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
        self.assertEqual(unicode(instance), "{0} - {1}".format(instance.board, instance.name))


class TransitionTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['date', u'id', 'issue', 'step'], Transition._meta.get_all_field_names())

    def test_date_should_be_a_datetime_field(self):
        member_field = Transition._meta.get_field_by_name('date')[0]
        self.assertIsInstance(member_field, models.DateTimeField)

    def test_issue_should_be_a_foreign_key(self):
        member_field = Transition._meta.get_field_by_name('issue')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Issue, member_field.related.parent_model)

    def test_next_should_be_a_foreign_key(self):
        member_field = Transition._meta.get_field_by_name('step')[0]
        self.assertIsInstance(member_field, models.ForeignKey)
        self.assertEqual(Step, member_field.related.parent_model)

    def test_board_instance_should_output_name(self):
        instance = mommy.make(Transition)
        self.assertEqual(unicode(instance),
                         u"#{0} in {1} on {2}".format(instance.issue.id, instance.step.name, instance.date))
