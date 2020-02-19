# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShanbeiSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Chinese = scrapy.Field()

class JdsplashItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    p_store = scrapy.Field()
    comment = scrapy.Field()
    href = scrapy.Field()
    pass

class BosssplashItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    work = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    co = scrapy.Field()
    href = scrapy.Field()
    number = scrapy.Field()
    pass
