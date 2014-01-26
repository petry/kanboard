from django.db import models
from django.test import TestCase
from model_mommy import mommy
from apps.boards.models import Transition, Step
from apps.issues.models import Issue


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