# 练习:
#    定义员工管理器
#    记录所有员工
#    计算员工总薪资
# 1.普通员工:底薪
# 2.程序员:底薪+项目分红
# 3.销售:底薪+提成(销售额*0.05)
# 要求:增加新岗位,员工管理器不变

# --------------调用者--------------------

class Employee:
  def __init__(self, name, base_salary):
    # 代表人的很多数据....
    self.name = name
    self.base_salary = base_salary

  def calculate_salary(self):
    return self.base_salary


class Programmer(Employee):
  def __init__(self, name, base_salary, bonus):
    self.bonus = bonus
    super().__init__(name, base_salary)

  def calculate_salary(self):
    return self.base_salary + self.bonus


class Salesmen(Employee):
  def __init__(self, name, base_salary, sale_value):
    self.sale_value = sale_value
    super().__init__(name, base_salary)

  def calculate_salary(self):
    return self.base_salary + self.sale_value * 0.05
lw = Salesmen("老王", 2000, 5000)
print(lw.calculate_salary())
# 老王  -转岗--> 程序员

# 开除原老王, 招聘新老王
# 缺点:员工的姓名等人的数据,都会重新创建.
# 目标:对象一个部分改变,而不是全部改变.
lw = Programmer("老王",8000,10000)
print(lw.calculate_salary())

class Employee:
  def __init__(self, name,job_instance):
    # 代表人的很多数据....
    self.name = name
    self.job_instance = job_instance

  def get_salary(self):
    return self.job_instance.calculate_salary()

class Job:
  def __init__(self,base_salary):
    self.base_salary = base_salary

  def calculate_salary(self):
    return self.base_salary

class Programmer(Job):
  def __init__(self,base_salary, bonus):
    self.bonus = bonus
    super().__init__(base_salary)

  def calculate_salary(self):
    # return self.base_salary + self.bonus
    # 扩展重写:先调用父类被重写方法,再定义新功能
    return super().calculate_salary()  + self.bonus


class Salesmen(Job):
  def __init__(self, base_salary, sale_value):
    self.sale_value = sale_value
    super().__init__(base_salary)

  def calculate_salary(self):
    return self.base_salary + self.sale_value * 0.05


lw = Employee("老王",Salesmen(2000,5000))
print(lw.get_salary())
# 老王  -转岗--> 程序员

lw.job_instance = Programmer("老王",8000,10000)
print(lw.calculate_salary())

"""
  类与类的关系
"""

# 泛化:父子
class A:
  pass

class B(A):
  pass

# 关联:部分与整体
class C:
  def __init__(self, d):
    self.d = d

class D:
  pass

d01 = D()
c01 = C(d01)

# 依赖:合作
class E:
  def fun01(self, f):
    pass

class F:
  pass
#内置可重写函数
#Python中，以双下划线开头、双下划线结尾的是系统定义的成员。我们可以在自定义类中进行重写，从而改变其行为。
#__str__函数：将对象转换为字符串(对人友好的)
#__repr__函数：将对象转换为字符串(解释器可识别的)
class Wife:
  def __init__(self, name, sex, age):
    self.name = name
    self.sex = sex
    self.age = age

  def __str__(self):
    return "奴家%s,芳龄%d,性别:%s" % (self.name, self.age, self.sex)

  def __repr__(self):
    return 'Wife("%s","%s",%d)' % (self.name, self.sex, self.age)


w01 = Wife("铁锤", "女", 23)
# <__main__.Wife object at 0x7f292fef9278>
str01 = str(w01)
#       w01.__str__()
str02 = repr(w01)
#        w01.__repr__()
print(str01)
print(str02)
print(w01)

# eval 作用:根据字符串执行python代码.
re = eval("1+2+3+4")
print(re)  # 10
# 需求:克隆对象
w02 = eval(w01.__repr__())
w03 = w01
w01.name = "捶捶"  # 影响w03 不影响w02
print(w03)
print(w02)
#练习:定义学生类(姓名,成绩,年龄)"""
class Student:
    def __init__(self,name,score,age):
        self.__name=name
        self.__score=score
        self.__age=age
    def __str__(self):
        return "%s的成绩是%d,年龄%s"%(self.__name,self.__score,self.__age)
    def __repr__(self):
        return "Student(%s,%d,%s)"%(self.__name,self.__score,self.__age)

student=Student("张三",90,22)
print(student)

#运算符重载
#定义：让自定义的类生成的对象(实例)能够使用运算符进行操作
class Vector:
    def __init__(self,x):
        self.x=x

    def __add__(self, other):
        return Vector(self.x+other)
    def __truediv__(self, other):
        return Vector(self.x/other)
    def __radd__(self, other):
        return self.__add__(other)
    def __iadd__(self, other):
        self.x+=other
        return self
v01=Vector(1)
result=v01+2  #result=v01.__add__(2)
print(result.x)#3

v02=Vector(4)
result01=v02/2
print(result01.x)#2.0

v03=Vector(3)
result=8+v03
print(result.x)#11

v04=Vector(3)
v04+=2
print(id(v04))
print(v04.x)#5