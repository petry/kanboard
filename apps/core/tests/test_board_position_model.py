from django.db import models
from django.test import TestCase
from model_mommy import mommy
from apps.core.models import BoardPosition


class BoardPositionTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['board', u'id', 'status', 'story'],
                         BoardPosition._meta.get_all_field_names())

    def test_name_should_be_a_char_field(self):
        member_field = BoardPosition._meta.get_field_by_name('board')[0]
        self.assertIsInstance(member_field, models.ForeignKey)

    def test_story_instance_should_output_name(self):
        instance = mommy.make(BoardPosition)
        self.assertEqual(unicode(instance),
                         "Story #{0} on board {1} in {2}".format(
                             instance.story.id, instance.board.id, instance.status.name))
