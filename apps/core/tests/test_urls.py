from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import TestCase


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

    def test_board_report_url(self):
        self.assertUrlExist('board-report', {'pk': 1})

    def test_issue_detail_url(self):
        self.assertUrlExist('issue-detail', {'pk': 1})

    def test_issue_advance_url(self):
        self.assertUrlExist('issue-advance', {'pk': 1})

    def test_issue_on_board_url(self):
        self.assertUrlExist('issue-onboard', {'pk': 1})
