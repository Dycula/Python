""""
程序入口模块 main
"""
from ui import *

# 如果不是主模块,则不执行下列代码
# 目的:强迫程序从当前模块执行
view = StudentManagerView()
view.main()