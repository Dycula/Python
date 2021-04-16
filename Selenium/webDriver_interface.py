# _*_coding:utf-8 _*_
# description:webDriver aw interface
# date:2020/09/16
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.touch_actions import TouchActions
from time import sleep
import sys
import os
import re

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass


class NoFoundException(Exception):
    # 控件未找到异常类
    def __init__(self, log):
        self.log = log


def utf2gbk(func):
    # 处理Python2.7编码问题
    def _process(*args, **kwargs):
        if sys.version_info.major >= 3:
            return func(*args, **kwargs)
        new_args = []
        new_args.append(args[0])
        for i in args[1:]:
            try:
                if isinstance(i, str):
                    i = i.decode('utf-8')
            except Exception as e:
                print(e)
            new_args.append(i)
        return func(*new_args, **kwargs)

    return _process


def waitLoading(func):
    # 等待Loading结束
    def _process(*args, **kwargs):
        self = args[0]
        self.log("Wait Loading....")
        i = 1
        while i <= 30:
            try:
                f = self.driver.find_element('xpath', '//*[text()="加载中..."]')
            except Exception as e:
                try:
                    f = self.driver.find_element('xpath', '//*[text()="Loading..."]')
                except:
                    break
            i = i + 1
            sleep(1)
        return func(*args, **kwargs)

    return _process


def wrapper(func):
    # 统一处理函数，用于简化接口实现
    def _process(*args, **kwargs):
        self = args[0]
        if self.DEBUG:
            strFuncName = ''
            try:
                strFuncName = func.__name__
                self.log("Call %s%s" % (strFuncName, args[1:]))
            except:
                pass
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if self.dealFailFunc is not None:
                self.dealFail()
                self.dealFailFunc()
            else:
                self.dealFail()
            if self.ASSERT_IF_FAIL:
                assert False, e
            else:
                self.log(str(e))
                return False

    return _process


def logFunc(log):
    # 默认log函数
    print(log)


def scrollIntoView(func):
    '''
    将需要点击的控件对象滚动到可视区域。被装饰的函数传入的第二个参数为查找控件的条件，第三个参数为查找控件的方式
    '''

    def _process(*args, **kwargs):
        try:
            if kwargs:
                args[0].log('Move "+str(args[1])+" to the visible area')
                args[0].driver.execte_script('arguments[0].scrollIntoView({block:"center",inline:"center"});',
                                             args[0].driver.find_element(kwargs['by'], args[1]))
            else:
                args[0].log('Move "+str(args[1])+" to the visible area')
                args[0].driver.execte_script('arguments[0].scrollIntoView({block:"center",inline:"center"});',
                                             args[0].driver.find_element('xpath', args[1]))
        except Exception as e:
            print(e)
        return func(*args, **kwargs)

    return _process


def scrollIntoView_New(func):
    '''
    将需要点击的控件对象滚动到可视区域。被装饰的函数传入的第二个参数是被点击的元素对象
    '''

    def _process(*args, **kwargs):
        try:
            args[0].log('Move "+str(args[1])+" to the visible area')
            args[0].driver.execte_script('arguments[0].scrollIntoView({block:"center",inline:"center"});', args[1])
        except Exception as e:
            print(e)
        return func(*args, **kwargs)

    return _process


class Broswer():
    '''
    浏览器对象，web操作失败后默认抛异常置用例失败，如需重试处理，可修改ASSERT_IF_FAIL或使用自行捕获异常处理
    '''

    def __init__(self, logFunc=logFunc, dealFailFunc=None, screenshotSaveName='screenshot', ASSERT_IF_FAIL=True,
                 DEBUG=True):
        """
        logFunc:日志处理函数
        dealFailFunc:失败处理函数，例如可以用来失败截图，日志收集
        ASSERT_IF_FAIL:失败时处理标志，True则assert，False则返回False
        DEBUG:DEBUG开关
        """
        self.log = logFunc
        self.ASSERT_IF_FAIL = ASSERT_IF_FAIL
        self.DEBUG = DEBUG
        self.driver = None
        if dealFailFunc is not None:
            self.dealFailFunc = dealFailFunc
        else:
            self.dealFailFunc = dealFailFunc
        self.screenshotSaveName = '%s.png' % screenshotSaveName
        self.screenshotSavePath = "C:\\AutoFactoryLogs\AllFailPics\\"
        if not os.path.exists(self.screenshotSavePath):
            os.makedirs(self.screenshotSavePath)

    def dealFail(self):
        """
        失败处理，默认方式为截图，如需增加自定义处理方式，可在new类对象时传dealFailFunc
        """
        if self.driver is not None:
            self.driver.save_screenshot('%s%s' % (self.screenshotSavePath, self.screenshotSaveName))

    @wrapper
    def open(self, strUrl, strBrowser='chrome'):
        """
        打开指定网页
        Args:
            strUrl:待打开网址
            strBrowser:使用的浏览器，默认为chrome，支持chrome/firefox/ie
        Return:
            None
        """
        