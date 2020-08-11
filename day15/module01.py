"""
  模块1
"""

# 使用__all__定义可以导出的成员
__all__ = ["fun01"]

def fun01():
  print("fun01")

def fun02():
  print("fun02")

# 隐藏成员(不会被import * 导入)
def _fun03():
  print("fun03")

print(__name__)

"""
  模块变量
"""
#from module01 import *
#import module01

fun01()
# fun02()  不能导入__all__规定外的成员
# fun03()  不能导入隐藏成员

# 获取模块文档注释
print(__doc__)
#/home/tarena/1904/python_base/day15/code03.py
print(__file__)

import sys
print(sys.path)