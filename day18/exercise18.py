"""
  练习1:
    将通用函数定义在list_helper.py模块中
    在当前模块中,测试find.

  练习2:
    功能1:定义函数,在列表中查找"如来神掌"技能.
    功能2:定义函数,在列表中查找攻击力大于50的单个技能.
    功能3:定义函数,在列表中查找cd大于0的单个技能.
    ...
    最终:将通用代码定义在list_helper.py中
         将变化点使用lambda表示

  练习3:
    功能1:定义函数,在列表中计算攻击力小于50的技能数量.
    功能2:定义函数,在列表中查找cd等于0的技能数量.
    ...
    最终:将通用代码定义在list_helper.py中
         将变化点使用lambda表示

  练习4:
    功能1:定义函数,在列表中计算攻击力的总和.
    功能2:定义函数,在列表中计算速度的总和.
    ...
    最终:将通用代码定义在list_helper.py中
         将变化点使用lambda表示
  练习5:
    功能1:定义函数,在列表中获取攻击力最大的技能.
    功能2:定义函数,在列表中计算速度最大的技能.
    ...
    最终:将通用代码定义在list_helper.py中
         将变化点使用lambda表示

  练习6:
    功能1:定义函数,根据技能列表获取攻击力列表.
    功能2:定义函数,根据技能列表获取技能名称列表.
    17:28

  练习7:
    功能1:定义函数,对技能列表根据攻击力进行升序排列.
    功能2:定义函数,对技能列表根据攻击速度进行升序排列.
"""
from day18.common.list_helper import ListHelper


class SkillData:
  def __init__(self, name, atk, cd, speed):
    self.name = name
    self.atk = atk
    self.cd = cd
    self.atk_speed = speed


list01 = [
  SkillData("降龙十八掌", 100, 60, 50),
  SkillData("如来神掌", 80, 50, 30),
  SkillData("一阳指", 20, 0, 80)
]

# 练习1
for item in ListHelper.find(list01, lambda e: e.atk > 50):
  print(item.name)


# 练习2
"""
# 功能1:定义函数,在列表中查找"如来神掌"技能.
def find01(list_target):
  for item in list_target:
    if item.name == "如来神掌":
      return item
# 功能2:定义函数,在列表中查找攻击力大于50的单个技能.
def find02(list_target):
  for item in list_target:
    if item.atk > 50:
      return item
# 功能3:定义函数,在列表中查找cd大于0的单个技能.
def find03(list_target):
  for item in list_target:
    if item.cd == 0:
      return item

def condition01(item):
  return item.name == "如来神掌"

def condition02(item):
  return item.atk > 50

def condition03(item):
  return item.cd == 0

def first(list_target,func_condition):
  for item in list_target:
    # if item.cd == 0:
    # if condition03(item):
    if func_condition(item):
      return item
"""
result = ListHelper.first(list01,lambda e:e.name == "如来神掌")
print(result.name)

# 练习3
"""
def get_count01(list_target):
  count_value = 0
  for item in list_target:
    if item.atk < 50:
      count_value +=1
  return count_value

def get_count02(list_target):
  count_value = 0
  for item in list_target:
    if item.cd ==0:
      count_value +=1
  return count_value

def condition01(item):
  return item.atk < 50

def condition02(item):
  return item.cd ==0

def get_count(list_target,func_condition):
  count_value = 0
  for item in list_target:
    if func_condition(item):
      count_value +=1
  return count_value
"""
count =ListHelper.get_count(list01,lambda e:e.atk <50)
print(count)

# 练习4
# 功能1: 定义函数, 在列表中计算攻击力的总和.
# 功能2: 定义函数, 在列表中计算速度的总和.
"""
def sum01(list_target):
  sum_value = 0
  for item in list_target:
    sum_value += item.atk
  return sum_value

def sum02(list_target):
  sum_value = 0
  for item in list_target:
    sum_value += item.atk_speed
  return sum_value

def sum(list_target,func_handle):
  sum_value = 0
  for item in list_target:
    sum_value += func_handle(item)
  return sum_value
"""
result = ListHelper.sum(list01,lambda e:e.atk)
print(result)

# 练习5:
result = ListHelper.get_max(list01,lambda e:e.atk)
print(result.name)

# 练习6:
result = ListHelper.select(list01,lambda e:{e.name:e.atk})
print(result)

# 练习7:
ListHelper.order_by(list01,lambda e:e.atk)
for item in list01:
  print(item.atk)

"""
  day18 复习
  函数式编程
    函数作为参数
      将核心逻辑传入方法体，使该方法的适用性更广，体现了面向对象的开闭原则。
      lambda 表达式:匿名方法,作为参数传递时特别优雅.
      设计思想:
        "封装"
            功能1...
            功能2...
            功能3...
        "继承"
            提取变化点(一个函数处理一个变化的逻辑)
            定义通用函数(形参代表/抽象变化的函数)
        "多态"
            在通用的函数中,通过调用形参,执行实参(变化点).
      内置高阶函数:ListHelper类都包含了(跨语言的编程思想,还可以无限扩展).
                 参照了微软Linq框架思想.
    函数作为返回值
      闭包:语法上讲,外部函数执行完毕后,不会立即释放栈帧,而是等着内部函数执行完毕后,再释放.
          设计上讲,为了让逻辑连续(外部与内部函数逻辑持续).
        def 外部函数():
          变量
          def 内部函数():
             使用外部变量
          return 内部函数

        变量 = 外部函数()
        变量()
      闭包应用:装饰器
"""
# find : 查找列表中符合条件的元素
# a:列表
# b:条件
def fun01(a,b):
  pass

def fun02():
  pass

# 将数据(100)传入方法fun01中
# 将逻辑(fun02)传入方法fun01中
# 目的:让数据与逻辑随意变化,不影响通用的方法(find..).
fun01(100,fun02)
fun01(100,lambda :"返回的数据")






