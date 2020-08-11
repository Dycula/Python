from selenium import webdriver
import time


class JdSpider(object):
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.url = 'https://www.jd.com/'
        self.i = 0

    # 获取商品页面
    def get_page(self):
        self.browser.get(self.url)
        # 找2个节点
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书籍')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(2)

    # 解析页面
    def parse_page(self):
        # 把下拉菜单拉到底部,执行JS脚本
        self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        # 匹配所有商品节点对象列表
        li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        item = {}
        for li in li_list:
            item['name'] = li.find_element_by_xpath(
                './/div[@class="p-name"] |.//div[@class="p-name p-name-type-2"]').text
            item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]').text
            item['commit'] = li.find_element_by_xpath('.//div[@class="p-commit"]').text
            item['shopname'] = li.find_element_by_xpath(
                './/div[@class="p-shopnum"]/a |.//div[@class="p-shopnum"]/span').text
            print(item)
            self.i += 1

    # 主函数
    def main(self):
        self.get_page()
        while True:
            self.parse_page()
            # 判断是否该点击下一页,没有找到说明不是最后一页
            if self.browser.page_source.find('pn-next disabled') == -1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(2)
            else:
                break
        print(self.i)


if __name__ == '__main__':
    spider = JdSpider()
    spider.main()
