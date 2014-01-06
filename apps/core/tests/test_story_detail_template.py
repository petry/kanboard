from django.test import TestCase, RequestFactory
from model_mommy import mommy
from lxml import html
from apps.core.models import Story, Step
from apps.core.views import StoryDetailView

class StoryDetailViewTest(TestCase):
    urls = 'apps.core.urls'

    def setUp(self):
        self.factory = RequestFactory()
        self.story = mommy.make(Story)
        self.request = self.factory.get('/storys/1/')

        response = StoryDetailView.as_view()(self.request, pk=self.story.pk)
        self.dom = html.fromstring(response.rendered_content)

    def test_should_have_story_name_on_title(self):
        title = self.dom.cssselect('.modal-dialog .modal-content h4.modal-title')[0]
        self.assertEqual(title.text, "Story #{0} - {1}".format(self.story.id, self.story.name) )

