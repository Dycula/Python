def fun03():
  print("exercise03模块的fun03函数")

import sys
sys.path.append("/home/tarena/1904/python_base/day16/project")
print(sys.path)

from package01.module01 import *
fun01()