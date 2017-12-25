from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from random import choice
import os


class LinkFinder():
    def __init__(self, base_url, page_url):
        self.base_url = base_url
        self.page_url = page_url

    def __get_content(self):
        headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",  
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",  
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0", 
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"  
        ]

        req = Request(self.page_url)
        req.add_header("User-Agent", choice(headers))
        req.add_header("Host", "softs.fun")
        req.add_header("GET",self.page_url)

        return urlopen(req).read()

    def links(self):
        soup = BeautifulSoup(self.__get_content(), "html.parser")
        return [os.path.join(self.base_url, link.get('href')) \
                for link in soup.find_all('a', class_ = 'clearfix') \
                if 'https://' not in link.get('href')]


if __name__ == "__main__":
    linkfinder = LinkFinder(URL, URL)
    print(linkfinder.links())



