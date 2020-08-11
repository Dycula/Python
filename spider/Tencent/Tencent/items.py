# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    # 类别
    job_type = scrapy.Field()
    # 职责
    job_duty = scrapy.Field()
    # 要求
    job_require = scrapy.Field()
    # 地址
    job_address = scrapy.Field()
    #时间
    job_time=scrapy.Field()
