import requests
from scrapy.selector import Selector
splash_url = 'http://192.168.33.133:8050/render.html'
args = {'url':'https://sell.paipai.com/auction-list','timeout':5,'image':0}
response = requests.get(splash_url, params=args)
sel = Selector(response)
print sel.extract()
open("22222.html", 'wb').write(sel.extract().encode('utf-8'))

# extract = sel.css('div.quote span.text::text').extract()
# print extract