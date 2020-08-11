# day11
# 1.三合一
# 2.当天练习独立完成
# 3.使用面向对象描述下列情景(攻击力,血量)
#    玩家攻击敌人,敌人受伤后掉血,还可能死亡(掉装备)
#    敌人攻击玩家,玩家受伤后掉血并且碎屏,还可能死亡(游戏结束)
class Player:
    def __init__(self, hp, atk):
        self.atk = atk
        self.hp = hp

    def attack(self, enemy):
        print("玩家攻击")
        enemy.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        print("玩家受伤啦,还剩%d血量" % self.hp)
        print("屏幕碎啦")
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("游戏结束")


class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk

    def damage(self, value):
        self.hp -= value
        print("敌人受伤啦,还剩%d血量" % self.hp)
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("敌人死啦,掉下了?装备")

    def attack(self, player):
        print("敌人攻击")
        player.damage(self.atk)


p01 = Player(500, 50)
e01 = Enemy(100, 10)
# 玩家打敌人
p01.attack(e01)
p01.attack(e01)
# 敌人打玩家
e01.attack(p01)


# 4.使用面向对象描述下列情景
# 张无忌教赵敏打篮球
# 赵敏教张无忌画眉
# 张无忌上班赚了10000元
# 赵敏上班赚了5000元
# 要求:遇到数据使用属性进行封装

class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, vaule):
        self.__name = vaule

    def teach(self, perosn_other, str_skill):
        print("%s教%s%s" % (self.name, perosn_other.name, str_skill))

    def work(self, money):
        print("%s上班赚了%s" % (self.name, money))


person01 = Person("张无忌")
person02 = Person("赵敏")
person01.teach(person02, "打篮球")
person02.teach(person01, "画眉")
person01.work(10000)
person02.work(5000)
# 5.倾尽一切手段,在互联网中找到封装的知识,并结合课堂所讲,总结为自己
# 的语言,为"全国面向对象课程答辩峰会"做准备


# 封装：
# 封装数据：多个数据－－－＞一个种数据(新数据)
#        例如：学生类(姓名,年龄)汽车(品牌,价格)
#        适用性:多种信息数据描述同一种事物
# 封装行为:函数只能表示一个行为,
#        类可以将数据与行为和二为一,表示世间万物
#        对外数据按必要的功能,隐藏(命名以双下划线开头)实现的细节
# 封装的设计思想:
#       分而治:将大的需求分解为多个小类,共同完成
#             类要小而精,拒绝大而全
#       封装变化:分解的度,识别变化点,单独做成类
#       高内聚:类内部要高度聚集完成一个类
#       低耦合：类与类关系,尽量松散.
