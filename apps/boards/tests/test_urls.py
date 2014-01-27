from apps.core.tests.test_urls import UrlsTest

class BoardsUrlsTest(UrlsTest):

    def test_board_index_url(self):
        self.assertUrlExist('index')

    def test_board_detail_url(self):
        self.assertUrlExist('board-detail', {'pk': 1})

    def test_board_report_url(self):
        self.assertUrlExist('board-report', {'pk': 1})

