# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from tutorial.items import TutorialItem

class ExampleSpider(scrapy.Spider):
    name = "example"
    # allowed_domains = ["example.com"]
    # start_urls = ['http://example.com/']

    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        l  =ItemLoader(item = TutorialItem(), response = response)
        l.add_xpath('quote', '//span[@class=\'text\']/text()')
        l.add_css('author', 'span small::text')
        # l.add_css('tags', 'div.tags a.tag::text')
        return l.load_item()
