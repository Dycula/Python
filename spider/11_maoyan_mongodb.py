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
#1.连接对象
conn=pymongo.MongoClient(host="127.0.0.1",port=27017)
#2.库对象
db=conn["maoyandb"]
#3.集合对象
myset=db["filmtab"]
#4.插入数据库
myset.insert_one({"name":"小哥哥"})

from urllib import request
import time
import re
import random
from useragents import ua_list
import csv
import pymysql


class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        # 创建3个对象
        self.conn=pymongo.MongoClient("localhost",27017)
        self.db=self.conn["maoyandb"]
        self.myset=self.db["filmset"]


    def get_html(self, url):
        headers = {"User-Agent": random.choice(ua_list)}
        req = request.Request(url=url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode("utf-8")
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        re_bds = '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
        pattern = re.compile(re_bds, re.S)
        # film_list : [('霸王别姬','张国荣','1993'),(),()]
        film_list = pattern.findall(html)
        # 直接调用写入函数
        self.write_html(film_list)

    # mysql--->enum
    def write_html(self, film_list):
        for film in film_list:
            film_dict={"name":film[0].strip(),
                       "star":film[1].strip(),
                       "time":film[2].strip()[5:15]}
            #插入mongodb数据库
            self.myset.insert_one(film_dict)

    def main(self):
        for offset in range(0, 91, 10):
            url = self.url.format(offset)
            self.get_html(url)
            time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    start = time.time()
    spider = MaoyanSpider()
    spider.main()
    end = time.time()
    print("执行时间：%.2f" % (end - start))
