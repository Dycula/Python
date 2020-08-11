"""
  skill_system.py
"""

class SkillSystem:
  def generate_skill(self):
    print("SkillSystem--generate_skill")


import sys
# 如果在终端中,从当前模块开始运行
# 则必须将项目根目录添加到path中.
sys.path.append("/home/tarena/1904/python_base/day16/my_project")
print(sys.path)

from skill_system.skill_deployer import SkillBaseDeployer
# 通过类名调用类方法
SkillBaseDeployer.fun01()
# 通过对象调用实例方法
# deployer = SkillBaseDeployer()
# deployer.deploy()
SkillBaseDeployer().deploy()

