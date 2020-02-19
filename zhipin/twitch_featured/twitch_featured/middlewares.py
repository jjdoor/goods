# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1200x600')
#
# driver = webdriver.Chrome(chrome_options=options)


from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')
# chrome_options.add_argument('window-size=1200x6000')
# driver = webdriver.Remote(command_executor='http://192.168.33.133:4444/wd/hub',
#                           desired_capabilities = chrome_options.to_capabilities())


class TwitchFeaturedSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TwitchFeaturedDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        driver = webdriver.Remote(command_executor='http://192.168.33.133:4444/wd/hub',
                                  desired_capabilities=chrome_options.to_capabilities())
        url_ = request.url[8:36]
        if url_ != 'sell.paipai.com/auction-list':
            return None
        # if request.url != 'https://sell.paipai.com/auction-list':
        #     return None
        # driver.set_page_load_timeout(30)
        # print ">>>>>>>>>>>>>>>>>>"+request.url+"<<<<<<<<<<<<<<<<"
        try:
            driver.set_page_load_timeout(60)
            driver.set_script_timeout(60)
            driver.get(request.url)
            body = driver.page_source
            url = driver.current_url
        except Exception, e:
            driver.quit()
        # finally:
        #     driver.close()
        #     driver.quit()


        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//p[@data-a-target='carousel-broadcaster-displayname']"))
        # )


        request.driver = driver
        # request.benjamin='>>>>>>>>>>>>>>>>>>>>name<<<<<<<<<<<<<'
        return HtmlResponse(url, body=body, encoding='utf-8', request=request)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
