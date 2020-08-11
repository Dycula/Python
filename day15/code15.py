"""
  多继承
"""
#一个子类继承两个或两个以上的基类，父类中的属性和方法同时被子类继承下来。
#同名方法的解析顺序（MRO， Method Resolution Order）:
#类自身 --> 父类继承列表（由左至右）--> 再上层父类
#     A
#    / \
#   /   \
#  B     C
#   \   /
#    \ /
#     D
#定义
#    1. 重用现有类的功能与概念，并在此基础上进行扩展。
#    2. 说明：
# -- 子类直接具有父类的成员（共性），还可以扩展新功能。
#-- 事物具有一定的层次、渊源，继承可以统一概念。
#优点
#    1. 一种代码复用的方式。
#    2. 以层次化的方式管理类。
#缺点:耦合度高#
#作用:隔离客户端代码与功能的实现方式。
#相关概念
#父类相对于子类更抽象，范围更宽泛；子类相对于父类更具体，范围更狭小。
#单继承：父类只有一个（例如 Java，C#）。
#多继承：父类有多个（例如C++，Python）。
#Object类：任何类都直接或间接继承自 object 类。
#内置函数
#   isinstance(obj, class_or_tuple)
#返回这个对象obj 是否是某个类的对象,或者某些类中的一个类的对象。
class A:
  def fun01(self):
    print("A--fun01")

class B(A):
  def fun01(self):
    super().fun01()
    print("B--fun01")

class C(A):
  def fun01(self):
    super().fun01()
    print("C--fun01")

class D(C,B):
  def fun01(self):
    super().fun01()#?
    print("D--fun01")

# 测试
d01 = D()
d01.fun01()
# 同名方法解析顺序
print(D.mro())

"""
  模块  调用 module01 中fun01函数.
"""
# 导入方式1:
#  语法:import 模块名称
#  使用:模块名称.成员
#  本质:创建一个变量叫module01,关联模块地址.
import module01
module01.fun01()

# 起别名
import module01 as m
m.fun01()

# 导入方式2:
# 语法:from 模块名 import 成员
# 使用:直接使用成员
# 本质:将成员添加到当前作用域
from module01 import fun01
fun01()

# 导入方式3:
#from module01 import *

def fun01():
  print("code02 -- fun01")

# 就近原则:选择调用语句最近的,方法的定义.
fun01()

#fun02()

#实现以下功能:
#        1. 获取00位置向右3个元素
#        2. 获取13位置向左2个元素
#        3. 获取22位置向上2个元素
#      要求:分别使用三种导入方式实现.

list01 = [
  ["00", "01", "02", "03"],
  ["10", "11", "12", "13"],
  ["20", "21", "22", "23"],
]

import double_list_helper as helper

pos = helper.Vector2(0, 0)
dir = helper.Vector2.get_right()
re = helper.get_elements(list01, pos, dir, 3)
print(re)
"""
"""
from double_list_helper import Vector2,get_elements

pos = Vector2(0, 0)
dir = Vector2.get_right()  # 0 1
re = get_elements(list01, pos, dir, 3)
print(re)


from double_list_helper import *

pos = Vector2(0, 0)
dir = Vector2.get_right()  # 0 1
re = get_elements(list01, pos, dir, 3)
print(re)