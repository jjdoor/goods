# -*- coding: UTF-8 -*-
import re
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
# from urllib.parse import urlparse
# from urllib2 import *
from urlparse import *

read1 = open('example1.html').read()
read2 = open('example2.html').read()
response1 = HtmlResponse(url='https://www.zhipin.com', body=read1, encoding='utf8')
response2 = HtmlResponse(url='http://www.51job.com', body=read1, encoding='utf8')
extractor1 = LinkExtractor(allow='.*job_detail.*html')
extractor2 = LinkExtractor()
links1 = extractor1.extract_links(response1)
links2 = extractor2.extract_links(response2)
# https://www.zhipin.com/job_detail/a16bd912681b28dc1nJz2dW6FFc~.html
pattern = '.*job_detail.*$'
# for link in links1:
#     print(link.url)

# print(urlparse(response1.url).geturl())
# pattern = patten = '^'+urlparse(response1.url).geturl()
# print(patten)
# extractor = LinkExtractor(deny=pattern)
def process(value):
    search = re.search("sign-welcome", value)
    if search:
        return value
extractor = LinkExtractor(tags='div',attrs='class',process_value=process)
links = extractor.extract_links(response1)
# print(links)
for link in links:
    print(link.url)
# print (links1)
