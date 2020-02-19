# -*- coding: utf-8 -*-
# @Time    : 2018/1/7 上午11:46
# @Author  : Mazy
# @File    : html_downloader.py
# @Software: PyCharm


import requests
import ssl


class HtmlDownloader(object):

    # 初始化方法，定义一些变量
    def __init__(self):
        ssl._create_default_https_context = ssl._create_unverified_context

    # 通过 url + 页码 + 关键词 获取数据
    def get_page(self, baseUrl, page_num, keyword):
        try:
            param = {"query": keyword, "city": "101010100", "page": page_num}

            # 设置请求头，模拟浏览器访问headers
            header = {
                'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                              r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
                'Referer': r'http://www.zhipin.com/job_detail/',
                'Connection': 'keep-alive'
            }

            header = {
                'x-devtools-emulate-network-conditions-client-id': "5f2fc4da-c727-43c0-aad4-37fce8e3ff39",
                'upgrade-insecure-requests': "1",
                'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
                'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                'dnt': "1",
                'accept-encoding': "gzip, deflate",
                'accept-language': "zh-CN,zh;q=0.8,en;q=0.6",
                'cookie': "__c=1501326829; lastCity=101020100; __g=-; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2F; __a=38940428.1501326829..1501326829.20.1.20.20; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1501326839; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1502948718; __c=1501326829; lastCity=101020100; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1501326839; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1502954829; __l=r=https%3A%2F%2Fwww.google.com.hk%2F&l=%2F; __a=38940428.1501326829..1501326829.21.1.21.21",
                'cache-control': "no-cache",
                'postman-token': "76554687-c4df-0c17-7cc0-5bf3845c9831"
            }

            result = requests.get(baseUrl, params=param, headers=header)

            print(result.text)

            return result.text

        except Exception as err:
            print(err)
            print("Boss直聘爬取失败")
            return None
