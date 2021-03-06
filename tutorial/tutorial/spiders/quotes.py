import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # shorthand for start_requests with default implementation
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': response.xpath('//span[@class=\'text\']/text()').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    # """Run to save into json"""
    # scrapy crawl quotes -o quotes.json

    # """
    # This bit saves them pages to a new copy.
    # """
    # page = response.url.split("/")[-2]
    # filename = 'quotes-%s.html' % page
    # with open(filename, 'wb') as f:
    #     f.write(response.body)
    # self.log('Saved file %s' % filename)
