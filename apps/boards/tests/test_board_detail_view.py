from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.boards.models import Board, Step
from apps.boards.views import BoardDetailView
from apps.core.tests.utils import LoggedTestCase
from apps.issues.models import Issue
from apps.teams.models import Team


class BoardDetailViewTest(LoggedTestCase):
    urls = 'kanboard.urls'



    def get_view(self):
        return BoardDetailView.as_view()

    def setUp(self):
        super(BoardDetailViewTest, self).setUp()
        self.team = Team.objects.create(name='test-team')
        self.team.users.add(self.user)
        self.board = mommy.make(Board, team=self.team)
        self.issue = mommy.make(Issue)

    def test_should_use_the_correctly_template(self):
        self.response = self.view(self.request, pk=self.board.pk)
        self.assertIn('boards/board_detail.html', self.response.template_name)

    def test_should_not_have_panel_size_class_on_context_if_board_doesnt_have_a_step(self):
        mommy.make(Step, board=self.board)
        self.response = self.view(self.request, pk=self.board.pk)
        self.assertIn('panel_size_class',self.response.context_data)

    def test_should_have_panel_size_class_on_context_if_step_exists(self):
        self.response = self.view(self.request, pk=self.board.pk)
        self.assertNotIn('panel_size_class',self.response.context_data)

    def test_redirect_if_not_logged(self):
        self.assertRedirectIfNotLogged()

    def test_should_redirect_to_board_list_if_member_not_has_permission_(self):
        self.team.users.remove(self.user)
        self.assertRaises(PermissionDenied, self.view, self.request, pk=self.board.pk)