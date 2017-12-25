from general import *
from link_finder import LinkFinder

class Spider:
    project_name = ""
    base_url = ""
    queue_file = ""
    crawled_file = ""
    finish_file = ""

    queue = set()
    crawled = set()
    finish = set()

    def __init__(self, project_name, base_url):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.queue_file = project_name + '/queue.txt'
        Spider.crawled_file = project_name + '/crawled.txt'
        Spider.finish_file = project_name + '/finish.txt'

        self.boot()

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name,Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
        Spider.finish = file_to_set(Spider.finish_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if (page_url not in (Spider.crawled | Spider.finish)):
            finder = LinkFinder(Spider.base_url, page_url)
            Spider.add_links_to_queue_finish(finder.links())
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()


    @staticmethod
    def add_links_to_queue_finish(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled) or (url in Spider.finish):
                continue

            if '?dir=' in url:
                Spider.queue.add(url)
            else:
                Spider.finish.add(url)


    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
        set_to_file(Spider.finish, Spider.finish_file)