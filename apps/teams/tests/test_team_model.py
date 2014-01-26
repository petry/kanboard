import datetime
from django.db.models.related import RelatedObject
from model_mommy import mommy

from django.db import models
from django.test import TestCase
from apps.teams.models import Team


class TeamTestCase(TestCase):
    def test_should_have_all_fields_name(self):
        self.assertEqual(['board', u'id', 'name', 'users'],
                         Team._meta.get_all_field_names())

    def test_name_should_be_a_char_field(self):
        field = Team._meta.get_field_by_name('name')[0]
        self.assertIsInstance(field, models.CharField)

    def test_users_should_be_a_many2many_field(self):
        field = Team._meta.get_field_by_name('users')[0]
        self.assertIsInstance(field, models.ManyToManyField)

    def test_issue_instance_should_output_name(self):
        instance = mommy.make(Team)
        self.assertEqual(unicode(instance), "Team {0}".format(instance.name))
