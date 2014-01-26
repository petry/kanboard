# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib import admin as django_admin
from apps.issues.admin import IssueAdmin, PositionInline, TransitionInline
from apps.issues.models import Issue


class CoreAdminTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_Issue_model_should_be_registered_within_the_admin(self):
        self.assertIn(Issue, django_admin.site._registry)

    def test_issue_should_be_customize(self):
        self.assertTrue(django_admin.site._registry[Issue], IssueAdmin)

    def test_should_have_position_inlines(self):
        self.assertIn(PositionInline, IssueAdmin.inlines)

    def test_should_have_transition_inlines(self):
        self.assertIn(TransitionInline, IssueAdmin.inlines)