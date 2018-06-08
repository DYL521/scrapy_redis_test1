# -*- coding: utf-8 -*-
import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/']

    def parse(self, response):
        pass
