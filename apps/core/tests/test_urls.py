from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import TestCase
from model_mommy import mommy
from apps.core.models import Board


class UrlsTest(TestCase):


    def setUp(self):
        super(UrlsTest, self).setUp()

    def assertUrlExist(self, name, kwargs={}):
        try:
            reverse(name, kwargs=kwargs)
        except NoReverseMatch:
            self.fail("Reversal of url named '{0}' failed with NoReverseMatch".format(name))

    def test_board_listl_url(self):
        self.assertUrlExist('board-list')

    def test_board_detail_url(self):
        self.assertUrlExist('board-detail', {'pk': 1})

    def test_story_detail_url(self):
        self.assertUrlExist('story-detail', {'pk': 1})

    def test_story_detail_url(self):
        self.assertUrlExist('story-advance', {'pk': 1})
