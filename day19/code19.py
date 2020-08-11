"""
函数装饰器decorators
    1. 定义:在不改变原函数的调用以及内部代码情况下,为其添加新功能的函数
    2. 语法
def 函数装饰器名称(func):
    def 内嵌函数(*args, **kwargs):
        需要添加的新功能
        return func(*args, **kwargs)
    return wrapper

@ 函数装饰器名称
def 原函数名称(参数):
		函数体

原函数(参数)

    3. 本质:使用“@函数装饰器名称”修饰原函数,等同于创建与原函数名称相同的变量,关联内嵌函数;故调用原函数时执行内嵌函数
原函数名称 = 函数装饰器名称（原函数名称）

    4. 装饰器链:
一个函数可以被多个装饰器修饰,执行顺序为从近到远
"""

def memo(func):
    cache={}
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
            return cache[args]
    return wrap
@memo
def fib(i):
    if i <2:
        return 1
    return fib(i-1)+fib(i-2)
"""
  装饰器
"""

"""
def say_hello():
  print("hello")


def say_goodbye():
  print("goodbye")

say_hello()
say_goodbye()
"""
# 需求:在两个方法所实现的功能基础上,增加一种新功能(打印方法名称).

"""
def say_hello():
  print(say_hello.__name__)
  print("hello")

def say_goodbye():
  print(say_goodbye.__name__)
  print("goodbye")
"""

# 在say_hello与say_goodbye内部调用新功能,不容易改变(增加/删除)
"""
def print_func_name(func):
  print(func.__name__)

def say_hello():
  print_func_name(say_hello)
  print("hello")

def say_goodbye():
  print_func_name(say_goodbye)
  print("goodbye")
"""

"""
def print_func_name(func):# 提供旧功能
  def wrapper():# 包装
    print(func.__name__)# 新功能
    func()# 调用旧功能
  return wrapper

def say_hello():
  print("hello")

def say_goodbye():
  print("goodbye")

# 调用外部函数
say_hello = print_func_name(say_hello)
say_goodbye = print_func_name(say_goodbye)

# 调用内部函数(包装新 + 旧功能)
say_hello()
say_goodbye()
"""
"""
def print_func_name(func):# 提供旧功能
  def wrapper():# 包装
    print(func.__name__)# 新功能
    func()# 旧功能
  return wrapper

@print_func_name # say_hello = print_func_name(say_hello)
def say_hello():
  print("hello")

@print_func_name
def say_goodbye():
  print("goodbye")

say_hello()
say_goodbye()

"""


def print_func_name(func):  # 提供旧功能
  def wrapper(*args, **kwargs):  # 包装
    print(func.__name__)  # 新功能
    return func(*args, **kwargs)  # 旧功能

  return wrapper


@print_func_name  # say_hello = print_func_name(say_hello)
def say_hello():
  print("hello")
  return "ok"


@print_func_name
def say_goodbye(name):
  print(name, "goodbye")


result = say_hello()
print(result)
say_goodbye("张无忌")
"""
#练习:在不改变以下俩个功能的基础上,为其增加新功能
def enter_background():
    print("进入后台系统")
def delete_order():
    print("删除订单")
"""
def back(func):
    def wrapper(*args ,**kwargs):
        print("验证权限")
        return func(*args, **kwargs)
    return wrapper
@back
def enter_background():
    print("进入后台系统")
@back
def delete_order():
    print("删除订单")

enter_background()
delete_order()

"""
练习:在不改变学习和玩的功能基础上,增加新功能(打印执行时间)
import time

class Student:
    def study():
        print("学习...")
        time.sleep(10)
    def play():
        print("玩...")
        time.sleep(20)
"""
import time

def exercute_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        exercute_time=time.time()-start_time
        print("执行时间:",exercute_time)
        return result
    return wrapper
class Student:
    @exercute_time
    def study(self):
        print("学习...")
        time.sleep(10)
    @exercute_time
    def play(self):
        print("玩...")
        time.sleep(20)

student=Student()
student.study()
student.play()