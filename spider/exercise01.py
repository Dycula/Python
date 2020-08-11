import os

import requests
from lxml import etree
from useragents import ua_list
import random


class CodeSpider(object):
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDcode/aid1904/14-redis/'
        self.auth = ("tarenacode", "code_2013")

    def parse_html(self):
        html = requests.get(url=self.url,
                            headers={"User-Agent": random.choice(ua_list)},
                            auth=self.auth).content.decode("utf-8", 'ignore')
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath("//a/@herf")
        for r in r_list:
            if r.endswith(".zip") or r.endswith(".rar"):
                self.save_files(r)
    def save_files(self,r):
        #操作目录home/tarena/redis
        directory="/home/tarena/AID/redis/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        #拼接地址,把zip文件保存到指定目录
        url=self.url+r
        #filename:home/tarena/AID/redis/xxx.zip
        filename=directory+r
        html=requests.get(url=url,
                          headers={"User-Agent":random.choice(ua_list)},
                          auth=self.auth).content
        with open(filename,"wb") as f :
            f.write(html)
            print("%s下载成功"%r)


if __name__ == "__main__":
    spider = CodeSpider()
    spider.parse_html()
