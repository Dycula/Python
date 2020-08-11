from selenium import  webdriver
import time
#1.创建浏览器对象
browser=webdriver.Chrome()
#2.输入：http://www.baidu.com
browser.get("http://www.baidu.com/")
#3.找到搜索框,向这个节点发送文字
browser.find_element_by_xpath("//*[@id='kw']").send_keys("赵丽颖")
#4.找到百度一下按钮,点击一下
time.sleep(2)
browser.find_element_by_xpath('//*[@id="su"]').click()