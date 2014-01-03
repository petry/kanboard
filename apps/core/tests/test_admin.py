# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib import admin as django_admin
from apps.core.admin import StoryAdmin, BoardAdmin
from apps.core.models import Board, Step, Story, Transition


class CoreAdminTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_Board_model_should_be_registered_within_the_admin(self):
        self.assertIn(Board, django_admin.site._registry)

    def test_board_should_be_customize(self):
        self.assertTrue(django_admin.site._registry[Board], BoardAdmin)

    def test_Story_model_should_be_registered_within_the_admin(self):
        self.assertIn(Story, django_admin.site._registry)

    def test_story_should_be_customize(self):
        self.assertTrue(django_admin.site._registry[Story], StoryAdmin)

    def test_Transition_model_should_be_registered_within_the_admin(self):
        self.assertIn(Transition, django_admin.site._registry)
