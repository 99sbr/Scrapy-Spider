#!/usr/bin/env python
import requests
import urllib
from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class Spider:
    # class variable which is shared among all instances
    project_name=''
    base_url=''
    domain_name=''
    queue_file=''
    crawled_file=''
    queue=set()
    crawled=set()
    def __init__(self,project_name,base_url):
        Spider.projct_name=project_name
        Spider.base_url=base_url
        Spider.domain_name=domain_name
        Spider.queue_file=Spider.projct_name + '/queue.txt'
        Spider.crawled=Spider.projct_name + '/crawled.txt'
        self.boot()
        self.crawled_page('First Spider',Spider.base_url)
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.projct_name, Spider.base_url)
        Spider.queue=file_to_set(Spider.crawled_file)
    
    @staticmethod
    def crawled_page(thread_name, page_url):
        if page_url not in  Spider.crawled:
            print(thread_name +'crawling' + page_url)
            print('Queue' + str(len(Spider.queue) + '| Crawled' + str(len(Spider.crawled))))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
            
    @staticmethod
    def gather_links(page_url):
        html_string=''
        # anytime we are working with networking type of stuff we always put it in try except stuff
        try:
            response = urlopen(page_url) # helps to connect to web page
            if response.getheader('Content-Type')=='text/html':
                html_bytes=response.read()
                html_string=html_bytes.decode('utf-8')
            finder=LinkFinder(Spider.base_url,page_url)
            finder.feed(html_string)
        except:
            print(" Error !! Cannot crawl page")
            return set()
        return finder.page_links()
            