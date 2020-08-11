import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent


class GetProxyIP(object):
    def __init__(self):
        self.url = 'http://www.xicidaili.com/nn/{}'
        self.proxies = {"http": "http://183.6.183.35:8010",
                        "https": "https://183.6.183.35:8010"}

    # 随机生成一个User-Agent
    def get_random_ua(self):
        ua = UserAgent()
        useragent = ua.random
        return useragent

    def get_ip_file(self, url):
        headers = {"User-Agent": self.get_random_ua()}
        html = requests.get(url=url, headers=headers).text
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath("//tr")
        for tr in tr_list[1:]:
            ip = tr.xpath('./td[2]/text()')[0]
            port = tr.xpath('./td[3]/text()')[0]
            self.test_ip(ip, port)

    def test_ip(self, ip, port):
        # res.status_code==200
        proxies = {
            "http": "http://{}:{}".format(ip, port),
            "https": "https://{}:{}".format(ip, port)
        }
        test_url = "http://www.baidu.com/"
        try:
            res = requests.get(url=test_url, proxies=proxies)
            if res.status_code == 200:
                with open("proxies.txt", "a") as f:
                    f.write(ip + ":" + port + "\n")
        except Exception as e:
            print(ip, port, "filed")

    def main(self):
        for i in range(1, 1001):
            url = self.url.format(i)
            self.get_ip_file(url)
            time.sleep(random.randint(2, 5))


if __name__ == "__main__":
    spider = GetProxyIP()
    spider.get_ip_file('http://www.xicidaili.com/nn/{}')
