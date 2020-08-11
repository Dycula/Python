#day16
#1.三合一
#2.当天练习独立完成
#3.阅读HeadFirst设计模式和重构
#4.准备面向对象答辩内容
def fib(n):
    a,b=0,1
    for a in range(n):
        a,b=b,a+b
    return b

print(fib(4))

fib=lambda n:n if n<=2 else fib(n-1)+fib(n-2)
print(fib(4))

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





#day17复习
#模块和包
#  为什么有模块和包?
#    将代码有逻辑的组织在一起,使结构更加清晰,便与团队开发
#导入语法:
#    import 包.模块.成员 as 别名
#    本质:定义变量关联模块引用
#    from 包.模块 import 成员 as 别名
#    from 包.模块 import *
#    本质:将模块成员引入到当前模块作用域中
#    注意:如果导入模块或包失败,  检查sys.path.
#        如果路劲衔接正确(path路劲与from路劲),导入一定成功
#异常处理
#    异常:运行时检测的错误,程序会返回给调用者,不会继续执行
#    处理:将异常状态,改为正常状态
#    语法:
#    try:
#      可能出错的代码(...int(input())...)
#    except:
#      逻辑处理
#    后续逻辑