#coding:utf-8
import scrapy
import time
from scrapy.http import Request
from scrapy.selector import Selector
from ..items import TwitchFeaturedItem

class TwitchSpider(scrapy.Spider):
    name = 'twitch-spider'
    start_urls = [
        'https://sell.paipai.com/auction-list',
    ]

    def parse(self, response):
        # print response.request.benjamin
        try:
            open("111111.html", 'wb').write(response.body)

            item = TwitchFeaturedItem()
            nows = response.request.driver.find_elements_by_css_selector("[class='gl-i-wrap']")
            for now in nows[:]:
                item['source'] = now.find_element_by_xpath(".//div[@class='p-label']/span").text
                item['name'] = now.find_element_by_xpath(".//div[@class='p-name']").text
                # print item['name']
                item['href'] = now.find_element_by_xpath(".//div[@class='p-img']/a").get_attribute("href")
                item['sale_status'] = now.find_element_by_xpath(".//div[@class='p-time']/span[@class='desc']").text
                time__text = now.find_element_by_xpath(".//span[@class='time']").text
                if time__text.strip() == "":
                    item['hour'] = 0
                    item['minute'] = 0
                    item['second'] = 0
                else:
                    item['hour'] = now.find_element_by_xpath(".//span[@class='time']/b[1]").text
                    item['minute'] = now.find_element_by_xpath(".//span[@class='time']/b[2]").text
                    item['second'] = now.find_element_by_xpath(".//span[@class='time']/b[3]").text
                # item['sale_time'] = time__text
                item['url'] = response.request.driver.current_url
                yield item

            #找不到会抛异常，从而确定是不是最后一页
            text = response.request.driver.find_element_by_css_selector('li.active + li').text
            print ">>>>>>>>>>>"+text+"<<<<<<<<<<<<<<<<"
            response.request.driver.find_element_by_css_selector('li.active + li').click()
            url = response.request.driver.current_url
            response.request.driver.quit()
            print "**********************"+url+"***********************"
            yield Request(url, callback=self.parse)
        except Exception,e:
            response.request.driver.quit()
        finally:
            pass
            # response.request.driver.quit()
