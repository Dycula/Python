from selenium import webdriver
# 导入鼠标事件类
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
#输入selenium 搜索
driver.find_element_by_id('kw').send_keys('赵丽颖')
driver.find_element_by_id('su').click()
#移动到 设置,perform()是真正执行操作,必须有
element = driver.find_element_by_name('tj_settingicon')
ActionChains(driver).move_to_element(element).perform()
#单击,弹出的Ajax元素,根据链接节点的文本内容查找
driver.find_element_by_link_text('高级搜索').click()