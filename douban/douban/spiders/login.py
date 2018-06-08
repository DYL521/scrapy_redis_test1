# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import urllib
from PIL import Image

class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://accounts.douban.com/login']

    ## 模拟登陆
    ## 第一步get请求-- 获得验证码
    ## 根据验证码--- 发起post请求

    def parse(self, response):
        captcha_url = response.xapth('//img[@id="captcha_image"]/@src').extract_first()

        ## 没有验证码
        if not captcha_url:
            pass
            form = {'email': '1767932904',
                    'passwd': '106207.123'}
        else:  # 有验证码
            urllib.request.urlretrieve(captcha_url, './captcha.png')
            Image.open('./captcha.png').show()

            code = input('请输入验证码：')
            username = '17679329004'
            pwd = '106207.123'
            form = {
                'email': username,
                'passwd': pwd,
                'captcha': code
            }
