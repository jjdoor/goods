# -*- coding: utf-8 -*-
import scrapy
# from scrapy import Request
from scrapy_splash import SplashRequest
from ..items import BosssplashItem

lua_script = '''
function main(splash, args)
   splash.images_enabled = true
   splash:set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
   assert(splash:go(args.url))
   splash:wait(5)
   return splash:html()
 end
'''

lua_script2 = '''
 function main(splash, args)
   splash.images_enabled = false
   splash:set_user_agent('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36')
   assert(splash:go(args.url))
   splash:wait(5)
   return splash:html()
 end
'''

class BossSpider(scrapy.Spider):
    name = 'duobaodao'
    # allowed_domains = ['search.jd.com']
    # start_urls = ['https://www.zhipin.com/c101210100/?query=php']
    # start_urls = ['https://www.zhipin.com/c101210100/?query=php&period=4&page=1&ka=page-1']
    start_urls = ['https://www.jd.com/']

    def start_requests(self):
        #进入搜索页进行搜索
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,
                                args={'wait': 30.5, 'viewport': '1024x2480', 'timeout': 90, 'images': 0, 'resource_timeout': 30}, endpoint='render.html')
        # for each in self.start_urls:
        #     yield SplashRequest(each,callback=self.parse,endpoint='execute',
        #          args={'lua_source': lua_script})

    def parse(self, response):
        open("111111.html", 'wb').write(response.body)
        # titele = response.xpath('//div[@class="row row-2 title"]/a/text()').extract()
        # print('这是标题：', titele)

    def parse1(self, response):
        filename = response.url.split("/")[-1]+'.html'
        open("111111.html", 'wb').write(response.body)
        print "0000000000000000000000000000000000000"