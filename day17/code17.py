#raise 语句
#1. 作用:抛出一个错误,让程序进入异常状态
#2. 目的:在程序调用层数较深时,向主调函数传递错误信息要层层return 比较麻烦,
#  所以人为抛出异常,可以直接传递错误信息.
#自定义异常
#1. 定义：
#class 类名Error(Exception):
#   def __init__(self,参数):
#       super().__init__(参数)
#       self.数据 = 参数
#2. 调用：
#try:
#….
#raise 自定义异常类名(参数)
#….
# except 定义异常类 as 变量名:
#       变量名.数据
#3. 作用：封装错误信息
"""
  主动抛出异常
  自定义异常类
  体会:抛出异常 与 接收异常信息
"""
class AgeError(Exception):
  def __init__(self, value, str_msg, code):
    super().__init__(str_msg)
    self.age_value = value
    self.msg = str_msg
    self.code = code

class Wife:
  def __init__(self, age):
    self.age = age

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, value):
    if 22 <= value <= 30:
      self.__age = value
    else:
      # 将错误信息传递给创建Wife对象的代码
      # 需求:传递的错误信息有很多.
      # raise Exception("我不要")
      raise AgeError(value, "年龄不在范围内", "self.__age = value")

# w01 = Wife(50)
try:
  w01 = Wife(50)
except AgeError as e:
  print("错误提示:", e.msg)
  print("错误数值:", e.age_value)
  print("错误代码:", e.code)
# 练习:
class WeightError(Exception):
    def __init__(self, vaule, str_msg, code):
        super().__init__(str_msg)
        self.weight_vaule = vaule
        self.msg = str_msg
        self.code = code

class Wife():
    def __init__(self, weight):
        self.weight = weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, vaule):
        if 50 <= vaule <= 60:
            self.__weight = vaule
        else:
            raise WeightError(vaule, "体重不在范围内", "self.__weight=vaule")

try:
    w01 = Wife(65)
except WeightError as a:
    print("错误", a.msg)
    print("错误", a.weight_vaule)
    print("错误", a.code)

#可迭代对象iterable 
#1. 定义：具有__iter__函数的对象，可以返回迭代器对象。
#2. 语法
#-- 创建：
#class 可迭代对象名称:
#  def __iter__(self):
#      return 迭代器
#-- 使用：
#  for 变量名 in 可迭代对象:
#语句
#3. 原理：
#迭代器 = 可迭代对象.__iter__()
#while True:
#   try:
#       print(迭代器.__next__())
#   except StopIteration:
#       		break

# 面试题:可以被for的条件? 对象具有__iter__()方法
list01 = [4, 543, 565, 45, 365, 41, 54]
# for原理:
# 1.获取迭代对象
iterator = list01.__iter__()
# 2.循环获取下一个元素
while True:
    try:
        item = iterator.__next__()
        print()
    # 3.异常处理
    except StopIteration:
        break

# 练习1.(4,4,54,5,45,4,565,45,45)通过迭代器获取元组元素
tuple01 = (4, 4, 54, 5, 45, 4, 565, 45, 45)
iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
# 练习2.{"张无忌":3,"赵敏":2}通过迭代器获取字典记录
dict01 = {"张无忌": 3, "赵敏": 2}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        vaule = dict01[key]
        print(key, vaule)
    except StopIteration:
        break

"""
  迭代器
"""
#代器对象iterator
#. 定义：可以被next()函数调用并返回下一个值的对象
#. 语法
#class 迭代器类名:
#   def __init__(self, 聚合对象):
#       self.聚合对象= 聚合对象

#   def __next__(self):
#       if 没有元素:
#           raise StopIteration
#           return 聚合对象元素
#. 说明：聚合对象通常是容器对象
#. 作用：使用者只需通过一种方式,便可简洁明了的获取聚合对象中各个元素,而又无需了解其内部结构。
class SkillIterator:
    """
      迭代器
    """
    def __init__(self, target):
        self.target = target
        self.index = 0

    def __next__(self):
        # 需求:将SkillManager中__list_skill的元素返回
        if self.index > len(self.target) - 1:
            raise StopIteration()

        result = self.target[self.index]
        self.index += 1
        return result

class Skill:
    pass
    # def __str__(self):
    #   return "技能"

class SkillManager:
    def __init__(self):
        self.__list_skill = []

    def add_skill(self, skill):
        self.__list_skill.append(skill)

    def __iter__(self):
        return SkillIterator(self.__list_skill)

manager = SkillManager()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())

# 目标:for 自定义类的对象
# for item in manager:
#   print(item)

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

# 练习:遍历员工管理器(私有的员工列表)
class EmployeeIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration()
        result = self.__target[self.__index]
        self.__index += 1
        return result

class Employee:
    pass

class EmployeeManager:
    def __init__(self):
        self.__list_emp = []

    def add_employee(self, emp):
        self.__list_emp.append(emp)

    def __iter__(self):
        return EmployeeIterator(self.__list_emp)

manager = EmployeeManager()
manager.add_employee(Employee())
manager.add_employee(Employee())

for item in manager:
    print(item)

