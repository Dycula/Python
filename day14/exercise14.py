#day14
#1. 三合一
#2. 当天练习独立完成
#3. 画出天龙八部3d游戏的技能系统类设计图.
#   变化:增加/减少技能
#        技能改变了影响效果.
#   尝试:一个技能定义为一个类(行为).
#4. 穷尽一切手段,收集六大设计原则的资料,结合课堂所讲,总结一份自述.
"""
  天龙八部 技能系统
  练习:指出下列代码,体现了哪些设计原则.
      开闭原则: 增加新的影响效果,只需要创建新类,
               不需要修改技能释放器.
      单一职责:释放器负责释放技能.
              具体影响效果类负责某一种算法.
              影响效果类负责隔离释放器与具体效果的变化.
      依赖倒置:技能释放器调用影响效果,没有调用具体效果类(伤害生命..)
              子类依赖父类,但父类不依赖子类.
              技能释放器通过字符串(配置文件)创建具体效果对象.
      组合复用:技能释放器与影响效果使用关联(组合)关系,而不是继承关系.
      里氏替换:所有具体影响效果,都可以将抽象(父)的影响效果替换掉.
      迪米特法则:具体影响效果之间,没有联系.
                技能释放器与具体影响效果也有隔离.
"""


class ImpactEffect:
  """
    影响效果
  """

  def impact(self):
    """
      影响效果,由技能释放器调用,由具体效果类实现.
    :return:
    """
    raise NotImplementedError()


class DamageEffect(ImpactEffect):
  """
    伤害生命效果
    可以被所有需要伤害生命的技能使用
  """

  def __init__(self, value):
    self.value = value

  def impact(self):
    print("伤害你的%d生命" % self.value)


class LowerMoveSpeed(ImpactEffect):
  """
    降低移动速度效果
  """

  def __init__(self, speed, time):
    self.speed = speed
    self.time = time

  def impact(self):
    print("降低速度为%d,持续时间%d." % (self.speed, self.time))


class SkillDeployer:
  """
    技能释放器
  """

  def __init__(self, name):
    self.name = name
    self.__list_impact = self.__config_skill()

  def __config_skill(self):
    """
      配置技能
    """
    # 配置文件中,记录的信息.
    dict_skill_config_info = {
      "金刚伏魔": ["DamageEffect(100)"],
      "降龙十八掌": ["LowerMoveSpeed(50,60)", "DamageEffect(100)"]
    }
    # 根据键(技能名称)从字典中获取值(str列表)
    list_skill_info = dict_skill_config_info[self.name]
    # 根据字符串列表,创建影响效果对象的列表.
    # "DamageEffect(100)" -->DamageEffect的对象
    list_skill_instance = []
    for item in list_skill_info:
      list_skill_instance.append(eval(item))
    # 返回技能列表
    return list_skill_instance
    # 建议使用列表推导式
    # return [eval(item) for item in list_skill_info]

  def generate_skill(self):
    """
      生成(释放)技能
    :return:
    """
    print(self.name, "技能释放啦")
    # 遍历影响效果列表,执行每个效果.
    for item in self.__list_impact:
      item.impact()


# 测试
# 创建技能(确定技能名称,加载技能效果)
xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()

jgfm = SkillDeployer("金刚伏魔")
jgfm.generate_skill()

"""
  day14 复习
  面向对象
    三大特征:
      封装:分而治之,封装变化.      识别变化
      继承:抽象(代表)变化         隔离变化
      多态:调用父方法,执行子方法.  执行变化
          重写:子类方法与父类方法名称相同.

    六大原则:
      开闭原则: 允许增加新功能,不能修改客户端的代码.  目标
      单一职责: 一个类只有一个变化点.
      依赖倒置:调用父(抽象/稳定),而不是子类(具体/变化).
      组合复用: 代码复用的最佳实践.
      里氏替换: 父类出现的地方,可以被子类替换掉;
               重写父类方法时,要保持原有功能(建议扩展重写)
              形参:  方法(父类型)
              实参:  方法(子对象)
      迪米特法则:低耦合

    设计模式:
        六大原则的代码实践.
"""
