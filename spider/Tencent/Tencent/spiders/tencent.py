# -*- coding: utf-8 -*-
import json
from urllib import parse

import requests
import scrapy
from ..items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp = 1563912271089 & countryId = & cityId = & bgIds = & productId = & categoryId = & parentCategoryId = & attrId = & keyword = & pageIndex = {} & pageSize = 10 & language = zh - cn & area = cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn'
    user_input = input("请输入工作类型:")

    # 重写start_requests()方法,把一级页面所有地址交给调度器
    def start_requests(self):
        user_input = parse.quote(self.user_input)
        total=self.get_total(user_input)
        for index in range(1, total):
            url = self.one_url.format(user_input, index)
            yield scrapy.Request(
                url=url,
                callback=self.parse_one_page
            )
    def get_total(self,user_input):
        url=self.one_url.format(user_input,1)
        html=requests.get(url=url).json()
        total=html["Data"]["Count"]//10+1
        return total

    def parse_one_page(self, response):
        html = response.text
        html = json.loads(html)
        for job in html["Data"]["Posts"]:
            post_id = job["PostId"]
            url = self.two_url.format(post_id)
            yield scrapy.Request(
                url=url,
                callback=self.parse_two_page
            )

    def parse_two_page(self, response):
        item = TencentItem()
        html = json.loads(response.text)
        item["job_name"] = html['Data']['RecruitPostName']
        item["job_type"] = html['Data']['CategoryName']
        item["job_duty"] = html['Data']['Responsibility']
        item["job_reqire"] = html['Data']['Responsibility']
        item["job_address"] = html['Data']['LocationName']
        item["job_time"] = html["Data"]["LastUpdateTime"]
        yield

    def parse(self, response):
        pass
