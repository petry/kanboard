import datetime
from model_mommy import mommy

from django.db import models
from django.test import TestCase
from django.utils import timezone

from apps.boards.models import Board, Step, BoardPosition, Transition
from apps.issues.models import Issue


class IssueModelTest(TestCase):

    def setUp(self):
        self.board = mommy.make(Board)
        self.step2 = Step.objects.create(board=self.board, name='step 2')
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)
        self.issue = mommy.make(Issue)
        self.position = BoardPosition.objects.create(
            issue=self.issue,
            board=self.board,
            status=self.step1
        )
        self.first_transition = Transition.objects.create(
            issue=self.issue,
            step=self.step1
        )

    def test_should_find_first_transition(self):
        self.last_transition = Transition.objects.create(
            issue=self.issue,
            step=self.step2
        )
        self.assertEqual(self.first_transition, self.issue.get_first_transition())

    def test_should_find_last_transition(self):
        self.last_transition = Transition.objects.create(
            issue=self.issue,
            step=self.step2
        )
        self.assertEqual(self.last_transition, self.issue.get_last_transition())

    def test_should_return_issue_duration(self):
        self.last_transition = Transition.objects.create(
            issue=self.issue,
            step=self.step2
        )
        self.assertIsInstance(self.issue.get_duration(), datetime.timedelta)


class IssueTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['boardposition', 'description', u'id', 'name', 'transition'],
                         Issue._meta.get_all_field_names())

    def test_name_should_be_a_char_field(self):
        member_field = Issue._meta.get_field_by_name('name')[0]
        self.assertIsInstance(member_field, models.CharField)

    def test_issue_instance_should_output_name(self):
        instance = mommy.make(Issue)
        self.assertEqual(unicode(instance), instance.name)


class IssueTransitionTest(TestCase):

    def setUp(self):
        super(IssueTransitionTest, self).setUp()
        self.issue = mommy.make(Issue)
        self.board = mommy.make(Board)
        self.step3 = Step.objects.create(board=self.board, name='step 3')
        self.step2 = Step.objects.create(board=self.board, name='step 2',
                                         next=self.step3)
        self.step1 = Step.objects.create(board=self.board, name='step 1',
                                         next=self.step2, initial=True)

        self.first_transition = Transition.objects.create(
            issue=self.issue,
            step=self.step1
        )
        self.second_transition = Transition.objects.create(
            issue=self.issue,
            step=self.step2
        )
        self.last_transition = Transition.objects.create(
            issue=self.issue,
            step=self.step3
        )

    def test_should_get_first_transition(self):
        self.assertEqual(self.issue.get_first_transition(), self.first_transition)

    def test_should_get_last_transition(self):
        self.assertEqual(self.issue.get_last_transition(), self.last_transition)

    def test_should_return_none_id_doesnt_have_last_trantision(self):
        self.last_transition.delete()
        self.assertIsNone(self.issue.get_last_transition())

    def test_should_return_get_expected_date(self):
        self.first_transition.date = datetime.datetime(2014, 1, 1)
        self.first_transition.save()
        time_delta = datetime.timedelta(days=5)

        self.assertEqual(self.issue.get_expected_date(time_delta),
                         datetime.datetime(2014, 1, 6, tzinfo=timezone.utc))

    def test_should_return_duration(self):
        self.first_transition.date = datetime.datetime(2014, 1, 1)
        self.first_transition.save()
        self.last_transition.date = datetime.datetime(2014, 1, 5)
        self.last_transition.save()
        self.assertEqual(self.issue.get_duration(), datetime.timedelta(4))

    def test_shoruld_not_return_duration_if_issoen_downt_have_last_transition(self):
        self.last_transition.delete()
        self.assertIsNone(self.issue.get_duration())