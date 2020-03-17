import os
import mock
import unittest
from crawler import Crawler

url = "http://www.google.com"


class CrawlerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.crawler = Crawler(url)
        self.crawler.startingUrl = url
        self.crawler.fileToSave = "TestCrawlerResults.csv"

    def test_getHtml(self):
        returnVal = self.crawler.getHtml(url)
        self.assertTrue(type(returnVal) == str)

    @mock.patch("crawler.Crawler.saveToFile", return_value=None)
    def test_saveLinks(self, mockSaveToFile):
        self.crawler.saveLinks(url)
        self.assertTrue(len(self.crawler.queue) > 0)

    def test_saveToFile(self):
        self.crawler.saveToFile("https:www.google.com", ["https://www.testURL.com", "https://www.some_test.com"])
        with open("TestCrawlerResults.csv", 'r') as f:
            reader = f.read()
            self.assertTrue(len(reader) > 0)

    # def test_crawl(self):

    @mock.patch("crawler.Crawler.crawl", return_value=None)
    def test_start(self, mockCrawl):
        self.crawler.start()
        self.assertEqual(len(self.crawler.queue), 1)

    # def tearDown(self) -> None:
    #     #os.remove(os.path.realpath("TestCrawlerResults.csv"))
    #     os.remove(os.path.realpath("/mnt/c/Users/Anvitha/PycharmProjects/WebCrawler/TestCrawlerResults.csv"))

##TODO fix test for crawl, relative path for deleting the test file, thread pool implementation
if __name__ == "__main__":

    unittest.main()
