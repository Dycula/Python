# encoding=utf-8
#
# 浏览器驱动
from selenium import webdriver


class Browser_Engine():
    def __init__(self):
        """创建浏览器类型"""
        self.driver = driver_Creator().get_driver()
        if not hasattr(self,"driver"):     # 判断当前是否有driver对象, 如果没有就调用一下初始化driver
            self.driver = webdriver.Chrome()


    def get_browser(self):
        """浏览器类型选择, 返回驱动"""
        if self.driver == "Chrome":
            driver = webdriver.Chrome()
        elif self.driver == "Firefox":
            driver = webdriver.Firefox()
        elif self.driver == "IE":
            driver = webdriver.Ie()
        else: driver = webdriver.Chrome()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get("http://121.41.14.39:8088/index.html#/demo/96")
        return driver

class Single(object):       # 单例模式
    def __new__(cls, *args, **kwargs):
        # 查看当前类是否有对象
        if not hasattr(cls, "_instance"):
            #没有创建1个再返回
            # object创建对象
            cls.instance = object.__new__(cls)
        return cls.instance  # 返回创建的对象

# 单例模式可以继承
class driver_Creator(Single):
    def get_driver(self):
        if not hasattr(self,"driver"):     # 判断当前是否有driver对象, 如果没有就调用一下初始化driver
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
        return self.driver



# encoding=utf-8

# # 浏览器驱动
# from selenium import webdriver
# import time
#
#
# class Browser(object):
#
#     def __init__(self):
#         self.driver = None
#
#     def open(self, strUrl, strBrowser='chrome'):
#         """
#         打开指定网页
#         Args:
#             strUrl:待打开网址
#             strBrowser:使用的浏览器，默认为chrome，支持chrome/firefox/ie
#         Return:
#             None
#         """
#         if strBrowser == 'chrome':
#             self.driver = webdriver.Chrome()
#         elif strBrowser == 'firefox':
#             self.driver = webdriver.Firefox()
#         elif strBrowser == 'ie':
#             self.driver = webdriver.Ie()
#         else:
#             print('No support browser type:%s,use "chrome" as default' % strBrowser)
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(30)  # 隐性等待，最长等30秒
#
#         self.driver.get(strUrl)
#         self.driver.maximize_window()
#         time.sleep(2)
#
#
# browser = Browser()







