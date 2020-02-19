# -*- coding: utf-8 -*-
import scrapy


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['image.baidu.com']
    start_urls = ['http://image.baidu.com/']

    def parse(self, response):
        pass
