from selenium import webdriver
browser=webdriver.Chrome()
browser.get("https://www.qiushibaike.com/text/")
#单元素查找
div=browser.find_element_by_class_name("content")
print(div.text)

# 多元素查找: [<selenium xxx at xxx>,<selenium xxx >]
divs = browser.find_elements_by_class_name('content')
for div in divs:
  print('\033[31m*************************\033[0m')
  print(div.text)
  print('\033[31m*************************\033[0m')



