from selenium import webdriver
import time
#创建浏览器对象
browser=webdriver.Chrome()
browser.get('http://www.baidu.com/')
print(browser.page_source.find("kw"))
#获取快照
browser.save_screenshot('baidu.png')
browser.quit()