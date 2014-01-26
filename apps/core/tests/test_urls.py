from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import TestCase


class UrlsTest(TestCase):

    def assertUrlExist(self, name, kwargs={}):
        try:
            reverse(name, kwargs=kwargs)
        except NoReverseMatch:
            self.fail("Reversal of url named '{0}' failed with NoReverseMatch".format(name))


class CoreUrlsTest(UrlsTest):

    def test_board_list_url(self):
        self.assertUrlExist('board-list')

    def test_login_url(self):
        self.assertUrlExist('core-login')

    def test_logout_url(self):
        self.assertUrlExist('core-logout')