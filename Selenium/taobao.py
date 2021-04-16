from selenium import webdriver

# 打开Chrome浏览器
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
browser.find_element_by_link_text("亲，请登录").click()
# 等待3秒(隐性等待)
browser.implicitly_wait(3)
# 输入会员/邮箱/手机号
browser.find_element('xpath', '//*[@id="fm-login-id"]').send_keys("cpci")
# 请输入登录密码
browser.find_element('xpath', '//*[@id="fm-login-password"]').send_keys("cpci")
# 点击登录
browser.find_element('xpath', '//*[@id="login-form"]/div[4]/button').click()
# 等待3秒(隐性等待)
browser.implicitly_wait(3)
# 在搜索框输入
browser.find_element_by_id("J_search_key").send_keys('口红')
# 点击搜索按钮
browser.find_element_by_xpath('//*[@id="J_searchForm"]/input').click()
# 点击第一个商品口红
browser.find_element_by_xpath('//*[@id="mx_5"]/ul/li[1]/a/img').click()
# 选择颜色分类的第一个N37型号
browser.find_element_by_xpath('//*[@id="J_DetailMeta"]//div[4]//dl[1]//li[1]/a/span').click()
# 点击立即购买
browser.find_element_by_id("J_LinkBuy").click()
# 等待3秒(隐性等待)
browser.implicitly_wait(3)
# 点击提交订单按钮
try:
    if browser.find_element_by_link_text('提交订单'):
        browser.find_element_by_link_text('提交订单').click()
        print("请尽快付款")
except:
    print("再次尝试提交订单")
# 等待3秒(隐性等待)
browser.implicitly_wait(10)
# 选择付款方式
browser.find_element_by_xpath('//*[@id="J_SavecardList"]/li[1]/div[1]/label').click()
#输入支付宝支付密码()
browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[1]').send_keys('1')
browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[2]').send_keys('2')
browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[3]').send_keys('3')
browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[4]').send_keys('4')
browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[5]').send_keys('5')
browser.find_element_by_xpath('//*[@id="payPassword_container"]/div/i[6]').send_keys('6')

# 点击确定
browser.find_element_by_id("J_authSubmit").click()
