#生成器表达式
#   1. 定义:用推导式形式创建生成器对象
#   2. 语法:变量 = ( 表达式 for 变量 in 可迭代对象 if 真值表达式)

list=[5,656,32,241,456]
#立即执行,将所有结果存入内存
result=[item for item in list if item>30]
for item in result:
    print(item)
list=[5,656,32,241,456]
#返回执行,循环一次,计算一次,返回一个(覆盖了上一个)
result=(item for item in list  if item>30  )
for item in result:
    print(item)

#函数式编程
#1. 定义:用一系列函数解决问题
#-- 函数可以赋值给变量,赋值后变量绑定函数
#-- 允许将函数作为参数传入另一个函数
#-- 允许函数返回一个函数
#2. 高阶函数:将函数作为参数或返回值的函数
"""
  函数式编程
  -- 函数作为参数
"""
def fun01():
  print("fun01执行执行喽")

# 有小括号,是调函数,a变量得到是函数返回值
#a = fun01()
# 没小括号,没调函数,a变量得到是函数地址
#a = fun01
# 通过变量a,调用函数fun01.
#a()

def fun03():
  print("fun03执行执行喽")

def fun04():# 定义很多具体函数  [封装]
  print("fun04执行执行喽")

# func 代表(抽象) fun01 fun03  fun04  [继承]
def fun02(func):
  print("fun02的逻辑")
  func()# 调用func执行....  [多态]

fun02(fun01)
fun02(fun03)
fun02(fun04)
"""
  函数作为参数的案例
"""
list01 = [43, 4, 55, 56, 6, 67, 8]

# --------------封装-------------------
# 功能1:查找列表中所有偶数
def find01(list_targt):
  for item in list_targt:
    if item % 2 == 0:
      yield item

# 功能2:查找列表中所有大于5的数
def find02(list_targt):
  for item in list_targt:
    if item > 5:
      yield item

# 功能3:查找列表中所有小于40的数
def find03(list_targt):
  for item in list_targt:
    if item < 40:
      yield item

# --------------继承-------------------
# 提取变化点
def condition01(item):
  return item % 2 == 0

def condition02(item):
  return item > 5

def condition03(item):
  return item < 40

# 定义不变的
def find(list_targt, func_condition):
  for item in list_targt:
    # if item < 40:
    # if condition03(item):
    if func_condition(item):  # ----------多态------------
      yield item

for item in find(list01,condition03):
  print(item)

#练习:定义技能类(技能名称,攻击力,冷却时间,攻击速度)
#封装:功能1:获取冷却时间为0的所有技能
#    功能2:获取攻击力大于10的所有技能
#    功能3:获取攻击速度小于5的所有技能
#继承:提取变化点
#    定义不变的代码(客户源代码)
#    测试最后再实现3个功能
class Skill:
    def __init__(self, name, attack, time, speed):
        self.name=name
        self.attack=attack
        self.time=time
        self.speed=speed

list=[
    Skill("打狗棍",10,0,3),
    Skill("降龙十八掌",10,10,15),
    Skill("蛤蟆功",15,15,10)
]
def fun01(list):
    for item in list:
        if item.time==0:
            yield item

def fun02(list):
    for item in list:
        if item.attack>10:
            yield item

def fun03(list):
    for item in list:
        if item.speed<5:
            yield item

def condition01(item):
    return item.time==0

def condition02(item):
    return item.attack>10

def condition03(item):
    return item.speed<5

def find(list,func):
  for item in list:
    if func(item):
      yield item

for item in find(list,condition02):
  print(item.name)
"""
lambda 表达式
1. 定义:是一种匿名方法
2. 作用:作为参数传递时语法简洁优雅,代码可读性强,随时创建和销毁,减少程序耦合度
3. 语法
-- 定义:
       变量 = lambda 形参: 方法体
-- 调用:
		变量(实参)
4. 说明:形参没有可以不填,方法体只能有一条语句,且不支持赋值语句
"""
class Skill:
    def __init__(self, name, attack, time, speed):
        self.name=name
        self.attack=attack
        self.time=time
        self.speed=speed

list=[
    Skill("打狗棍",10,0,3),
    Skill("降龙十八掌",10,10,15),
    Skill("蛤蟆功",15,15,10)
]

def fun01(list):
    for item in list:
        if item.time==0:
            yield item

def fun02(list):
    for item in list:
        if item.attack>10:
            yield item

def fun03(list):
    for item in list:
        if item.speed<5:
            yield item

#def condition01(item):
#    return item.time==0
a=lambda item:item.time==0

#def condition02(item):
#    return item.attack>10
b=lambda item:item.attack>10

#def condition03(item):
#    return item.speed<5
c=lambda item:item.speed<5

def find(list,func_condition):
  for item in list:
    if func_condition(item):
      yield item

for item in find(list,a):
  print(item.name)





from day18.common.list_helper import ListHelper

class Skill:
    def __init__(self, name, attack, time, speed):
        self.name = name
        self.attack = attack
        self.time = time
        self.speed = speed

list = [
    Skill("打狗棍", 10, 0, 3),
    Skill("降龙十八掌", 10, 10, 15),
    Skill("蛤蟆功", 15, 15, 10)
]
for item in ListHelper.find(list, lambda e: e.attack > 5):
    print(item.name)
