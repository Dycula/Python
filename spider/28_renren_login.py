import requests


class RenRenLogin(object):
    def __init__(self):
        # url为需要登录才能正常访问的地址
        self.url = 'http://www.renren.com/967469305/profile'
        # headers中的cookie为登录成功后抓取到的cookie
        self.headers = {
            # 此处注意cookie,要自己抓取
            "Cookie": "xxx",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        }

    # 获取个人主页响应
    def get_html(self):
        html = requests.get(url=self.url, headers=self.headers, verify=False).text
        print(html)
        self.parse_html(html)

    # 可获取并解析整个人人网内需要登录才能访问的地址
    def parse_html(self, html):
        pass


if __name__ == '__main__':
    spider = RenRenLogin()
    spider.get_html()
