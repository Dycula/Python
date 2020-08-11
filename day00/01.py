import re

print(re.findall("ab*?", "abbbafdsafdsafd"))

# 基于fork的进程创建演示
import os

pid = os.fork()
if pid < 0:
    print("jkjl")
elif pid == 0:
    print("abc")
else:
    print("def")
print("ABCDEF")
os.getpid()
os.getppid()
import os

pid = os.fork()
if pid < 0:
    print("error")
elif pid == 0:
    print("child process:", os.getpid())
    os._exit(3)
else:
    p, status = os.wait()
    print("p:", p)
    print("status:", os.WEXITSTATUS(status))
    while True:
        pass


# python中唯一的映射类型是:字典
# 查看变量类型的python内置函数是：isinstance(),type()
# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
def demo(x, y, op):
    return eval(str(x) + op + str(y))


a = demo(3, 5, '*')
print(a)  # 15
print(list('[1,2,3]'))
import random

a = random.sample(range(10), 7)
print(a)
