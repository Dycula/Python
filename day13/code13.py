#继承
#语法
#1. 代码
#   class 子类(父类):
#    	def __init__(self,参数列表):
#   		super().__init__(参数列表)
#   		self.自身实例变量 = 参数
#2. 说明
#-- 子类拥有父类的所有成员。
#-- 子类如果没有构造函数，将自动执行父类的，但如果有构造函数将覆盖父类的。
#   此时必须通过super()函数调用父类的构造函数，以确保父类属性被正常创建。
#设计角度:先有子类后有父类   抽象化过程  具体(子,小概念)-->抽象(父,大概念)
#编码角度:先有父类后有子类
#判断对象的继承关系
#内置函数:
#   isinstance(obj, class_or_tuple)
# 返回这个对象obj 是否是某个类的对象,或者某些类中的一个类的对象。
#判断一个类型是否属于另一个类型
#   issunclass
"""
  继承--方法

  财产:钱不用孩子挣,但是可以花.
  皇位:江山不用孩子打,但是可以坐.
  ...
  代码:子类不用写,但是可以用.

  练习:exercise01.py
"""
# 设计角度: 先有子类,再有父类. 抽象化的过程:子(具体,小概念) -> 父(抽象,大概念)
# 编码角度: 先写父类,再写子类.

class Person:
  def say(self):
    print("会说话")

class Student(Person):
  def study(self):
    print("会学习")

class Teacher(Person):
  def teach(self):
    print("会讲课")

s01 = Student()
# 子类对象,直接使用父类方法.(继承语法的体现)
s01.say()
s01.study()

p01 = Person()
p01.say()
# 父类对象,只能使用自身方法,不能使用子类方法.

# 判断对象是否属于一个类型
print(isinstance(s01, Person))  # true
print(isinstance(s01, Teacher))  # false
print(isinstance(s01, (Person, Teacher)))  # true
print(isinstance(s01, Student))  # true

# 判断一个类型是否属于另一个类型
print(issubclass(Teacher, Person))  # true
print(issubclass(Teacher, Student))  # false
print(issubclass(Person, Student))  # false
print(issubclass(Person, Person))  # true
# 如果判断父子
print(issubclass(Teacher, Person) and Teacher != Person)
print(issubclass(Teacher, Teacher) and Teacher != Teacher)
#练习：定义子类:
#       狗(行为:看守)
#       鸟(行为:飞)
#       父类：动物(行为:叫)
class Animal():
    def shout(self):
        print("叫")
class Dog(Animal):
    def watch(self):
        print("看守")
class Bird(Animal):
    def fly(self):
        print("飞")
dog01=Dog()
dog01.shout()
bird01=Bird()
bird01.shout()
#判断对象的继承关系
print(isinstance(dog01,Dog))#True
print(isinstance(bird01,Bird))#True
#判断一个类型是否属于另一个类型
print(issubclass(Dog, Animal))#True
print(issubclass(Bird, Animal))#True
"""
  继承--数据 
"""
class Person:
  def __init__(self, name):
    self.name = name

class Student(Person):
  # 如果子类具有构造函数,则没有父类的构造函数.
  def __init__(self, name, score):
    self.score = score
    # 通过super()函数调用父类方法
    super().__init__(name)

s01 = Student("无忌", 100)
print(s01.name)
print(s01.score)


p01 = Person("无忌")
print(p01.name)
# 如果子类没有构造函数,则使用父类的.
#练习：定义父类:汽车(数据:品牌,型号,价格)
#     子类:电动汽车(数据:电池容量充电功率)
class Car():
    def __init__(self,price,model,brand):
        self.price=price
        self.model=model
        self.brand=brand
class ElectricCar(Car):
    def __init__(self, battery_capacity, charing_power,price,model,brand):
        #调用父类的构造函数
        super().__init__(price,model,brand)
        self.battery_capacity=battery_capacity
        self.charing_power=charing_power
#定义父类:动物(数据:姓名,年龄)
#定义子类:狗(数据:爱称)
class Aminal():
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Dog(Aminal):
    def __init__(self,dear_name,name,age):
        super().__init__(name,age)
        self.dear_name=dear_name

dog02=Dog("Lcukly","狗",2)

#设计原则:
#1.开闭原则
#扩展(增加新功能)开放(允许)
#修改(改变以前的代码)关闭(拒绝)
#2.依赖倒置
#使用抽象(父类,稳定的),而不是使用子类(多变化)
# 老王开车去东北
# 需求变化:坐飞机
#          火车
#          骑车
#  ....

"""
class Person:
  def __init__(self, name):
    self.name = name

  def to(self, type, str_pos):
    print(self.name)
    if isinstance(type, Car):
      type.run(str_pos)
    elif isinstance(type, Airplane):
      type.flay(str_pos)

class Car:
   def run(self, str_pos):
     print("行驶到:", str_pos) 

class Airplane:
   def flay(self, str_pos):
     print("飞过到:", str_pos)

"""

# ------------使用者------------
class Person:
  def __init__(self, name):
    self.name = name

  def to(self, type, str_pos):
    # 如果传入的不是交通工具
    if not isinstance(type, Vehicle):
      # 人为抛出一个错误(程序中断)
      # 目的:传入的对象,必须是交通工具的子类.
      raise TypeError()
    print(self.name)
    # 关心的不是火车/飞机/汽车等交通工具
    # 关心的是他们有运输的功能
    type.transport(str_pos)

class Vehicle:
  """
    交通工具:代表火车/飞机/汽车..
  """
  def transport(self, str_pos):
    # 人为抛出一个错误(程序中断)
    # 目的:要求子类必须具有当前方法
    raise NotImplementedError()

# ------------定义者------------
class Car(Vehicle):
  def transport(self, str_pos):
    print("行驶到:", str_pos)

class Airplane(Vehicle):
  def transport(self, str_pos):
    print("飞过到:", str_pos)

lw = Person("老王")
c01 = Car()
a01 = Airplane()
lw.to(c01, "东北")

#练习:手雷爆炸了,可能伤害敌人,玩家,
# 还可能伤害未知的事物(鸭子,树)
#要求:如果增加了新的事物,不影响雷的代码
#体会:开闭原则,依赖倒置
# ------------使用者----------------
class Grenade:
  def explode(self, target):
    """
      爆炸
    """
    # 如果传入的对象,没有按要求继承Damageable,则错误.
    if not isinstance(target,Damageable):
      raise TypeError()
    # 调用目标的受伤方法
    target.damage(100)

class Damageable:
  """
    可以受伤害
  """
  def damage(self, value):
    # 如果子类没有当前方法,则错误.
    raise NotImplementedError()

# ------------定义者----------------
class Player(Damageable):
  """
    玩家
  """

  def damage(self, value):
    print("玩家扣%d血,并且碎屏." % value)

class Enemy(Damageable):
  """
    敌人
  """

  def damage(self, value):
    print("敌人扣%d血,并且头顶冒字." % value)

# 测试
g01 = Grenade()
p01 = Player()
e01 = Enemy()
g01.explode(e01)



