"""
练习:
    功能1:定义函数,在列表中查找"打狗棍"技能.
    功能2:定义函数,在列表中查找攻击力大于10的单个技能.
    功能3:定义函数,在列表中查找time大于0的单个技能.
    ...
    最终:将通用代码定义在list_helper.py中
         将变化点使用lambda表示
"""
class Skill:
    def __init__(self, name, attack, time, speed):
        self.name = name
        self.attack = attack
        self.time = time
        self.speed = speed

list = [
    Skill("打狗棍", 10, 0, 3),
    Skill("降龙十八掌", 10, 10, 15),
    Skill("蛤蟆功", 15, 15, 10)]

def fun01(list):
    for itme in list:
        if item.name == "打狗棍":
            return item

def fun02(list):
    for itme in list:
        if item.attack > 10:
            return item

def fun03(list):
    for itme in list:
        if item.time > 0:
            return item

def find(list, func_condition):
    for item in list:
        if func_condition(item):
            yield item

for item in find(list, lambda item: item.time > 0):
    print(item.name)

class Skill:
    def __init__(self, name, attack, time, speed):
        self.name = name
        self.attack = attack
        self.time = time
        self.speed = speed

list = [
    Skill("打狗棍", 10, 0, 3),
    Skill("降龙十八掌", 10, 10, 15),
    Skill("蛤蟆功", 15, 15, 10)]

def fun01(list):
    for item in list:
        if item.attack > 10:
            yield item

def fun02(list):
    for item in list:
        if item.time > 0:
            yield item

def find(list, func_condition):
    for item in list:
        if func_condition(item):
            yield item

for item in find(list, lambda item: item.time > 0):
    print(item.name)

"""  
内置高阶函数
    1. map（函数,可迭代对象）:使用可迭代对象中的每个元素调用函数,将返回值作为新可迭代对象元素;返回值为新可迭代对象.
    2. filter(函数,可迭代对象):根据条件筛选可迭代对象中的元素,返回值为新可迭代对象.
    3. sorted(可迭代对象,key = 函数,reverse = bool值)：排序,返回值为排序结果.
    4. max(可迭代对象,key = 函数):根据函数获取可迭代对象的最大值.
    5. min(可迭代对象,key = 函数):根据函数获取可迭代对象的最小值.
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
  SkillData("一阳指", 20, 80, 80)
]

# 练习1: 查找技能列表中攻击力在50 - -100 之间的所有技能.
for item in filter(lambda e:50 <= e.atk <= 100,list01):
  print(item.atk)

# 练习2: 在技能列表中, 获取技能名称与cd的列表.
# list --> 惰性操作 转换为 立即操作
result = map(lambda e:(e.name,e.cd),list01)
print(result)

# 练习3: 在列能列表中, 查找攻击速度最小的技能
result = min(list01,key = lambda e:e.atk_speed)
print(result.name)

# 练习4: 根据cd对象技能列表进行降序排列.
result = sorted(list01,key = lambda  e:e.cd,reverse= True)
# sorted 不会改变原来的列表,而是返回新列表.
# 如果需要改变原来的列表,需要通过切片定位元素,再进行修改.
list01[:] = result
for item in list01:
  print(item.cd)

# 练习5: 在技能列表中, 查找名称最长的技能.
result = max(list01,key = lambda e:len(e.name))
print(result.name)

"""
 Enclosing  外部嵌套作用域 ：函数嵌套。
"""

def fun01():
  a = 1  # 对于fun02 而言,属于外部嵌套作用域

  def fun02():
    b = 2
    # print(a)# 可以直接访问外部嵌套变量
    # a = 111 # 又创建了局部变量a,没有修改外部嵌套变量.
    nonlocal a  # 声明外部嵌套变量
    a = 111
    print(a)

  fun02()
  print(a)

fun01()

"""
  闭包
    1. 三要素:
-- 必须有一个内嵌函数
-- 内嵌函数必须引用外部函数中变量
-- 外部函数返回值必须是内嵌函数
    2. 语法
-- 定义:
def 外部函数名(参数):
		外部变量
		def 内部函数名(参数):
			使用外部变量
		return 内部函数名
-- 调用:
	   变量 = 外部函数名(参数)
	   变量(参数)
    3. 定义:在一个函数内部的函数,同时内部函数又引用了外部函数的变量
    4. 本质:闭包是将内部函数和外部函数的执行环境绑定在一起的对象
    5. 优点:内部函数可以使用外部变量 
    6. 缺点:外部变量一直存在于内存中,不会在调用结束后释放,占用内存
    7. 作用:实现python装饰器
"""
def fun01():
  a = 1  # 对于fun02 而言,属于外部嵌套作用域

  def fun02():
    print(a)

  return fun02
# 闭包:
# 内部函数可以使用外部嵌套变量,外部函数执行完毕后,
# 没有释放内存,而是等待内部函数执行结束.
func = fun01()# 调用外部函数
func()# 再调用内部函数

#案例:
# 压岁钱
def give_gife_money(money):
  """
    获取压岁钱
  """
  print("得到压岁钱:",money)
  def child_buy(target,price):
    """
      孩子需要买东西
    """
    nonlocal money
    if money >=  price:
      money -= price
      print("孩子需要花%d钱,买%s"%(price,target))
    else:
      print("钱不够")
  # 希望外部可以调用内部函数
  return child_buy

action_buy = give_gife_money(30000)
action_buy("飞机",1000)
action_buy("手机",10000)
action_buy("房子",10000000)

