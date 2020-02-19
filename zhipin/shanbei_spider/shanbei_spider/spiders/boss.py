# -*- coding: utf-8 -*-
import scrapy
# from scrapy import Request
from scrapy_splash import SplashRequest
from ..items import BosssplashItem

lua_script = '''
function main(splash, args)
   splash.images_enabled = false
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
    name = 'boss'
    # allowed_domains = ['search.jd.com']
    # start_urls = ['https://www.zhipin.com/c101210100/?query=php']
    # start_urls = ['https://www.zhipin.com/c101210100/?query=php&period=4&page=1&ka=page-1']
    start_urls = ['https://www.zhipin.com/c101190200/?query=php&page=1&ka=page-1']

    def start_requests(self):
        #进入搜索页进行搜索
        for each in self.start_urls:
            yield SplashRequest(each,callback=self.parse,endpoint='execute',
                 args={'lua_source': lua_script})

    def parse(self, response):
        filename = response.url.split("/")[-1]+'.html'
        open(filename, 'wb').write(response.body)

        item = BosssplashItem()
        work = response.css('div.job-primary div.info-primary h3.name div.job-title::text').getall()
        price = response.css('div.job-primary div.info-primary h3.name span.red::text').getall()
        address = response.xpath("//div[@class='job-primary']//div[@class='info-primary']").xpath('string(.//p)').getall()
        co = response.css('div.info-company div.company-text h3.name').xpath('string(.//a)').getall()
        number = response.css('div.info-company div.company-text').xpath('string(.//p)').getall()
        # price = response.css('div.gl-i-wrap div.p-price i::text').getall()
        # page_num = response.xpath("//span[@class= 'p-num']/a[last()-1]/text()").get()
        # page_num = response.xpath("//span[@class='p-skip']/em/b/text()").get()
        # page_num = response.xpath("//span[@class='p-skip']/em/b/text()").get()
        #这里使用了 xpath 函数 fn:string(arg):返回参数的字符串值。参数可以是数字、逻辑值或节点集。
        #可能这就是 xpath 比 css 更精致的地方吧
        # name = response.css('div.gl-i-wrap div.p-name').xpath('string(.//em)').getall()
        #comment = response.css('div.gl-i-wrap div.p-commit').xpath('string(.//strong)').getall()
        # comment = response.css('div.gl-i-wrap div.p-commit strong a::text').getall()
        # publishstore = response.css('div.gl-i-wrap div.p-shopnum a::attr(title)').getall()
        href = [response.urljoin(i) for i in response.css('div.job-primary div.info-primary h3.name a::attr(href)').getall()]
        for each in zip(work, price, address, co,href,number):
            item['work'] = each[0]
            item['price'] = each[1]
            item['address'] = each[2]
            item['co'] = each[3]
            item['href'] = each[4]
            item['number'] = each[5]
            yield item

        # javascript:;
        href = response.css('div.job-list div.page a:last-child::attr(href)').extract_first()
        if href != 'javascript:;':
            yield SplashRequest(response.urljoin(href), callback=self.s_parse, endpoint='execute',
                                args={'lua_source': lua_script2})
        #这里从第二页开始
        # url = 'https://search.jd.com/Search?keyword=python3.7&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=%d&s=%d&click=0'
        # url = 'https://www.zhipin.com/c101210100/?query=python&page=%d&ka=page-%d'
        # url = 'https://www.zhipin.com/c101210100/?query=php&page=%d&ka=page-%d'
        # url = 'https://www.zhipin.com/c101020100/?query=php&period=4&page=%d&ka=page-%d'
        # url = 'https://www.zhipin.com/c101210100/?query=php&period=4&page=%d&ka=page-%d'
        # url = 'https://www.zhipin.com/c101210100/?query=php&period=4&page=%d&ka=page-%d'
        # url = 'https://www.zhipin.com/c101190200/?query=php&page=%d&ka=page-%d'
        # for each_page in range(1,10):
        #     yield SplashRequest(url%(each_page,each_page),callback=self.s_parse,endpoint='execute',
        #         args={'lua_source': lua_script2})

    def s_parse(self, response):
        filename = response.url.split("/")[-1]+'.html'
        open(filename, 'wb').write(response.body)
        item = BosssplashItem()
        work = response.css('div.job-primary div.info-primary h3.name div.job-title::text').getall()
        price = response.css('div.job-primary div.info-primary h3.name span.red::text').getall()
        address = response.xpath("//div[@class='job-primary']//div[@class='info-primary']").xpath('string(.//p)').getall()
        co = response.css('div.info-company div.company-text h3.name').xpath('string(.//a)').getall()
        href = [response.urljoin(i) for i in response.css('div.job-primary div.info-primary h3.name a::attr(href)').getall()]
        for each in zip(work, price, address, co, href):
            item['work'] = each[0]
            item['price'] = each[1]
            item['address'] = each[2]
            item['co'] = each[3]
            item['href'] = each[4]
            yield item

        # javascript:;
        href = response.css('div.job-list div.page a:last-child::attr(href)').extract_first()
        if href != 'javascript:;':
            yield SplashRequest(response.urljoin(href), callback=self.s_parse, endpoint='execute',
                                args={'lua_source': lua_script2})