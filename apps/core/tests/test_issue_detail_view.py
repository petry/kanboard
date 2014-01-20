from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.core.forms import BoardPositionForm
from apps.core.models import Issue
from apps.core.views import IssueDetailView


class IssueDetailViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.issue = mommy.make(Issue)
        self.request = self.factory.get('/boards/1/')
        self.response = IssueDetailView.as_view()(self.request, pk=self.issue.pk)

    def test_should_use_the_correctly_template(self):
        self.assertIn('core/issue_detail.html', self.response.template_name)

    def test_should_have_board_form_on_context(self):
        self.assertTrue(self.response.context_data.has_key('board_form'))
        self.assertIsInstance(self.response.context_data['board_form'], BoardPositionForm)