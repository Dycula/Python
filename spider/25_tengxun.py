import requests
import json
import time
import random
from useragents import ua_list


class TencentSpider(object):
    def __init__(self):
        self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
        self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn'

    # 获取响应内容函数
    def get_page(self, url):
        headers = {"User-Agent": random.choice(ua_list)}
        html = requests.get(url=url, headers=headers).text
        # json格式字符串--->python
        html = json.loads(html)
        return html

    # 主线函数：获取所有数据
    def parse_page(self, one_url):
        html = self.get_page(one_url)
        item = {}
        for job in html["Data"]["Posts"]:
            # 名称
            item["name"] = job["RecruitPostName"]
            item['address'] = job['LocationName']
            # postid
            post_id = job["PostId"]
            # 拼接二级地址,获取职责和要求
            two_url = self.two_url.format(post_id)
            item["duty"], item["requirement"] = self.parse_two_page(two_url)
            print(item)

    # 解析二级页面函数
    def parse_two_page(self, two_url):
        html = self.get_page(two_url)
        duty = html["Data"]["Responsibility"]
        duty = duty.replace("\r\n", "").replace("\n", "")
        require = html["Data"]["Requirement"]
        require = require.replace("\r\n", "").replace("\n", "")
        return duty, require

    def get_numbers(self):
        url = self.one_url.format(1)
        html = self.get_page(url)
        numbers = int(html["Data"]["Count"]) // 10 + 1
        return numbers

    def main(self):
        number = self.get_numbers()
        for page in range(1, number):
            one_url = self.one_url.format(page)
            self.parse_page(one_url)


if __name__ == "__main__":
    start=time.time()
    spider = TencentSpider()
    spider.main()
    end=time.time()
    print("执行时间：%.2f"%(end-start))
