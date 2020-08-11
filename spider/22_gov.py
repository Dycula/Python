import requests
from lxml import etree
import re
import pymysql


class GovementSpider(object):
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {"User-Agent": "Mozilla/5.0"}
        # 创建2个对象
        self.db = pymysql.connect("127.0.0.1", "root", "123456", "govdb", charset="utf8")
        self.cursor = self.db.cursor()

    # 获取假链接
    def get_false_link(self):
        html = requests.get(url=self.url, headers=self.headers).text
        # 解析
        parse_html = etree.HTML(html)
        a_list = parse_html.xpath('//a[@class="artitlelist"]')
        for a in a_list:
            # title=a.xpath('./@title')[0]
            # get()方法:获取某个属性的值
            title = a.get("title")
            if title.endswith("代码"):
                false_link = "http://www.mca.gov.cn" + a.get("href")
                break
        self.incr_spider(false_link)

    # 增量函数
    def incr_spider(self, false_link):
        sel = "select url from version where url=%s"
        self.cursor.execute(sel, [false_link])
        # fetchall:(('http://xxx.html'),)
        result = self.cursor.fetchall()
        if not result:
            self.get_true_link(false_link)
            #可选操作：数据库version表中保留最新1条数据
            dele="delete from version"
            self.cursor.execute(dele)
            # 把提取后的url插入到version中
            ins = "insert into version values(%s)"
            self.cursor.execute(ins, [false_link])
            self.db.commit()
        else:
            print("数据已是最新,无需爬取")

    # 获取真链接
    def get_true_link(self, false_link):
        html = requests.get(url=false_link, headers=self.headers).text
        # 正则获取真是数据
        re_bds = r'window.location.href="(.*?)"'
        pattern = re.compile(re_bds, re.S)
        true_link = pattern.findall(html)[0]
        self.save_data(true_link)

    # 数据提取
    def save_data(self, true_link):
        html = requests.get(url=true_link, headers=self.headers).text
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//tr[@height=19 ]')
        for tr in tr_list:
            code = tr.xpath("./td[2]/text()")[0].strip()
            name = tr.xpath("./td[3]/text()")[0].strip()
            print(code, name)

    # 主函数
    def main(self):
        spider.get_false_link()


if __name__ == "__main__":
    spider = GovementSpider()
    spider.main()
