# -*- coding: utf-8 -*-
import json

import scrapy
from ..items import SoItem


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']
    url = 'http://image.so.com/zj?ch=beauty&sn={} & listtype = new & temp = 1'

    def start_requests(self):
        for sn in range(0, 300, 100):
            url = self.url.format(sn)
            yield scrapy.Request(
                url=url,
                callback=self.parse_page
            )

    def parse_page(self, response):
        html = json.loads(response.text)
        item = SoItem()
        for img in html("list"):
            item["img_url"] = img["qhimg_url"]
            yield item

    def parse(self, response):
        pass
