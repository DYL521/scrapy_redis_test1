# -*- coding: utf-8 -*-
import scrapy
import json


## 演示post
class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['fanyi.baidu.com']
    start_urls = ['http://fanyi.baidu.com/sug/'] ## post请求接口



    # scrapy.Request() ---- get
    # scrapy.FormRequest() --- post

    # 重写方法--实现post
    def start_requests(self):
        url = self.start_urls[0]
        form = {'kw':'世界'}
        ## callback -- 数据返回的后处理方式
        requset =  scrapy.FormRequest(url=url,formdata=form,callback=self.parse)
        yield requset ## 把请求返回给引擎，

    ## 自动调用
    def parse(self, response):
        ## 百度返回的是json数据
        text = response.text ##这里比括号
        data = json.loads(text,encoding='utf-8')
        print('------------------------')
        print(data)
        print('------------------------')


        yield data ## 返回给引擎