#coding:utf-8
import scrapy
import time
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import TwitchFeaturedItem

class TwitchSpider(scrapy.Spider):
    name = 'twitch-spider_bak'
    start_urls = [
        'https://sell.paipai.com/auction-list',
    ]

    def parse(self, response):
        print response.request.benjamin
        try:
            open("111111.html", 'wb').write(response.body)
            for num in range(2000):
                #找不到会抛异常，从而确定是不是最后一页
                text = response.request.driver.find_element_by_css_selector('li.active + li').text
                # if(text)
                print ">>>>>>>>>>>"+text+"<<<<<<<<<<<<<<<<"
                response.request.driver.find_element_by_css_selector('li.active + li').click()
                # response.request.driver.find_elements_by_class_name("number")[text-1].click()
                time.sleep(2)
                source1 = response.request.driver.page_source
                open(text+".html", 'wb').write(source1.encode("utf-8"))
                # self.parse_detail(response)
                item = TwitchFeaturedItem()
                nows = response.request.driver.find_elements_by_css_selector("[class='gl-i-wrap']")
                for now in nows[:]:
                    # 价格
                    # t = now.text
                    # x = now.find_element_by_css_selector('[class="p-price"]').text
                    item['source'] = now.find_element_by_xpath(".//div[@class='p-label']/span").text
                    # print "[[[[[[[[[[[[[[[[[[[[[" + source + "]]]]]]]]]]]]]]]]]]]]]]]]"
                    item['name'] = now.find_element_by_xpath(".//div[@class='p-name']").text
                    # print "[[[[[[[[[[[[[[[[[[[[[" + name + "]]]]]]]]]]]]]]]]]]]]]]]]"
                    item['href'] = now.find_element_by_xpath(".//div[@class='p-img']/a").get_attribute("href")
                    # print "[[[[[[[[[[[[[[[[[[[[[" + href + "]]]]]]]]]]]]]]]]]]]]]]]]"
                    item['time'] = now.find_element_by_xpath(".//span[@class='time']").text
                    # print "[[[[[[[[[[[[[[[[[[[[[" + time + "]]]]]]]]]]]]]]]]]]]]]]]]"
                    item['url'] = response.request.driver.current_url
                    yield item
                # response.request.driver.quit()
        finally:
            response.request.driver.quit()
        # streamer = response.xpath('//p[@data-a-target="carousel-broadcaster-displayname"]/text()').extract()
        # playing = response.xpath('//p[@data-a-target="carousel-user-playing-message"]/span/a/text()').extract()
        #
        # yield {
        #     'streamer': streamer,
        #     'playing': playing
        # }
    def parse_detail(self,response):
        # pass TwitchFeaturedItem
        item = TwitchFeaturedItem()
        nows = response.request.driver.find_elements_by_css_selector("[class='gl-i-wrap']")
        for now in nows[:]:
            # 价格
            # t = now.text
            # x = now.find_element_by_css_selector('[class="p-price"]').text
            item['source'] = now.find_element_by_xpath(".//div[@class='p-label']/span").text
            # print "[[[[[[[[[[[[[[[[[[[[[" + source + "]]]]]]]]]]]]]]]]]]]]]]]]"
            item['name'] = now.find_element_by_xpath(".//div[@class='p-name']").text
            # print "[[[[[[[[[[[[[[[[[[[[[" + name + "]]]]]]]]]]]]]]]]]]]]]]]]"
            item['href'] = now.find_element_by_xpath(".//div[@class='p-img']/a").get_attribute("href")
            # print "[[[[[[[[[[[[[[[[[[[[[" + href + "]]]]]]]]]]]]]]]]]]]]]]]]"
            item['time'] = now.find_element_by_xpath(".//span[@class='time']").text
            # print "[[[[[[[[[[[[[[[[[[[[[" + time + "]]]]]]]]]]]]]]]]]]]]]]]]"
            yield item