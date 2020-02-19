import scrapy
from scrapy.http import Request
from shanbei_spider.items import ShanbeiSpiderItem

class ShanbaySpider(scrapy.Spider):
    name = 'shanbay'
    allowed_domains = ['shanbay.com']
    # start_urls = ['http://shanbay.com/']

    def start_requests(self):
        for i in range(29):
            page = 540709 + i * 3
            url_base = 'https://www.shanbay.com/wordlist/187711/' + str(page) + '/?page={}'
            print url_base
            for x in range(10):
                url = url_base.format(x+ 1)
                print url
                yield Request(url,self.parse)

    def parse(self, response):
        html_contents = response.xpath('/html/body/div[3]/div/div[1]/div[2]/div/table/tbody/tr//*/text()')
        item = ShanbeiSpiderItem()

        for result in html_contents:
            item['Chinese'] = result.extract()
            print ">>>>>>"
            print item['Chinese']
            print "<<<<<<"
            yield item