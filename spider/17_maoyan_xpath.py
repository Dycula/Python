"""
非关系型数据库
基本命令
show dbs#所有库
use 库名　#切换库
show collections#查看库中所有的集合
db.集合名.find().pretty()#查看集合中所有文档
db.集合名.count()#统计集合中文档个数
"""

import pymongo

# 1.连接对象
conn = pymongo.MongoClient(host="127.0.0.1", port=27017)
# 2.库对象
db = conn["maoyandb"]
# 3.集合对象
myset = db["filmtab"]
# 4.插入数据库
myset.insert_one({"name": "小哥哥"})

import requests
from lxml import etree
import time
import re
import random
from useragents import ua_list
import csv
import pymysql


class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.page = 1

    def get_page(self, url):
        try:
            headers = {"User-Agent": random.choice(ua_list)}
            res = requests.get(url=url, headers=headers)
            res.encoding = "utf-8"
            html = res.text
            # 直接调用解析函数
            self.parse_html(html)
        except Exception as e:
            print('Error')
            self.get_page(url)

    def parse_html(self, html):
        # 创建解析对象
        parse_html = etree.HTML(html)
        # 基准xpath节点对象列表
        dd_list = parse_html.xpath('//dl[@class="board-wrapper"]/dd')
        item = {}
        # 依次遍历每个节点对象,提取数据
        if dd_list:
            for dd in dd_list:
                # 电影名称
                name_list = dd.xpath('.//p/a/@title')
                item['name'] = [name_list[0].strip() if name_list else None][0]
                # 电影主演
                star_list = dd.xpath('.//p[@class="star"]/text()')
                item['star'] = [star_list[0].strip() if star_list else None][0]
                # 上映时间
                time_list = dd.xpath('.//p[@class="releasetime"]/text()')
                item['time'] = [time_list[0].strip() if time_list else None]
                print(item)
        else:
            print('No Data')

    def main(self):
        for offset in range(0, 31, 10):
            url = self.url.format(str(offset))
            self.get_page(url)
            print('第%d页完成' % self.page)
            time.sleep(random.randint(1, 3))
            self.page += 1


if __name__ == "__main__":
    start = time.time()
    spider = MaoyanSpider()
    spider.main()
    end = time.time()
    print("执行时间：%.2f" % (end - start))
