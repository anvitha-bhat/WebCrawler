import unittest
from crawler import Crawler

url = "http://rescale.com"


class CrawlerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.crawler = Crawler(url)
        self.startingUrl = url
        #self.queue = collections.deque([])

    def test_getHtml(self):
        returnVal = self.crawler.getHtml("http://rescale.com")
        self.assertTrue(type(returnVal) == str)

    #def test_start(self):


if __name__ == "__main__":

    unittest.main()
