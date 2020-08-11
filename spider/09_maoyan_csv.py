from urllib import request
import time
import re
import random
from useragents import ua_list
import csv

class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'

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

    # 存入csv文件
    def write_html(self, film_list):
        with open("film.csv","a") as f:
            writer=csv.writer(f)
            for film in film_list:
                l=[film[0].strip(),film[1].strip(),film[2].strip()[5:15]]
                writer.writerow(l)

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
