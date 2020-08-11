#  标准库模块
#------时间
import time
#1558401723.1319582
#时间戳:从1970年后经过的秒数
print(time.time())

#时间戳---->时间元组
#time.struct_time(tm_year=2019, tm_mon=5, tm_mday=21, tm_hour=9, tm_min=22, tm_sec=3, tm_wday=1, tm_yday=141, tm_isdst=0)
#年  月   日   时   分   秒   星期(周一0　周二1　周日6) 一年的第几天　　夏令时
print(time.localtime(1558401723.1319582))
for item in time.localtime(1558401723.1319582):
    print(item)
tuple_time=time.localtime(1558401723.1319582)
print(tuple_time)
# 时间元组--->str
#   年/月/日   小时:分钟:秒
print(time.strftime("%y/%m/%d %H/%M/%S",tuple_time))#19/05/21 09/22/03
print(time.strftime("%Y/%m/%d %H/%M/%S",tuple_time))#2019/05/21 09/22/03

#str--->时间元组
print(time.strptime("2019-05-21","%Y-%m-%d"))

#时间元组---->时间戳
print(time.mktime(tuple_time))#1558401723.0

#练习:定义函数,根据年月日,返回星期几
#星期一　　星期二....星期日
import time
def get_week(year,month,day):
    tuple_time=time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
    dict_week={
        0:"星期一",
        1:"星期二",
        2:"星期三",
        3:"星期四",
        4:"星期五",
        5:"星期六",
        6:"星期日",
    }
    return  dict_week[tuple_time[6]]
#测试
print(get_week(2019,5,21))

#练习:根据生日(年月日)计算活了多少天
import time
print(time.time())
def fun(year, month, day):
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    result=time.time()-time.mktime(tuple_time)
    return result/3600//24
print(fun(2000,8,15))


#导入
#from 包名 import 模块名 [as 模块新名]
#from 包名.子包名 import 模块名 [as 模块新名]
#from 包名.子包名.模块名 import 成员名 [as 属性新名]
#
# 导入包内的所有子包和模块
#from 包名 import *
#from 包名.模块名 import *

"""
  包

python 程序结构
包(文件夹)
  模块(文件)
    类
      函数
        语句
"""

#练习:定义函数,在控制台中获取成绩(1~100)
#     如果输入有误请重新输入
def score():
    while True:
        score=float(input("请输入一个成绩"))
        try:
            int_score=int(score)
        except ValueError:
            continue
        if 1<=score<=100:
            return int_score
print(score())
"""
  异常处理
"""
def div_apple(apple_count):
  """
    分苹果
  """
  # ValueError
  person_count = int(input("请输入人数:"))
  # ZeroDivisionError
  result = apple_count / person_count
  print("每人分到%d个苹果" % result)

# 测试
try:
  div_apple(10)
except:
  print("通用的处理逻辑")
try:
  div_apple(10)
except Exception:
  print("通用的处理逻辑")

try:
  div_apple(10)
except ValueError:
  print("输入的数据应该是整数")
except ZeroDivisionError:
  print("分母不能是0")
except Exception:
  print("未知错误")
else:
  # 没有异常时执行
  print("分苹果成功喽")
finally:
  print("无论是否发生异常,都执行的代码.")
print("后续逻辑.....")

# 练习:
# 对下列代码进行异常处理.
dict_commodity_info = {
  101: {"name": "屠龙刀", "price": 10000},
  102: {"name": "倚天剑", "price": 10000},
  103: {"name": "九阴白骨爪", "price": 8000},
  104: {"name": "九阳神功", "price": 9000},
  105: {"name": "降龙十八掌", "price": 8000},
  106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def buying():
  """
    购买
  """
  print_commodity()
  dict_order = create_order()
  list_order.append(dict_order)
  print("添加到购物车。")

def input_number(str_msg):
  while True:
    try:
      number = int(input(str_msg))
      return number
    except:
      print("输入有误")

def create_order():
  """
    创建订单
  :return: 订单 字典类型{"cid": 商品编号, "count": 数量}
  """
  while True:
    # cid = int(input("请输入商品编号："))
    cid = input_number("请输入商品编号：")
    if cid in dict_commodity_info:
      break
    else:
      print("该商品不存在")
  # count = int(input("请输入购买数量："))
  count = input_number("请输入购买数量：")
  return {"cid": cid, "count": count}

def print_commodity():
  for key, value in dict_commodity_info.items():
    print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))

def select_menu():
  """
     菜单选择
  :return:
  """
  while True:
    item = input("1键购买，2键结算。")
    if item == "1":
      buying()
    elif item == "2":
      settlement()

def settlement():
  """
    结算
  :return:
  """
  print_order()
  total_money = get_total_money()
  pay(total_money)

def pay(total_money):
  """
    购买
  :param total_money:
  :return:
  """
  while True:
    money = float(input("总价%d元，请输入金额：" % total_money))
    if money >= total_money:
      print("购买成功，找回：%d元。" % (money - total_money))
      list_order.clear()
      break
    else:
      print("金额不足.")

def print_order():
  """
    打印订单
  """
  for item in list_order:
    commodity = dict_commodity_info[item["cid"]]
    print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))

def get_total_money():
  """
    获取总价
  :return:
  """
  total_money = 0
  for item in list_order:
    commodity = dict_commodity_info[item["cid"]]
    total_money += commodity["price"] * item["count"]
  return total_money

# 程序入口
select_menu()