# 1. 获取迭代器对象(创建迭代器对象,将manager中的数据传递给迭代器)
iterator = manager.__iter__()
while True:
    try:
        # 2. 获取下一个元素(读取元素)
        item = iterator.__next__()
        print(item)
        # 3. 异常处理
    except StopIteration:
        break


# 练习:参照下列代码,定义MyRange
# for i in range(5):
#    print(i)
class MyRangeIterator:
    def __init__(self, stop_value):
        self.__start_value = 0
        self.__stop_value = stop_value

    def __next__(self):
        if self.__start_value >= self.__stop_value:
            raise StopIteration()
        result = self.__start_value
        self.__start_value += 1
        return result

class MyRange:
    def __init__(self, stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        return MyRangeIterator(self.__stop_value)

# 0 1 2
# 循环一次  计算一次  返回一个
for i in MyRange(5):
    print(i)

#生成器函数
#1. 定义：含有yield语句的函数，返回值为生成器对象。
#2. 语法
#----- 创建：
#def 函数名():
#  …
#  yield 数据
#  …
#----- 调用：	 for 变量名 in 函数名():		  语句
#3. 说明：
#-- 调用生成器函数将返回一个生成器对象，不执行函数体。
#--  yield翻译为”产生”或”生成”
#4. 执行过程：
#(1) 调用生成器函数会自动创建迭代器对象。
#(2) 调用迭代器对象的__next__()方法时才执行生成器函数。
#(3) 每次执行到yield语句时返回数据，暂时离开。
#(4) 待下次调用__next__()方法时继续从离开处继续执行。
#5. 原理：生成迭代器对象的大致规则如下
#-- 将yield关键字以前的代码放在next方法中。
#-- 将yield关键字后面的数据作为next方法的返回值。

"""
     执行过程:
        1. 调用__iter__()方法程序不执行.
        2. 调用__next__()方法开始执行.
        3. 执行到yield语句暂时离开方法.
        4. 再次调用__next__()方法继续执行
        .....
     原理:如果方法体中包含yield语句,则自动生成迭代器代码.
     生成迭代器代码的大致规则:
       1.将yield关键字以前的代码,放到__next__()方法中.
       2.将yield关键字以后的数据,作为__next__()方法返回值.
   """

# 练习:遍历员工管理器(私有的员工列表)
class Employee:
    pass

class EmployeeManager:
    def __init__(self):
        self.__list_emp = []

    def add_employee(self, emp):
        self.__list_emp.append(emp)

    def __iter__(self):
        for item in self.__list_emp:
            yield item

manager = EmployeeManager()
manager.add_employee(Employee())
manager.add_employee(Employee())
for item in manager:
    print(item)
iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

# 练习:参照下列代码,定义MyRange
# for i in range(5):
#    print(i)
class MyRange:
    def __init__(self, stop_value):
        self.__stop_value = stop_value

    def __iter__(self):
        start_value = 0
        while start_value < self.__stop_value:
            yield start_value
            start_value += 1

# 0 1 2
# 循环一次  计算一次  返回一个
for i in MyRange(5):
    print(i)
# 练习: 改写MyRnage类
def MyRange(stop_value):
    start_value = 0
    while start_value < stop_value:
        yield start_value
        start_value += 1

# 0 1 2
# 循环一次  计算一次  返回一个
for i in MyRange(5):
    print(i)

# 练习:使用生成器函数,获取列表中的所有偶数
#   [34,4,54,5,7,8]
def Double(list):
    for item in list:
        if item % 2 == 0:
            # return item 返回一个数据,退出方法
            yield item  # 返回多个数据,暂时离开方法
list = [34, 4, 54, 5, 7, 8]
for item in Double(list):
    print(item)
#枚举函数enumerate
#1. 语法：
#   for 变量 in enumerate(可迭代对象):
#       语句
#
#   for 索引, 元素in enumerate(可迭代对象):
#       语句
#2. 作用：遍历可迭代对象时，可以将索引与元素组合为一个元组
#练习:参照下列代码现象,自定义生成函数my_enumerate
#for item in enumerate(list):
#    print(item)

def my_enumerate(list):
    for item in range(len(list)):
        yield (item,list[item])

list = [34, 4, 54, 5, 7, 8]
for item in my_enumerate(list):
    print(item)

for index,item in enumerate([3,34,4,5,6]):
  print(index,item)

#zip
#1. 语法：
#   for item in zip(可迭代对象1, 可迭代对象2….):
#    	语句
#2. 作用：将多个可迭代对象中对应的元素组合成一个个元组,生成的元组个数由最小的可迭代对象决定。
#练习：参照下列代码现象,自定义生成器函数my_zip
list01=["张无忌","赵敏","周芷若"]
list02=[101,102,103]
for item in zip(list01,list02):
    print(item)

def my_zip(list01,list02):
    for item in range(len(list01)):
        yield (list01[item],list02[item])
list01=["张无忌","赵敏","周芷若"]
list02=[101,102,103]
for item in my_zip(list01,list02):
    print(item)

list01 = ["张无忌","赵敏","周芷若"]
list02 = [101,102]
for item in zip(list01,list02,list02):
  print(item)