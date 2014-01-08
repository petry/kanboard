from django.test import TestCase, RequestFactory
from model_mommy import mommy
from apps.core.forms import OnBoardForm
from apps.core.models import Story
from apps.core.views import StoryDetailView


class StoryDetailViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.story = mommy.make(Story)
        self.request = self.factory.get('/boards/1/')
        self.response = StoryDetailView.as_view()(self.request, pk=self.story.pk)

    def test_should_use_the_correctly_template(self):
        self.assertIn('core/story_detail.html', self.response.template_name)

    def test_shoul_have_board_form_on_context(self):
        self.assertTrue(self.response.context_data.has_key('board_form'))
        self.assertIsInstance(self.response.context_data['board_form'], OnBoardForm)