from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from lxml import html
from apps.core.models import Issue, Step, BoardPosition
from apps.core.views import IssueDetailView


class IssueDetailViewTest(TestCase):
    urls = 'apps.core.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.issue = mommy.make(Issue)
        self.step2 = mommy.make(Step)
        self.step1 = mommy.make(Step, next=self.step2)
        self.request = self.factory.get('/issue/1/')

    def test_should_have_issue_name_on_title(self):
        response = IssueDetailView.as_view()(self.request, pk=self.issue.pk)
        dom = html.fromstring(response.rendered_content)
        title = dom.cssselect('.modal-dialog .modal-content h4.modal-title')[0]
        self.assertEqual(title.text, "Issue #{0} - {1}".format(self.issue.id, self.issue.name))

    def test_should_have_issue_advance_link(self):
        mommy.make(BoardPosition, issue=self.issue, status=self.step1)
        response = IssueDetailView.as_view()(self.request, pk=self.issue.pk)
        dom = html.fromstring(response.rendered_content)
        link = dom.cssselect('.modal-dialog .modal-content .modal-footer a.btn.btn-primary')[0]

        self.assertEqual(link.attrib['href'], reverse("issue-advance", kwargs={"pk": self.issue.id}))
        self.assertEqual(link.text, "To {0}".format(self.step2.name))

    def test_not_have_step_link_when_is_on_final_step(self):
        mommy.make(BoardPosition, issue=self.issue, status=self.step2)
        response = IssueDetailView.as_view()(self.request, pk=self.issue.pk)
        dom = html.fromstring(response.rendered_content)
        link = dom.cssselect('.modal-dialog .modal-content .modal-footer')[0]
        self.assertEqual(link.text.lstrip(), "")

    def test_not_have_step_link_when_issue_are_not_in_any_board(self):
        response = IssueDetailView.as_view()(self.request, pk=self.issue.pk)
        dom = html.fromstring(response.rendered_content)
        link = dom.cssselect('.modal-dialog .modal-content .modal-footer')[0]
        self.assertEqual(link.text.lstrip(), "")
