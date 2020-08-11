# day09
# 1.三合一
# 2.当天练习独立完成
# 3.2048的核心算法
# (1)定义函数,向上移动二维列表
# (核心思想:从上到下获取列数据,形成一维列表,交给合并方法,最后恢复)
# 依次获取第一,二,三,四个列表的第一个数,依次获取第一,二,三,四个列表的第二个数
# 依次获取第一,二,三,四个列表的第三个数,依次获取第一,二,三,四个列表的第四个数
# 组成一个新的列表,调用函数1和2,最后还原
def move_up(map):
    for r in range(len(map)):
        list_merge = []
        for c in range(4):
            list_merge.append(map[c][r])
        merge(list_merge)
        for c in range(4):
            map[c][r] = list_merge[c]


list = [
    [2, 2, 0, 2],
    [0, 2, 0, 4],
    [2, 0, 4, 2],
    [0, 4, 2, 2],
]
move_up(list)
print(list)


# (2)定义函数,向下移动二维列表
# (核心思想:从下到上获取列数据,形成一维列表,交给合并方法,最后恢复)
def move_down(map):
    # 30  20  10  00
    for c in range(4):
        list_merge = []
        for r in range(3, -1, -1):
            list_merge.append(map[r][c])

        merge(list_merge)

        # list_merge(从左到右) 赋值给 二维列表(从下到上)
        for r in range(3, -1, -1):  # 3 2 1 0
            map[r][c] = list_merge[3 - r]


list = [
    [2, 2, 0, 2],  #
    [0, 2, 0, 4],  #
    [2, 0, 4, 2],  #
    [0, 4, 2, 2],  #
]
move_right(list)
print(list)


# 4.画出code01.py代码的内存图
# 5.创建狗类,具有姓名,体重等数据
# 　具有坐,吃,导盲等行为
# 　创建至少2个对象
class Dog:
    def __init__(self, str_name, str_weight):
        self.name = str_name
        self.height = str_weight

    def sit(self):
        print(self.name + "坐")

    def eat(self):
        print(self.name + "吃")


Dog01 = Dog("Luckly", 20)
Dog01.sit()
Dog01.eat()


# 6.以万物皆对象的思想,洞察身边存在客观事物
# 自行创建1个类,2个对象
class People:
    def __init__(self, name, attack, length, blood):
        self.name = name
        self.attack = attack
        self.length = length
        self.blood = blood

    def eat(self):
        print(self.name + "吃")

    def sit(self):
        print(self.name + "坐")


people01 = People("luckly", "500", "100", "100")
people01.eat()
people01.sit()
# day09复习
# 面向对象:
#    面向过程:考虑细节//逐步实现
#    面向对象:识别对象//分配职责//建立交互
#    类和对象:
#        语法:
#            创建类:
#                class 类名:
#                    def __init__(self,参数):
#                        self.数据=参数
#                    def 行为(self):
#                        方法体
#            创建对象:构造函数指的是类中的__init__方法
#                   变量名=构造函数(参数)
#         问题:先有类还是先有对象?
#               设计角度:先有对象再有类    抽象化过程
#               编码角度:先有类后有对象    具体化过程
#        类:类别   抽象的
#        对象:个体  具体的
#        类和对象的区别:抽象与具体
#        类和类的区别:行为的不同
#        对象和对象的区别:数据的不同
#
