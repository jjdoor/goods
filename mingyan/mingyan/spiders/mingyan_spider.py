import scrapy
# import influxdb

class mingyan(scrapy.Spider):
    name = "mingyan2"
    def start_requests(self):
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
            # 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv26195&productId=19220331267&score=0&sortType=6&page=2&pageSize=10&isShadowSku=0&rid=0&fold=1',
            # 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv26195&productId=19220331267&score=0&sortType=6&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1',
            # 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv26195&productId=19220331267&score=0&sortType=6&page=0&pageSize=10&isShadowSku=0&fold=1',
            # 'https://item.jd.com/610898.html#comment'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        page = response.url.split("/")[-2]  # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        filename = 'mingyan-%s.html' % page  # 拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html
        with open(filename, 'wb') as f:  # python文件操作，不多说了；
            f.write(response.body)  # 刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
        self.log('保存文件: %s' % filename)