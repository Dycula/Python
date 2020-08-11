"""
  skill_deployer.py
"""

class SkillBaseDeployer:

  def deploy(self):
    print("SkillBaseDeployer -- deploy")

  @classmethod
  def fun01(cls):
    print("SkillBaseDeployer--fun01")


from common.list_helper import helper01
helper01()