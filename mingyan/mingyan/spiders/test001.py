import urllib.request

url = "http://tieba.baidu.com"

response = urllib.request.urlopen(url)
""":type : response"""
# assert isinstance(response,urllib.request)
# response.re

html = response.read()         # 获取到页面的源代码
print(html.decode('utf-8'))    # 转化为 utf-8 编码


def f()->int:
    pass
a=f()
a.