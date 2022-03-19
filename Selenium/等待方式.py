# encoding=utf-8
"""
Selenium中的三大等待方式：
（1）强制等待sleep
最普通的时间等待方式，最直观简单，可以放在需要时间等待的地方，不管页面加载是否完成都必须等待，不够灵活。
"""
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
#强制等待
time.sleep(3)
print(driver.current_url)
driver.quit()
"""
（2）隐性等待implicitly_wait
隐性等待就是设置了一个最长等待时间，如果页面在等待时间内加载完了，则执行下一步，如果页面加载时间超过等待时间，那么最长在等待时间时就执行下一步。这样做的好处，就是页面加载完了就执行，页面没加载完就到等待时间执行下一步。坏处就是，等待时间长短的设置，会影响脚本运行效率的关键，另一个就是，在等待时间过了之后执行下一步，很容易定位不到元素，需要加上判断，抛出异常
注意：隐性等待对整个driver的周期都起作用，设置一次即可
"""
from selenium import  webdriver
driver = webdriver.Chrome()
#设置隐性等待，最长30s
driver.get("https://www.baidu.com")
print(driver.current_url)
driver.quit()
"""
(3)显性等待WebDriverWait
这个类的运作流程就是，程序每过一段时间就检查一次，如果条件成立就执行下一步，如果条件不成立，继续等待，直到超过最大等待时间，抛出TimeoutException
配合until()和until_not()方法，可以根据判断条件进行灵活的等待了
"""
from selenium import  webdriver
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id('kw').send_keys('自动化测试')
driver.find_element_by_id('su').click()
locator = (By.LINK_TEXT,"00")
try:
    WebDriverWait(driver,10,1).until(EC.presence_of_elemet_located(locator))
    print(driver.find_element_by_link_text("00").get_attribute("href"))
except:
    print("未找到，已超时")
finally:
    driver.quit()





