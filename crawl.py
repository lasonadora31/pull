# 安装bs4
# https://stackoverflow.com/questions/12228102/how-to-install-beautiful-soup-4-with-python-2-7-on-windows
# 如果你装的python是3.x版本，用pip或者其他工具下载应该默认和你的python版本匹配
# bs4的文档
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from random import choice

# URL = 'https://doub.bid'
# 先爬这个站点
# 这是个基础URL
URL = "https://softs.fun"

# Steps
# 1.crawl the urls in first page and save
# 2.crawl the urls of first page one by one, and save as second page urls
# 3.till no more next page

def get_content(url):
    headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",  
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",  
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",  
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"  
    ]

    req = Request(url)
    req.add_header("User-Agent", choice(headers))
    req.add_header("Host", "softs.fun")
    req.add_header("GET",url)

    return urlopen(req).read()

def get_soup_object(url, parser="html.parser"):
    return BeautifulSoup(get_content(url), parser)

def next_link(soup):
    return [link.get('href') for link in \
            soup.find_all('a', class_ = 'clearfix')]

if __name__ == "__main__":
    print(next_link(get_soup_object(URL)))



