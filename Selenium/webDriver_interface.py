# _*_coding:utf-8 _*_
# description:webDriver aw interface
# date:2021/04/16
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
    """
    控件未找到异常类
    """

    def __init__(self, log):
        self.log = log


def utf2gbk(func):
    """
    处理Python2.7编码问题
    """

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
    """
    等待Loading结束
    """

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
    """
    统一处理函数，用于简化接口实现
    """

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
    """
    默认log函数
    """
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
        if strBrowser == 'chrome':
            self.driver = webdriver.Chrome()
        elif strBrowser == 'firefox':
            self.driver = webdriver.firefox()
        elif strBrowser == 'ie':
            self.driver = webdriver.ie()
        else:
            self.log('No support browser type:%s,use "chrome" as default' % strBrowser)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)  # 隐性等待，最长等30秒
        # self.driver.pageLoadTimeout(10)
        self.driver.get(strUrl)
        self.driver.maximize_window()
        sleep(2)

    @wrapper
    def quit(self):
        """
        关闭浏览器
        """
        self.driver.quit()

    @wrapper
    def clear_then_input(self, strElement, strValue, by='xpath'):
        """
        清空输入框，然后输入
        Args：
            strElement：输入对象
            strValue：输入值
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        """
        self.driver.find_element(by, strElement).clear()
        self.driver.find_element(by, strElement).send_keys(strValue)

    @wrapper
    def clear(self, strElement, by='xpath'):
        """
        清空输入框
        Args：
            strElement：输入对象
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        """
        self.driver.find_element(by, strElement).clear()

    @wrapper
    def input(self, strElement, strValue, by='xpath'):
        """
        输入
        Args：
            strElement：输入对象
            strValue：输入值
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        """
        self.driver.find_element(by, strElement).send_keys(strValue)

    @wrapper
    def click(self, strElement, by='xpath'):
        """
        点击
        Args：
            strElement：输入对象
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        """
        self.driver.find_element(by, strElement).click()

    @waitLoading
    @wrapper
    def mousedown(self, strElement, by='xpath'):
        """
        鼠标按下
        Args：
            strElement：控件
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        """
        driver = self.driver
        ActionChains(driver).click_and_hold(driver.find_element(by, strElement)).perform()

    @wrapper
    def chexkbox(self, strElement, op, by='xpath'):
        """
        checkbox勾选/去勾选
        Args：
            strElement：控件
            op:操作，支持check/uncheck/getstatus
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        """
        pass

    @wrapper
    def move_to_element(self, strElement, by='xpath'):
        """
        移动鼠标
        Args：
            strElement：控件
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        """
        attrible = self.driver.find_element(by, strElement)
        ActionChains(self.driver).move_to_element(attrible).perform()

    @wrapper
    def wait(self, time):
        """
        硬等待
        Args：
            time:等待时长
        """
        sleep(int(time))

    @wrapper
    def waitAppear(self, strElement, intTime=60, by='xpath'):
        """
        等待某个控件出现
        Args：
            strElement：控件
            intTime:等待时长
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        Return：
            True/False
        """
        i = 1
        while i <= int(intTime):
            if self.isElementPresent(strElement, by):
                return True
            i += 1
            sleep(1)
        return False

    @wrapper
    def waitDisappear(self, strElement, intTime=60, by='xpath'):
        """
        等待某个控件消失
        Args：
            strElement：等待控件
            intTime:等待时长
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        Return：
            True/False
        """
        i = 1
        while i <= int(intTime):
            if not self.isElementPresent(strElement, by):
                return True
            i += 1
            sleep(0.1)
        return False

    @wrapper
    def isElementPresent(self, strElement, by='xpath'):
        """
        web对象是否存在
        Args：
            strElement：等待控件
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        Return：
            True/False
        """
        try:
            self.driver.find_element(by, strElement)
            return True
        except:
            return False

    @wrapper
    def getElementCount(self, strElement, by='xpath'):
        """
        Args：
            strElement：统计的控件
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        Return：
            统计数量
        """
        ret = len(self.driver.find_elements(by, strElement))
        return ret

    @wrapper
    def getAttribute(self, strElement, attrib, by='xpath'):
        """
        获取控制属性
        Args：
            strElement：控件
            attrib:属性
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        Return：
            属性值
        """
        return self.driver.find_element(by, strElement).get_attribute(attrib)

    @wrapper
    def getValue(self, strElement, by='xpath'):
        """
        获取控件值
        Args：
            strElement：控件
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        Return：
            控件值
        """
        return self.getAttribute(strElement, 'value', by)

    @wrapper
    def select(self, strElement, value, by='xpath'):
        """
        选择下拉框控件中的某个值
        Args：
            strElement：下拉框控件的路径
            value:下拉框中字段的路径
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        Return：
            None
        """
        self.driver.find_element(by, strElement).click()
        sleep(3)
        self.driver.find_element(by, value).click()

    @wrapper
    def refresh(self):
        """
        刷新页面
        """
        self.driver.refresh()

    @wrapper
    def keys_enter(self, strElement, by='xpath'):
        """
        点击键盘的“enter"键
        Args：
            strElement：控件
            by：定位控件方式，支持id/xpath/link text/partial link text/name/tag name/class/name/css selector
        Return：
            None
        """
        ele = self.driver.find_element(by, strElement)
        self.driver.execture_script("arguments[0].click()", ele)

    @waitLoading
    @wrapper
    def inputByYourSee(self, lookupValue, inputValue, idx=1):
        """
        根据输入框标签输入
        Args:
            lookupValue:输入框标签
            inputValue:输入内容
            idx:控件顺序，从1开始
        Return:
            None
        """
        self.driver.switch_to_default_content()
        e = self.__getElementByOneConditions("input", lookupValue)[idx - 1]
        self.__switch_to_frame(e[0])
        if 'ui-spinner' in e[1].get_attribute('outerHTML'):
            e[1].send_keys(Keys.CONTROL, 'a')
        else:
            e[1].clear()
        e[1].send_keys(inputValue)

    @waitLoading
    @wrapper
    def clickByYourSee(self, lookupValue, idx=1):
        """
        根据按钮名称点击
        Args:
            lookupValue:按钮名称
            idx:控件顺序，从1开始
        Return:
            None
        """
        self.driver.switch_to_default_content()
        tmp = lookupValue.split('>')
        if len(tmp) == 2:
            btn1 = tmp[0]
            btn2 = tmp[1]
            self.clickByYourSee(btn2, idx)
        else:
            btn1 = tmp[0]
            e = self.__getElementByOneConditions('button', btn1)[idx - 1]
            self.__switch_to_frame(e[0])
            e[1].click()
            sleep(1)
            # if len(tmp) == 2:
            #     self.clickByYourSee(btn2, idx)

    @waitLoading
    @wrapper
    def chooseDateByYourSee(self, lookupValue, idx=1):
        """
        根据按钮名称点击
        Args:
            lookupValue:按钮名称
            idx:控件顺序，从1开始
        Return:
            None
        """
        self.driver.switch_to_default_content()
        e = self.__getElementByOneConditions("date", lookupValue)[idx - 1]
        self.__switch_to_frame(e[0])
        e[1].click()
        sleep(1)

    @waitLoading
    @wrapper
    def menuClickByYourSee(self, lookupValue, idx=1):
        """
        根据菜名名称单点
        Args:
            lookupValue:菜单名称，多级菜单用>隔开
            idx:控件顺序，从1开始
        Return:
            None
        """
        self.driver.switch_to_default_content()
        tmp = lookupValue.split('>')
        if len(tmp) == 2:
            lookupValue2 = tmp[1]
            e = self.__getElementByOneConditions("menu", tmp[0])[idx - 1]
            self.__switch_to_frame(e[0])
            ActionChains(self.driver).move_to_element(e[1]).perform()
            if len(tmp) == 2:
                self.menuClickByYourSee(lookupValue2, idx)
            else:
                e[1].click()
                sleep(1)

    @waitLoading
    @wrapper
    def selectByYourSee(self, lookupValue1, lookupValue2, idx=1):
        """
        根据下拉列表标签选择选项
        Args:
            lookupValue1:下拉列表标签
            lookupValue2:选择选项
            idx:控件顺序，从1开始
        Return:
            None
        """
        self.driver.switch_to_default_content()
        e = self.__getElementByTwoConditions("select", lookupValue1, lookupValue2)[idx - 1]
        self.__switch_to_frame(e[0])
        if e[1].get_attribute('nodeName').lower() == 'select':
            Select(e[1]).select_by_visible_text(lookupValue2)
        elif e[1].get_attribute('nodeName').lower() == 'input':
            e[1].send_keys(lookupValue2)
        else:
            sleep(1)
            ActionChains(self.driver).move_to_element(e[1]).perform()
            e[1].click()

    @waitLoading
    @wrapper
    def radioByYourSee(self, lookupValue, idx=1):
        """
        根据单选框标签选择选项
        Args:
            lookupValue:单选框标签
            idx:控件顺序，从1开始
        Return:
            None
        """
        self.driver.switch_to_default_content()
        e = self.__getElementByOneConditions("radio", lookupValue)[idx - 1]
        self.__switch_to_frame(e[0])
        e[1].click()

    @waitLoading
    @wrapper
    def checkboxByYourSee(self, lookupValue, is_check, idx=1):
        """
        根据选择框标签选择选项
        Args:
            lookupValue:选择框标签
            is_check:勾选/去勾选
            idx:控件顺序，从1开始
        Return：
            None
        """
        self.driver.switch_to_default_content()
        for i in lookupValue.split("|"):
            e = self.__getElementByOneConditions("checkbox", i)[idx - 1]
            self.__switch_to_frame(e[0])
            if int(is_check) == 1:
                if not e[1].is_selected():
                    ActionChains(self.driver).click(e[1]).perform()
            elif int(is_check) == 0:
                if not e[1].is_selected():
                    ActionChains(self.driver).click(e[1]).perform()
            else:
                assert False, "invalid is_check"

    @waitLoading
    @wrapper
    def clickTableByYourSee(self, lookupValue, colldx, buttonText, idx=1):
        """
        根据表格中的按钮名称点击表格按钮
        Args:
            lookupValue:定位内容
            colldx:按钮所在列（从1开始）
            buttonText:表格中按钮名称
            idx:控件顺序，从1开始
        Return：
            None
        """
        self.driver.switch_to_default_content()
        if '>' in buttonText:
            tmp = buttonText.split('>')
            b1 = tmp[0]
            b2 = tmp[1]
            e = self.__getElementByTwoConditions("tableClick", lookupValue, colldx)[idx - 1]
            self.__switch_to_frame(e[0])
            if len(b1) == 0:
                e[1].find_element('xpath', './/button').click()
            else:
                e[1].find_element('xpath', './/*[text()="%s"]' % b1).click()
                g = self._getElementByOneConditions("button", b2)[idx - 1]
                self.__switch_to_frame(g[0])
                g[1].click()
        else:
            e = self.__getElementByTwoConditions("tableClick", lookupValue, colldx)[idx - 1]
            self.__switch_to_frame(e[0])
            f = e[1].find_element('xpath', './/*[text()="%s"]' % buttonText)
            f.click()

    @waitLoading
    @wrapper
    def inputTableByYourSee(self, lookupValue, colldx, inputValue, idx=1):
        """
        根据表格中输入框名称输入
        Args:
            lookupValue:定位内容
            colldx:按钮所在列，从1开始
            inputValue:表格中的输入框名称
            idx：控件顺序，从1开始
        Return：
            None
        """
        self.driver.switch_to_default_content()
        e = self.__getElementByTwoConditions("tableInput", lookupValue, colldx)[idx - 1]
        self.__switch_to_frame(e[0])
        if 'ui-spinner' in e[1].get_attribute('outerHTML'):
            e[1].send_keys(Keys.CONTROL, 'a')
        else:
            e[1].clear()
        e[1].send_keys(inputValue)

    @waitLoading
    @wrapper
    def selectInTableByYourSee(self, lookupValue1, colldx, lookupValue2, idx=1):
        """
        根据表格中下拉列表选择
        Args:
            lookupValue1:定位内容
            lookupValue2:选择项
            colldx:按钮所在列，从1开始
            idx：控件顺序，从1开始
        Return：
            None
        """
        self.driver.switch_to_default_content()
        e = self.__getElementByTwoConditions("tableSelect", lookupValue1, colldx)[idx - 1]
        self.__switch_to_frame(e[0])
        if 'editable="editable"' in e[1].get_attribute('outerHTML'):
            f = e[1].find_element('xpath', '//p-dropdown/div/input')
            f.send_keys(lookupValue2)
        else:
            e[1].click()
            f = e[1].find_element('xpath', '//*[text()="%s"]' % lookupValue2)
            f.click()

    @waitLoading
    @wrapper
    def checkboxInTableByYourSee(self, lookupValue, colldx, is_check, is_header=False, idx=1):
        """
        根据选择框标勾选/去勾选
        Args:
            lookupValue:定位内容
            colldx:按钮所在列，从1开始
            is_check:勾选/去勾选
            idx:控件顺序，从1开始
        Return：
            None
        """
        self.driver.switch_to_default_content()
        for i in lookupValue.split("|"):
            if is_header:
                e = self.__getElementByTwoConditions("tableHeaderCheckbox", i, colldx)[idx - 1]
                self.__switch_to_frame(e[0])
                if is_check != (e[1].is_selected()):
                    e[1].click()

    @waitLoading
    @wrapper
    def getTableByYourSee(self, lookupValue, colldx, idx=1):
        """
        根据表格中下拉列表选择
        Args:
            lookupValue:定位内容
            colldx:按钮所从1开始在列，
            idx：控件顺序，从1开始
        Return：
            None
        """
        self.driver.switch_to_default_content()
        e = self.__getElementByTwoConditions("tableGet", lookupValue, colldx)[idx - 1]
        self.__switch_to_frame(e[0])
        return e[1].text

    @waitLoading
    @wrapper
    def uploadByYourSee(self, lookupValue, filepath, buttonText, idx=1):
        """
        根据表格中下拉列表选择
        Args:
            lookupValue:定位内容
            filepath:上传文件路径，如‘c:\\abc.xls’
            buttonText：上传按钮文本
            idx：控件顺序，从1开始
        Return：
            None
        """
        self.driver.switch_to_default_content()
        self.inputByYourSee(lookupValue, filepath, idx)
        self.clickByYourSee(buttonText, idx)

    @wrapper
    def waitAppearByYourSee(self, lookupValue, time=60):
        """
        等待人界面看到的内容出现
        Args:
            lookupValue:文本
            time:等待时长
        Return：
            None
        """
        assert self.waitAppear('//*[text()="%s"]' % lookupValue, int(time)), '等待%s出现失败' % lookupValue

    @wrapper
    def byvaluefindElement(self, value):
        """
        通过value定位任务，判断任务是否完成
        Args:
            value:task的value值
        Return：
            任务状态
        """
        driver = self.driver
        task_state = driver.find_element('xpath', '//*[@id="tk-tbl"]//tr//input[@value="%s"]/../../../td[6]' % (value))[
            0].text
        return task_state

    @wrapper
    def gettableValue(self, strElement, strValue, by='xpath'):
        """
        输入框中的输入内容
        Args:
            strElement:输入的对象
            strValue:输入的内容
        Return:
            返回输入值
        """
        pass

    # @wrapper
    # def __getElementByTwoConditions(self, elementType, lookValue1, lookValue2_or_colldx, iFrameName='main'):
    #     """
    #     获取人界面看到的内容定位控件
    #     Args:
    #         elementType:控件类型
    #         lookValue1:搜寻文本1
    #         lookValue2_or_colldx:搜寻文本2或列索引
    #         iFrameName:iFrame 名称
    #     return:
    #         控件
    #     """
    #     listFindElement = []
    #     if elementType.startswith('table'):
    #         if 'Header' in elementType:
    #             xpath = '//tr//*[text()="%s"]' % lookValue1
    #         else:
    #             xpath = '//td//*[text()="%s"]' % lookValue1
    #     else:
    #         xpath = '//*[text()="%s"]' % lookValue1
    #     list_nodeName = []
    #     for item in [i for i in self.driver.find_elements('xpath', xpath) if i.is_displayed()]:
    #         nodeName = item.get_attribute('nodeName')
    #         if nodeName not in list_nodeName:
    #             list_nodeName.append(nodeName)
    #     for nodeName in list_nodeName:
    #         if elementType.startswith('table'):
    #             if 'Header' in elementType:
    #                 xpath = '//tr//%s[text()="%s"]/parent::*' % (nodeName, lookValue1)
    #             else:
    #                 xpath = '//td//%s[text()="%s"]/parent::*' % (nodeName, lookValue1)
    #         else:
    #             xpath = '//%s[text()="%s"]/parent::*' % (nodeName, lookValue1)
    #         for item in [i for i in self.driver.find_elements('xpath', xpath) if i.is_displayed()]:
    #             if elementType == 'select':
    #                 try:
    #                     e = item.find_element('xpath', './/p-dropdown')
    #                 except:
    #                     try:
    #                         e = item.find_element('xpath', './parent::*/div//p-dropdown')
    #                     except:
    #                         try:
    #                             e = item.find_element('xpath', './parent::*/parent::*//p-dropdown')
    #                         except:
    #                             continue
    #             if 'editable="editable"' in e.get_atttribute('outerHTML'):
    #                 f = e.find_element('xpath', './div/input')
    #                 listFindElement.append([iFrameName, f])
    #             else:
    #                 e.click()
    #                 e = item.find_element('xpath', '//*[text()="%s"]' % lookValue2_or_colldx)
    #                 listFindElement.append([iFrameName, e])
    #                 self.log('Find %s %s using xpath:%s %s in the %s iframe' % (
    #                 elementType, lookValue2_or_colldx, item, xpath, iFrameName))
    #     elif elementType == 'tableinput':
    #     xpath =


browser = Broswer(screeshotSaveName='screenshot', ASSERT_IF_FAIL=True, DEBUG=True)
