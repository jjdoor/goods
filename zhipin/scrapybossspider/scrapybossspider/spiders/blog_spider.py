# -*- coding: utf-8 -*-
from datetime import date,timedelta
import scrapy
from requests import Request
# from scrapy.spiders import Spider

today = date.today()


class ToutiaoItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()


class BlogSpider(scrapy.Spider):
    name = 'scrapybossspider'

    # start_urls = [f"https://toutiao.io/prev/today - timedelta(days=i)"
    #               for i in range(5)]

    start_urls = ['http://www.baidu.com']
    def parse(self, response):
        # crawler.settings.get
        page = 1
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        for post in response.xpath('//h3[@class="title"]/a'):
            item = ToutiaoItem()
            item['title'] = post.xpath('@title').extract_first()
            item['link'] = post.xpath('@href').extract_first()
            yield item

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)
    #
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)
