# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_splash import SplashRequest
from ..items import JdsplashItem

lua_script = '''
function main(splash, args)
   splash.images_enabled = false
   splash:set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
   assert(splash:go(args.url))
   splash:wait(0.5)
   local input = splash:select("#keyword")
   input:send_text('python3.7')
   splash:wait(0.5)
   local form = splash:select('.input_submit')
   form:click()
   splash:wait(2)
   splash:runjs("document.getElementsByClassName('bottom-search')[0].scrollIntoView(true)")
   splash:wait(6)
   return splash:html()
 end
'''

lua_script2 = '''
 function main(splash, args)
   splash.images_enabled = false
   splash:set_user_agent('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36')
   assert(splash:go(args.url))
   splash:wait(2)
   splash:runjs("document.getElementsByClassName('bottom-search')[0].scrollIntoView(true)")
   splash:wait(6)
   return splash:html()
 end
'''

class JdBookSpider(scrapy.Spider):
    name = 'jdbook'
    allowed_domains = ['search.jd.com']
    start_urls = ['https://search.jd.com']

    def start_requests(self):
        #进入搜索页进行搜索
        for each in self.start_urls:
            yield SplashRequest(each,callback=self.parse,endpoint='execute',
                 args={'lua_source': lua_script})

    def parse(self, response):
        item = JdsplashItem()
        price = response.css('div.gl-i-wrap div.p-price i::text').getall()
        page_num = response.xpath("//span[@class= 'p-num']/a[last()-1]/text()").get()
        page_num = response.xpath("//span[@class='p-skip']/em/b/text()").get()
        #这里使用了 xpath 函数 fn:string(arg):返回参数的字符串值。参数可以是数字、逻辑值或节点集。
        #可能这就是 xpath 比 css 更精致的地方吧
        name = response.css('div.gl-i-wrap div.p-name').xpath('string(.//em)').getall()
        #comment = response.css('div.gl-i-wrap div.p-commit').xpath('string(.//strong)').getall()
        comment = response.css('div.gl-i-wrap div.p-commit strong a::text').getall()
        publishstore = response.css('div.gl-i-wrap div.p-shopnum a::attr(title)').getall()
        href = [response.urljoin(i) for i in response.css('div.gl-i-wrap div.p-img a::attr(href)').getall()]
        for each in zip(name, price, comment, publishstore,href):
            item['name'] = each[0]
            item['price'] = each[1]
            item['comment'] = each[2]
            item['p_store'] = each[3]
            item['href'] = each[4]
            yield item
        #这里从第二页开始
        url = 'https://search.jd.com/Search?keyword=python3.7&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=%d&s=%d&click=0'
        for each_page in range(1,int(page_num)):
            yield SplashRequest(url%(each_page*2+1,each_page*60),callback=self.s_parse,endpoint='execute',
                args={'lua_source': lua_script2})

    def s_parse(self, response):
        item = JdsplashItem()
        price = response.css('div.gl-i-wrap div.p-price i::text').getall()
        name = response.css('div.gl-i-wrap div.p-name').xpath('string(.//em)').getall()
        comment = response.css('div.gl-i-wrap div.p-commit strong a::text').getall()
        publishstore = response.css('div.gl-i-wrap div.p-shopnum a::attr(title)').getall()
        href = [response.urljoin(i) for i in response.css('div.gl-i-wrap div.p-img a::attr(href)').getall()]
        for each in zip(name, price, comment, publishstore, href):
            item['name'] = each[0]
            item['price'] = each[1]
            item['comment'] = each[2]
            item['p_store'] = each[3]
            item['href'] = each[4]
            yield item