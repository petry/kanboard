from django.core.urlresolvers import reverse
from model_mommy import mommy
from apps.boards.forms import BoardPositionForm
from apps.core.tests.utils import LoggedTestCase
from apps.issues.models import Issue
from apps.issues.views import IssueCreateView


class IssueCreateDefaultTest(LoggedTestCase):
    def get_view(self):
        return IssueCreateView.as_view()

    def setUp(self):
        super(IssueCreateDefaultTest, self).setUp()

    def test_redirect_if_not_logged(self):
        self.assertRedirectIfNotLogged()

class IssueCreateViewTest(IssueCreateDefaultTest):

    def setUp(self):
        super(IssueCreateViewTest, self).setUp()
        self.response = self.view(self.request)

    def test_should_use_the_correctly_template(self):
        self.response = self.view(self.request)
        self.assertIn('issues/issue_form.html', self.response.template_name)


class IssueCreateAjaxViewTest(IssueCreateDefaultTest):
    ajax = True

    def test_should_use_the_correctly_template(self):
        self.response = self.view(self.request)
        self.assertIn('issues/issue_form_ajax.html', self.response.template_name)


class IssueCreatePostTest(IssueCreateDefaultTest):
    def setUp(self):
        super(IssueCreatePostTest, self).setUp()
        self.request = self.factory.post('/some-url/',
                                         {'name': 'created issue',
                                          'description': 'issue description'})
        self.request.user = self.user
        self.request.session = {}

    def test_should_create_an_issue(self):
        self.assertEqual(Issue.objects.all().count(), 0)
        self.response = self.view(self.request)
        self.assertEqual(Issue.objects.all().count(), 1)

    def test_should_redirect_to_board_when_created(self):
        self.response = self.view(self.request)
        self.assertEqual(self.response.url, reverse('board-list'))