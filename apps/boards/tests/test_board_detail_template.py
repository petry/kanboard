from django.core.urlresolvers import reverse
from model_mommy import mommy
from lxml import html
from apps.boards.models import Board, Step, BoardPosition
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

        self.step3 = mommy.make(Step, board=self.board)
        self.step2 = mommy.make(Step, board=self.board, next=self.step3)
        self.step1 = mommy.make(Step, board=self.board, next=self.step2, initial=True)

        response = self.get_view()(self.request, pk=self.board.pk)
        self.dom = html.fromstring(response.rendered_content)

    def test_should_have_report_link(self):
        link = self.dom.cssselect('.links .glyphicon.glyphicon-print')[0]
        self.assertEqual(link.attrib['href'], reverse('board-report', kwargs={'pk': self.board.id}))
        self.assertEqual(link.cssselect('span')[0].text, 'Report')

    def test_should_have_steps_on_the_board(self):
        panels = self.dom.cssselect('.steps .panel .panel-heading h3')
        self.assertEqual(self.step1.name, panels[0].text)
        self.assertEqual(self.step2.name, panels[1].text)
        self.assertEqual(self.step3.name, panels[2].text)

    def test_should_have_an_issue_on_step(self):
        issue = mommy.make(Issue)
        mommy.make(BoardPosition, issue=issue, status=self.step2)
        response = self.get_view()(self.request, pk=self.board.pk)
        dom = html.fromstring(response.rendered_content)
        step2 = dom.cssselect('.steps .panel')[1]

        self.assertEqual(1, len(step2.cssselect('.issue-item.badge')))
        title = step2.cssselect('.issue-item.badge')[0]
        self.assertEqual(title.text.strip(), "#{0} {1}".format(issue.id, issue.name))

    def test_should_not_have_an_issue_on_step_if_flag_id_false(self):
        issue = mommy.make(Issue)
        mommy.make(BoardPosition, issue=issue, status=self.step2, show=False)
        response = self.get_view()(self.request, pk=self.board.pk)
        dom = html.fromstring(response.rendered_content)
        step2 = dom.cssselect('.steps .panel')[1]

        self.assertEqual(0, len(step2.cssselect('.issue-item.badge')))

    def test_redirect_if_not_logged(self):
        self.assertRedirectIfNotLogged()