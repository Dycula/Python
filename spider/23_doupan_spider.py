import requests
import time
from fake_useragent import UserAgent


class DoupanSpider(object):
    def __init__(self):
        self.base_url = "https://movie.douban.com/j/chart/top_list?"
        self.i = 0

    def get_html(self, params):
        ua = UserAgent()
        headers = {"User-Agent": ua.random}
        res = requests.get(url=self.base_url, params=params, headers=headers)
        res.encoding = "utf-8"
        html = res.json()
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        # html:[{电影1信息},{电影2信息},{},]
        item = {}
        for one in html:
            item["name"] = one["title"]
            item["score"] = one["score"]
            item["time"] = one["release_date"]
            print(item)
            self.i += 1

    def get_total(self,typ):
        url = "https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90".format(typ)
        ua = UserAgent()
        html = requests.get(url=url, headers= {"User-Agent": ua.random}).json()
        total = html["total"]
        return total

    def main(self):
        typ=input("请输入电影类型（剧情｜喜剧｜动作）：")
        typ_dict={"剧情":"11","喜剧":"24","动作":"5"}
        typ=typ_dict[typ]
        total=self.get_total(typ)
        for page in range(0, int(total), 20):
            params = {
                "type": "11",
                "interval_id": "100:90",
                "action": "",
                "start": str(page),
                "limit": 20
            }
            self.get_html(params)
            time.sleep(1)
        print("数量:", self.i)


if __name__ == "__main__":
    spider = DoupanSpider()
    spider.main()
