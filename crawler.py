import re
import sys
import csv
import requests
import collections
from urllib.parse import urlparse


class Crawler(object):

    def __init__(self, startingUrl):
        self.startingUrl = startingUrl
        self.queue = collections.deque([])
        # self.visited = set() #visited will handle duplicate urls among different pages

    def getHtml(self, url):
        try:
            html = requests.get(url)
        except Exception as e:
            print(e)
            return ""
        return html.content.decode('latin-1')

    def saveLinks(self, url):
        html = self.getHtml(url)
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        links = list(set([link for link in re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', html) if link.startswith("http")]))
        for link in links:
            self.queue.append(link)
            print("  ", link)
        self.saveToFile(url, links)

    def saveToFile(self, url, links):
        with open('quotes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(url)
            for link in links:
                row = ["", link]
                writer.writerow(row)

    def crawl(self, url):
        print(url)
        while len(self.queue) > 0:
            link = self.queue.popleft()
            self.saveLinks(url)
            # if link in self.visited:
            #     continue
            # self.visited.add(link)
            self.crawl(link)

    def start(self):
        self.queue.append(self.startingUrl)
        self.crawl(self.startingUrl)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Incorrect input found, try again.. Expected run command - 'python crawler.py http://google.com'")
        quit()
    #crawler = Crawler("http://www.rescale.com") #test
    crawler = Crawler(sys.argv[1])
    crawler.start()