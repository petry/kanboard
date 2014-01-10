from django.db import models
from django.test import TestCase
from model_mommy import mommy
from apps.core.models import BoardPosition, Board, Step, Issue


class ModelTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['board', u'id', 'issue', 'status'],
                         BoardPosition._meta.get_all_field_names())

    def test_name_should_be_a_char_field(self):
        member_field = BoardPosition._meta.get_field_by_name('board')[0]
        self.assertIsInstance(member_field, models.ForeignKey)

    def test_issue_instance_should_output_name(self):
        instance = mommy.make(BoardPosition)
        self.assertEqual(unicode(instance),
                         "Issue #{0} on board {1} in {2}".format(
                             instance.issue.id, instance.board.id, instance.status.name))


class BoardPositionTestCase(TestCase):

    def setUp(self):
        super(BoardPositionTestCase, self).setUp()
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

    def test_should_advance_step(self):
        self.assertEqual(self.position.status, self.step1)
        last_position = self.position.go()
        self.assertEqual(self.position.status, self.step2)
        self.assertEqual(last_position, self.step2)

    def test_should_remain_in_the_last_position(self):
        self.position.go()
        self.assertEqual(self.position.status, self.step2)
        last_position = self.position.go()
        self.assertEqual(self.position.status, self.step2)
        self.assertEqual(last_position, self.step2)
