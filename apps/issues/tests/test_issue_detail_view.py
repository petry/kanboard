from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.boards.forms import BoardPositionForm
from apps.issues.models import Issue
from apps.issues.views import IssueDetailView


class IssueDetailDefaultTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.issue = mommy.make(Issue)
        self.request = self.factory.get('/boards/1/')

    def test_should_have_board_form_on_context(self):
        self.response = IssueDetailView.as_view()(self.request, pk=self.issue.pk)
        self.assertTrue(self.response.context_data.has_key('board_form'))
        self.assertIsInstance(self.response.context_data['board_form'], BoardPositionForm)



class IssueDetailViewTest(IssueDetailDefaultTest):

    def setUp(self):
        self.factory = RequestFactory()
        self.issue = mommy.make(Issue)
        self.request = self.factory.get('/boards/1/')
        self.response = IssueDetailView.as_view()(self.request, pk=self.issue.pk)

    def test_should_use_the_correctly_template(self):
        self.response = IssueDetailView.as_view()(self.request, pk=self.issue.pk)
        self.assertIn('issues/issue_detail.html', self.response.template_name)


class IssueDetailAjaxViewTest(IssueDetailDefaultTest):

    def setUp(self):
        self.factory = RequestFactory()
        self.issue = mommy.make(Issue)
        self.request = self.factory.get('/boards/1/', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

    def test_should_use_the_correctly_template(self):
        self.response = IssueDetailView.as_view()(self.request, pk=self.issue.pk)
        self.assertIn('issues/issue_detail_ajax.html', self.response.template_name)


