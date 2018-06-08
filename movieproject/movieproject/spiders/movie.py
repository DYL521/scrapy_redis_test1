# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieprojectItem

## 先使用scrapy，再使用scrapy_redis

class MovieSpider(scrapy.Spider):
    name = 'movie'  ## redis保存的文件夹名字叫movie
    allowed_domains = ['www.dy2018.com']
    start_urls = ['https://www.dy2018.com/0/']

    def parse(self, response):

        tables = response.xpath('//table[@class="tbspan"]') ## 直接找tabl
        for t in tables:
            item = MovieprojectItem()

            ##获取电影名
            ## 电影介绍
            title =  t.xpath('.//tr[2]//a[2]/text()').extract()[0]
            info = ''.join(t.xpath('.//tr[4]//p/text()').extract()).replace('\u3000','') ## 列表直接平成字符串
            # info =  info.replace('\u3000','') ##info.replace('\u3000','')##  \u3000代表中文空格
            item['title'] = title
            item['info'] = info
            yield item



