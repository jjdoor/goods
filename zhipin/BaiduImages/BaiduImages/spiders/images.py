# -*- coding: utf-8 -*-
from scrapy import Spider, Request
# from urllib.parse import quote
import urllib
from ..items import BaiduimagesItem
# from BaiduImages.items import BaiduimagesItem
import json


class ImagesSpider(Spider):
    name = 'images'
    allowed_domains = ['images.baidu.com']
    start_urls = ['https://images.baidu.com/']

    def parse(self, response):
        images = json.loads(response.body)['data']
        for image in images:
            item = BaiduimagesItem()
            try:
                item['url'] = image.get('thumbURL')
                yield item
            except Exception as e:
                print(e)
        pass

    def start_requests(self):
        data = {'queryWord': '女生标准照', 'word': '女生标准照'}
        base_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['pn'] = page * 30
            url = base_url + urllib.quote(data['queryWord']) + '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=' + \
                  urllib.quote(data['word']) + '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&pn=' + \
                  urllib.quote(str(data['pn'])) + '&rn=30&gsm=' + str(hex(data['pn']))
            yield Request(url, self.parse)