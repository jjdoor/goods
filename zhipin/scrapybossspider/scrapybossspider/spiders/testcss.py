# -*- coding: utf-8 -*-
# from scrapy.http import HtmlResponse
#
# body = '''
#     <html>
#         <head>
#             <base href='http://example.com/'>
#             <title>Example website</title>
#         </head>
#         <body>
#             <div id='images-1' style='width:1230px;'>
#                 <a href='image1.html'>Name: Image 1 <br/><img src='image1.jpg'/></a>
#                 <a href='image2.html'>Name: Image 2 <br/><img src='image2.jpg'/></a>
#             </div>
#             <div id='images-2' class='small'>
#                 <a href='image4.html'>Name: Image 4 <br/><img src='image4.jpg'/></a>
#                 <a href='image5.html'>Name: Image 5 <br/><strong>Next Page</strong><img src='image5.jpg'/></a>
#             </div>
#         </body>
#     </html>
# '''
# response = HtmlResponse(url='http://www.example.com', body=body, encoding='utf8')
# css = response.css('img')
# response_css = response.css('base,title')
# s = response.css('div:nth-child(2)>a:nth-child(2)').extract()
# selector_list_selector_list = response.css('a::attr(href)')
# print(selector_list_selector_list)