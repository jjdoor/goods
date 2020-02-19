import requests

get = requests.get("http://www.baidu.com")
print(get.content)
get.encoding = 'UTF-8'
print(get.encoding)
print(get.url)
print(get.text)