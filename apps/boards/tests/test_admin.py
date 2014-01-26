# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib import admin as django_admin
from apps.boards.admin import BoardAdmin, TransitionAdmin, StepInline
from apps.boards.models import Board, Transition


class BoardsAdminTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_Board_model_should_be_registered_within_the_admin(self):
        self.assertIn(Board, django_admin.site._registry)

    def test_board_should_be_customize(self):
        self.assertTrue(django_admin.site._registry[Board], BoardAdmin)

    def test_should_have_step_inline_board(self):
        self.assertIn(StepInline, BoardAdmin.inlines)

    def test_Transition_model_should_be_registered_within_the_admin(self):
        self.assertIn(Transition, django_admin.site._registry)

    def test_transition_should_be_customize(self):
        self.assertTrue(django_admin.site._registry[Transition], TransitionAdmin)
