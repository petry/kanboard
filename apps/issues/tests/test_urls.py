from apps.core.tests.test_urls import UrlsTest


class IssuesUrlsTest(UrlsTest):

    def test_issue_detail_url(self):
        self.assertUrlExist('issue-detail', {'pk': 1})

    def test_issue_advance_url(self):
        self.assertUrlExist('issue-advance', {'pk': 1})

    def test_issue_on_board_url(self):
        self.assertUrlExist('issue-onboard', {'pk': 1})
