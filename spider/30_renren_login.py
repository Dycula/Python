import requests
from lxml import etree


class RenrenSpider(object):
    def __init__(self):
        self.post_url = 'http://www.renren.com/PLogin.do'
        self.get_url = 'http://www.renren.com/967469305/profile'
        # 实例化session对象
        self.session = requests.session()

    def get_html(self):
        # email和password
        form_data = {
            "email": "",
            "possword": ""
        }
        # 先session.post()
        self.session.post(url=self.post_url, data=form_data)
        # 再session.get()
        html = self.session.get(url=self.get_url).text
        self.parse_html(html)

    def parse_html(self, html):
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath("//li[@class='school']/span/text()")
        print(r_list)


if __name__ == '__main__':
    spider = RenrenSpider()
    spider.get_html()
