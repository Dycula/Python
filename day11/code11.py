# 练习:创建敌人类,具有(攻击力血量)
#     保证数据的范围(攻击力10~50)
#     保证数据的范围(血量0~100)
class Enemy:
    def __init__(self, attack):
        # 数据成员
        self.attack = attack
        # 通过方法操作数据,不要直接设置数据
        self.set__attack(attack)

    def print_self(self):
        print(self.attack)

    # 提供读取和写入的变量的功能
    def get__attack(self):
        return self.__attack

    def set__attack(self, attack__vaule):
        if 10 <= attack__vaule <= 50:
            # 1.隐藏变量:内部改变变量名称
            self.__attack = attack__vaule
        else:
            raise Exception("错误攻击力")


e01 = Enemy(20)
attack = e01.get__attack()
print(attack)


class Enemy:
    def __init__(self, blood):
        self.blood = blood

    def print_self(self):
        print(self.blood)

    @property  # 拦截读取操作,本质:创建property对象注册到写入方法中
    def blood(self):
        return self.__blood

    @blood.setter  # 拦截写入操作,本质:将写入方法注册到property中
    def blood(self, vaule):
        if 0 <= vaule <= 100:
            self.__blood = vaule
        else:
            raise Exception("错误血量")


# 总结:1.私有化实例变量:__变量名
#    2.提供对实例变量的读/写操作
#    3.通过方法操作数据
# 封装定义
#    1. 数据角度讲，将一些基本数据类型复合成一个自定义类型。
#    2. 行为角度讲，向类外提供必要的功能，隐藏实现的细节。
#    3. 设计角度讲：
# （1）分而治之
#     --将一个大的需求分解为许多类，每个类处理一个独立的功能。
#     -- 拆分好处：便于分工，便于复用，可扩展性强。
# (2) 封装变化
#     --变化的地方独立封装，避免影响其他类。
# (3) 高 内 聚
#     --类中各个方法都在完成一项任务(单一职责的类)。
# (4) 低 耦 合
#     --类与类的关联性与依赖度要低(每个类独立)，让一个类的改变，尽少影响其他类。
# [例如：硬件高度集成化，又要可插拔]
# 最高的内聚莫过于类中仅包含1个方法，将会导致高内聚高耦合。
# 最低的耦合莫过于类中包含所有方法，将会导致低耦合低内聚。

# 需求:老张开车去东北
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def to(self, type, str_pos):
        print(self.name)
        type.run(str_pos)


class Car:
    def run(self, str_pos):
        print("行驶到:", str_pos)


lz = Person("老张")
car = Car()
lz.to(car, "东北")


# 小明在招商银行取钱
class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, vaule):
        self.__name = vaule


class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, vaule):
        self.__name = vaule

    def draw_money(self, person, vaule):
        person.money += vaule
        self.money -= vaule


name01 = Person("小明", 100)
zs = Bank("招商银行", 1000000)
print(name01.money)
zs.draw_money(name01, 1000)
print(name01.money)
