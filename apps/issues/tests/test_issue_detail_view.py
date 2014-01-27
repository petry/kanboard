from model_mommy import mommy
from apps.boards.forms import BoardPositionForm
from apps.core.tests.utils import LoggedTestCase
from apps.issues.models import Issue
from apps.issues.views import IssueDetailView


class IssueDetailDefaultTest(LoggedTestCase):
    def get_view(self):
        return IssueDetailView.as_view()

    def setUp(self):
        super(IssueDetailDefaultTest, self).setUp()
        self.issue = mommy.make(Issue)

    def test_should_have_board_form_on_context(self):
        self.response = self.view(self.request, pk=self.issue.pk)
        self.assertTrue(self.response.context_data.has_key('board_form'))
        self.assertIsInstance(self.response.context_data['board_form'], BoardPositionForm)

    def test_redirect_if_not_logged(self):
        self.assertRedirectIfNotLogged()


class IssueDetailViewTest(IssueDetailDefaultTest):

    def setUp(self):
        super(IssueDetailViewTest, self).setUp()
        self.response = self.view(self.request, pk=self.issue.pk)

    def test_should_use_the_correctly_template(self):
        self.response = self.view(self.request, pk=self.issue.pk)
        self.assertIn('issues/issue_detail.html', self.response.template_name)


class IssueDetailAjaxViewTest(IssueDetailDefaultTest):
    ajax = True

    def test_should_use_the_correctly_template(self):
        self.response = self.view(self.request, pk=self.issue.pk)
        self.assertIn('issues/issue_detail_ajax.html', self.response.template_name)

