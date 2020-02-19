import requests
import json

lua_script = '''
    function main(splash)
        splash:set_user_agent("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36")
        splash:go("https://sell.paipai.com/auction-list")
        splash:wait(5.5)
        local body = splash:evaljs("document.title")
        return {html = splash:html()}
        end
    '''
splash_url = 'http://192.168.33.133:8050/execute'
headers = {'cookie':'_c_id=939lha9q0bi5pcfpm6z1580189151093kr1o; _s_id=um4u3d00umibnwlk2wh1580189151093uroo; __jda=104464258.15801891512741167695177.1580189151.1580189151.1580189151.1; __jdb=104464258.1.15801891512741167695177|1.1580189151; __jdc=104464258; __jdv=104464258|direct|-|none|-|1580189151283; um4u3d00umibnwlk2wh1580189151093uroo=-10312; __tak=a2d08bcba7bbe8d8b3407d7f73ddd0a9dd30bafbb609b03e9f524324ca77b29050a0d6b2e8c2767752bdc305412eb1229675a3b652c9e47d46584bc3dc1853a307d66d8bf2a4c99a175030deaf4d8ce0; 3AB9D23F7A4B3C9B=N65ZYUFY6CWQJIYRZ5BT7RPIK5Y467HNCSGSV6HL7CQYJXDDNP43LCMC7WCSVZS4Z3HODB5MDOGW3TYOCRPPGIAH3I','content-type':'application/json','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
data = json.dumps({'lua_source':lua_script})
response = requests.post(splash_url,headers=headers,data=data)
response.content
open("33333.html", 'wb').write(response.content.encode('utf-8'))

# extract = sel.css('div.quote span.text::text').extract()
# print extract