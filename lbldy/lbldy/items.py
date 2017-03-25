# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LbldyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dy_name = scrapy.Field()    #电影名称
    dy_summary = scrapy.Field() #电影简介
    dy_link = scrapy.Field()    #电影下载链接
    dy_websit = scrapy.Field()  #电影下载网页
