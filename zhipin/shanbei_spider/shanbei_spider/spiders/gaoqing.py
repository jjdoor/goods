import scrapy
from scrapy.http import Request
from shanbei_spider.items import ShanbeiSpiderItem

class ShanbaySpider(scrapy.Spider):
    name = 'gaoqing'
    allowed_domains = ['gaoqing.la']
    start_urls = ['http://gaoqing.la/3d']

    # def start_requests(self):
    #     for i in range(29):
    #         page = 540709 + i * 3
    #         url_base = 'https://www.shanbay.com/wordlist/187711/' + str(page) + '/?page={}'
    #         print url_base
    #         for x in range(10):
    #             url = url_base.format(x+ 1)
    #             print url
    #             yield Request(url,self.parse)

    def parse(self, response):
        # html_contents = response.xpath('//a')
        html_contents = response.xpath('//ul/li/div/div/h2/a')
        item = ShanbeiSpiderItem()

        for result in html_contents:
            item['Chinese'] = result.xpath("./text()").extract()
            item['a'] = result.xpath("./@href").extract()
            print ">>>>>>"
            print item['Chinese']
            print "<<<<<<"
            yield item