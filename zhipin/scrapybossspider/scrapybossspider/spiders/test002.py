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
#             <div id='images'>
#                 <a href='image1.html'>Name: Image 1 <br/><img src='image1.jpg'/></a>
#                 <a href='image2.html'>Name: Image 2 <br/><img src='image2.jpg'/></a>
#                 <a href='image3.html'>Name: Image 3 <br/><img src='image3.jpg'/></a>
#                 <a href='image4.html'>Name: Image 4 <br/><img src='image4.jpg'/></a>
#                 <a href='image5.html'>Name: Image 5 <br/><strong>Next Page</strong><img src='image5.jpg'/></a>
#             </div>
#         </body>
#     </html>
# '''
# response = HtmlResponse(url='http://www.example.com', body=body, encoding='utf8')
# extract = response.xpath('/html').extract()
# xpath = response.xpath("//a/text()").extract()
# response_xpath = response.xpath("/html/*")
# # s = response.xpath("//div//*")
# # selector_list_selector_list = response.xpath("//div//a/text()").extract()
# a_ = response.xpath("//a")[0].extract()
# s = response.xpath('string(//a)')
# selector_list_selector_list = response.xpath("//a[contains(@href,'image')]").extract()
# print(selector_list_selector_list)