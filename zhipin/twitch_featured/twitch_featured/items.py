# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TwitchFeaturedItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    source = scrapy.Field()
    name = scrapy.Field()
    href = scrapy.Field()
    sale_status = scrapy.Field()
    # sale_time = scrapy.Field()
    hour = scrapy.Field()
    minute = scrapy.Field()
    second = scrapy.Field()
    url = scrapy.Field()
    pass
