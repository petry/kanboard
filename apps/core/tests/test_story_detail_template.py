from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from mock import patch
from model_mommy import mommy
from lxml import html
from apps.core.models import Story, Step, BoardPosition
from apps.core.views import StoryDetailView

class StoryDetailViewTest(TestCase):
    urls = 'apps.core.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.story = mommy.make(Story)

        self.step2 = mommy.make(Step)
        self.step1 = mommy.make(Step, next=self.step2)

        self.request = self.factory.get('/storys/1/')


    def test_should_have_story_name_on_title(self):
        response = StoryDetailView.as_view()(self.request, pk=self.story.pk)
        dom = html.fromstring(response.rendered_content)
        title = dom.cssselect('.modal-dialog .modal-content h4.modal-title')[0]
        self.assertEqual(title.text, "Story #{0} - {1}".format(self.story.id, self.story.name) )

    def test_should_have_story_advance_link(self):
        mommy.make(BoardPosition, story=self.story, status=self.step1)
        response = StoryDetailView.as_view()(self.request, pk=self.story.pk)
        dom = html.fromstring(response.rendered_content)
        link = dom.cssselect('.modal-dialog .modal-content .modal-footer a.btn.btn-primary')[0]

        self.assertEqual(link.attrib['href'], reverse("story-advance", kwargs={"pk": self.story.id}))
        self.assertEqual(link.text, "To {0}".format(self.step2.name))

    def test_not_have_step_link_when_is_on_final_step(self):
        mommy.make(BoardPosition, story=self.story, status=self.step2)
        response = StoryDetailView.as_view()(self.request, pk=self.story.pk)
        dom = html.fromstring(response.rendered_content)
        link = dom.cssselect('.modal-dialog .modal-content .modal-footer')[0]
        self.assertEqual(link.text.lstrip(), "")

    def test_not_have_step_link_when_story_are_not_in_any_board(self):
        response = StoryDetailView.as_view()(self.request, pk=self.story.pk)
        dom = html.fromstring(response.rendered_content)
        link = dom.cssselect('.modal-dialog .modal-content .modal-footer')[0]
        self.assertEqual(link.text.lstrip(), "")

