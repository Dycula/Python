import requests
from threading import Thread
from queue import Queue
import time
from fake_useragent import UserAgent
from lxml import etree


class XiaomiSpider(object):
    def __init__(self):
        self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30'
        # 存放所有url地址的队列
        self.q = Queue()
        self.ua = UserAgent()
        self.i = 0
        # 存放所有类型的空列表
        self.id_list = []

    def get_cateid(self):
        # 请求
        url = "http://app.mi.com/"
        headers = {"User-Agent": self.ua.random}
        html = requests.get(url=url, headers=headers).text
        # 解析
        parse_html = etree.HTML(html)
        xpath_bds = "//ul[@class='category-list']/li"
        li_list = parse_html.xpath(xpath_bds)
        for li in li_list:
            typ_name = li.xpath("./a/text()")[0]
            typ_id = li.xpath("./a/@href")[0].split("/")[-1]
            # 计算每个类型的页数
            pages = self.get_pages(typ_id)
            self.id_list.append((typ_id,pages))
        # 入队列
        self.url_in()

    # 获取counts的值并计算页数
    def get_pages(self, typ_id):
        # 每页返回的json数据中,都有count这个key
        url = self.url.format(0, typ_id)
        html = requests.get(url=url, headers={"User-Agent": self.ua.random}).json()
        count = html["count"]
        pages = int(count) // 30 + 1
        return pages

    # url入队列
    def url_in(self):
        for id in self.id_list:
            # id为元祖,("2",pages)
            for page in range(id[1]):
                url = self.url.format(page, id[0])
                print(url)
                # 把url地址入队列
                self.q.put(url)

    # 线程事件函数:get()--请求--解析--处理数据
    def get_data(self):
        while True:
            if not self.q.empty():
                url = self.q.get()
                headers = {"User-Agent": self.ua.random}
                html = requests.get(url=url, headers=headers).json()
                self.parse_html(html)
            else:
                break

    # 解析函数
    def parse_html(self, html):
        for app in html["data"]:
            # 获取应用名称
            name = app["displayName"]
            link = 'http://app.mi.com/details?id=' + app["packageName"]
            print(name, link)
            self.i += 1

    # 主函数
    def main(self):
        # url入队列
        self.get_cateid()
        t_list = []
        # 创建多个进程
        for i in range(1):
            t = Thread(target=self.get_data)
            t_list.append(t)
            t.start()
        # 回收线程
        for t in t_list:
            t.join()
        print("数量：", self.i)


if __name__ == "__main__":
    start = time.time()
    spider = XiaomiSpider()
    spider.main()
    end = time.time()
    print("执行时间:%.2f" % (end - start))
