from model_mommy import mommy
from apps.boards.models import Board
from apps.boards.views import BoardListView
from apps.core.tests.utils import LoggedTestCase
from apps.issues.models import Issue
from apps.teams.models import Team


class BoardListViewTest(LoggedTestCase):

    def get_view(self):
        return BoardListView.as_view()

    def test_should_use_the_correctly_template(self):
        self.response = self.view(self.request, pk=self.board.pk)
        self.assertIn('boards/board_list.html', self.response.template_name)

    def test_should_have_stories_in_icebox_on_context(self):
        self.response = self.view(self.request, pk=self.board.pk)
        self.assertIn('icebox', self.response.context_data)
        self.assertQuerysetEqual(self.response.context_data['icebox'],
                                 Issue.objects.filter(boardposition=None),
                                 lambda obj:obj)

    def test_should_display_the_board_only_when_the_member_has_permission_(self):
        team = Team.objects.create(name='test-team')
        team.users.add(self.user)
        board_1 = mommy.make(Board, team=team)

        board_2 = mommy.make(Board)

        self.response = self.view(self.request, pk=self.board.pk)
        self.assertIn(board_1, self.response.context_data['object_list'])
        self.assertNotIn(board_2, self.response.context_data['object_list'])

    def test_redirect_if_not_logged(self):
        self.assertRedirectIfNotLogged()
