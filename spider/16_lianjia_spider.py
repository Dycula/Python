import requests
from lxml import etree
import time
import random
from useragents import ua_list


class LianjiaSpider(object):
    def __init__(self):
        self.url = "https://bj.lianjia.com/ershoufang/pg{}/"
        self.page = 1

    def get_html(self, url):
        try:
            headers = {'User-Agent': random.choice(ua_list)}
            res = requests.get(url=url, headers=headers)
            res.encoding = "utf-8"
            html = res.text
            self.parse_page(html)
        except Exception as e:
            print('Error')
            self.get_html(url)

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        # li_list:[<element li a xxx>....]
        li_lsit = parse_html.xpath('/ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATALOGCLICKDATA"]')
        item = {}
        for li in li_lsit:
            # 名称
            name_list = li.xpath('.//a[@data-el="region"]/text()')
            if name_list:
                item["name"] = name_list[0].strip()
            else:
                item["name"] = None
            info_list = li.xpath('.//div[@class="houseInfo"]/text()')[0].strip().split("|")
            item["model"] = info_list[1].strip()
            item["area"] = info_list[2].strip()
            item["direction"] = info_list[3].strip()
            item["perfect"] = info_list[4].strip()
            # 楼层
            item["floor"] = li_lsit.xpath('.//div[@class="positionInfo"]/text()')[0].strip()
            # 区域
            item["address"] = li_lsit.xpath('.//div[@class="positionInfo"]/a/text()')[0].strip()
            # 总价
            item["total_price"] = li_lsit.xpath('.//div[@class="totalPrice"]/span/text()')[0].strip()
            # 单价
            item["unit_price"] = li_lsit.xpath('.//div[@class="unitPrice"]/span/text()')[0].strip()
            print(item)

    def main(self):
        for pg in range(1, 11):
            url = self.url.format(str(pg))
            self.get_html(url)
            print('第%d页爬取成功' % pg)
            time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    start = time.time()
    spider = LianjiaSpider()
    spider.main()
    end = time.time()
    print("执行时间：%.2f" % (end - start))
