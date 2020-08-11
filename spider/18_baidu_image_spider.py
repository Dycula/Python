import requests
from lxml import etree
import random
import time
from useragents import ua_list
from urllib import parse

class BaiduimageSpider(object):
    def __init__(self):
        self.url = "http://tieba.baidu.com/f?kw={}&pn={}"

    # 获取html的功能函数
    def get_html(self, url):
        html = requests.get(url=url, headers={"User-Agent": random.choice(ua_list)}).content.decode("utf-8")
        return html

    # 解析html的功能函数
    def xpath_func(self, html, xpath_bds):
        parse_html = etree.HTML(html)
        r_list = parse_html.xpath(xpath_bds)
        return r_list

    # 解析函数--实现最终的图片抓取
    def parse_html(self, one_url):
        html = self.get_html(one_url)
        # 准备提取帖子链接
        xpath_bds = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        r_list = self.xpath_func(html, xpath_bds)
        for r in r_list:
            # 拼接帖子的url地址
            t_url = "http://tieba.baidu.com" + r
            # 把帖子中所有图片保存到本地
            self.get_image(t_url)
            #爬完一个帖子后进行休眠
            time.sleep(random.uniform(1,3))

    # 功能:给定一个帖子url,把帖子中所有图片保存到本地
    def get_image(self, t_url):
        html=self.get_html(t_url)
        #图片链接的xpath的表达式：image_list["http://xx.jpg"]
        xpath_bds='//*[@class="d_post_content j_d_post_content　clearfix"]/img/@src'
        img_list=self.xpath_func(html,xpath_bds)
        for img in img_list:
            html_bytes=requests.get(url=img,headers={"User-Agent": random.choice(ua_list)}).content
            self.save_img(html_bytes,img)
    def save_img(self,html_bytes,img):
        filename=img[-10:]
        with open(filename,"wb") as f:
            f.write(html_bytes)
            print("%s下载成功"%filename)

    # 主函数
    def main(self):
        name=input("请输入贴吧名：")
        begin=int(input("请输入起始页："))
        end=int(input("请输入终止页："))
        #对贴吧名进行编码
        kw=parse.quote(name)
        for page in range(begin,end+1):
            pn=(page-1)*50
            url=self.url.format(kw,pn)
            #调用主线函数
            self.parse_html(url)



if __name__ == "__main__":
    start = time.time()
    spider = BaiduimageSpider()
    spider.main()
    end = time.time()
    print("执行时间：%.2f" % (end - start))
