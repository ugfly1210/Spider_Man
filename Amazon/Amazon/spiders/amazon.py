# -*- coding: utf-8 -*-
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon' # 爬虫名字。必须要跟爬的网站名相关
    allowed_domains = ['amazon.cn'] # 只能爬取这个，或者子域
    start_urls = ['http://amazon.cn/']  # 默认爬取的url

    def start_requests(self):
        print(self.start_urls[0])
        yield scrapy.Request(self.start_urls[0],callback=self.parse)

    def parse(self, response):
        print('111')
        pass
