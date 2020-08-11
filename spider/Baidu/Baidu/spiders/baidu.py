# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名：scrapy crawl 爬虫名
    name = 'baidu'
    # 允许爬虫名
    allowed_domains = ['www.baidu.com']
    # 起始Url地址
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # response为百度的响应对象,提取“百度一下,你就知道”
        xpath_bds = "/html/head/title/text()"
        #r_list:[<selector xpath="",data="">]
        #extract:["百度一下,你就知道"]
        #r_list = response.xpath(xpath_bds).extract()
        #extract_first():"百度一下,你就知道"
        #r_list = response.xpath(xpath_bds).extract_first()
        #1.6版本后可以使用get():"百度一下,你就知道"
        r_list = response.xpath(xpath_bds).get()
        print("*" * 50)
        print(r_list)
        print("*" * 50)
