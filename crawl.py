# 安装bs4
# https://stackoverflow.com/questions/12228102/how-to-install-beautiful-soup-4-with-python-2-7-on-windows
# 如果你装的python是3.x版本，用pip或者其他工具下载应该默认和你的python版本匹配
# bs4的文档
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
from bs4 import BeautifulSoup
from urllib.request import urlopen

# URL = 'https://doub.bid'
# 先爬这个站点
# 这是个基础URL
URL = "https://softs.fun"


# Steps
# 1.crawl the urls in first page and save
# 2.crawl the urls of first page one by one, and save as second page urls
# 3.till no more next page


# https://docs.python.org/3/library/__main__.html
# 如果从终端运行该文件才会调用， 其他python文件引用的情况下不调用
if __name__ == "__main__":
    response = urlopen(URL)
    html_doc = response.read().decode('utf-8')
    print(html_doc)
    soup = BeautifulSoup(html_doc)
    print(soup.prettify())