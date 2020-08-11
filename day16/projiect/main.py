"""
  main.py
     练习:
   创建如下结构:
    project
      main.py
      package01
         module01.py
         exercise03.py
   在main.py中调用exercise03.py
   在exercise03.py中调用module01.py
   测试1:从main.py中执行
   测试2:从exercise03.py中执行
   要求:从pycharm和终端中运行.
"""

from package01.exercise03 import *
fun03()

from package01 import *
exercise03.fun03()
