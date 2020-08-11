# 练习：定义,敌人类,具有数据(姓名,攻击力,攻击距离,生命值)
#     行为(print＿self 在控制台中输出对象数据)
class Enemy:
    def __init__(self, name, attack, length, blood):
        self.name = name
        self.attack = attack
        self.length = length
        self.blood = blood

    def print_self(self):
        print(self.name, self.attack, self.length, self.blood)


people01 = Enemy("灭霸", "10000", "100", "100")
people01.print_self()

##练习:在控制台中录入三个敌人,存入列表中
##并在控制台中循环调用print_self方法
list_all_people = []
for i in range(3):
    name = input("请输入姓名")
    attack = input("请输入攻击力")
    length = int(input("请输入攻击距离"))
    blood = int(input("请输入生命值"))
    people01 = Enemy(name, attack, length, blood)
    list_all_people.append(people01)
    people01.print_self()


class Wife:
    """
      老婆
    """

    def __init__(self, name, age):
        # 数据成员
        self.name = name
        self.age = age

    def play(self):
        print(self.name + "打游戏")


# 对象
w01 = Wife("丽丽", 23)
w01.play()
w02 = Wife("莹莹", 26)
w02.play()


# 实例变量
# 1. 语法
#   (1) 定义：对象.变量名
#   (2) 调用：对象.变量名
# 2. 说明
#   (1) 首次通过对象赋值为创建，再次赋值为修改.
#       w01 = Wife()
#       w01.name = “丽丽”
#      w01.name = “莉莉”
#   (2) 通常在构造函数(_init_)中创建。
#       w01 = Wife(“丽丽”,24)
#       print(w01.name)
#   (3) 每个对象存储一份，通过对象地址访问。
# 3.作用：描述所有对象的共有数据。
# 4. __dict__：对象的属性，用于存储自身实例变量的字典。
# 实例方法
# 1. 语法
#   (1) 定义：  def 方法名称(self, 参数列表):
#	             方法体
#   (2) 调用： 对象地址.实例方法名(参数列表)
#		      不建议通过类名访问实例方法
# 2. 说明
#   (1) 至少有一个形参，第一个参数绑定调用这个方法的对象,一般命名为"self"。
#   (2) 无论创建多少对象，方法只有一份，并且被所有对象共享。
# 3. 作用：表示对象行为。

# 练习:定义函数,在敌人列表中查找"灭霸"对象
def find01(list_target):
    for item in list_target:
        if item.name == "灭霸":
            return item


list = [
    Enemy("灭霸", 10000, 100, 100),
    Enemy("灭", 4000, 100, 100),
    Enemy("霸", 8000, 90, 100)]
result = find01(list)
result.print_self()


# 练习:定义函数,在敌人列表中,查找攻击力大于或等于5000的所有敌人
def find02(list_target):
    result = []
    for item in list_target:
        if item.attack >= 5000:
            result.append(item)
    return result


list01 = [
    Enemy("灭霸", 10000, 100, 100),
    Enemy("灭", 300, 8000, 100),
    Enemy("霸", 800, 9000, 100)]
result = find02(list01)
for item in result:
    item.print_self()


# 类变量
# 1. 语法
#   (3) 定义：在类中，方法外定义变量。
#         class 类名:
#		   变量名 = 表达式
#   (4) 调用：类名.变量名
#           不建议通过对象访问类变量
# 2. 说明
# -- 存储在类中。
# -- 只有一份，被所有对象共享。
# 3. 作用：描述所有对象的共有数据。
# 类方法
# 1. 语法
#   (1) 定义：
#    @classmethod
#    def 方法名称(cls,参数列表):
#         方法体
#   (2) 调用：类名.方法名(参数列表)
#      不建议通过对象访问类方法
# 2. 说明
# -- 至少有一个形参，第一个形参用于绑定类，一般命名为'cls'
# -- 使用@classmethod修饰的目的是调用类方法时可以隐式传递类。
# -- 类方法中不能访问实例成员，实例方法中可以访问类成员。
# 3. 作用：操作类变量。

class ICBC:
    # 类被加载时,类变量被创建
    total_money = 5000000

    @classmethod
    def print_total_money(cls):
        # 表达类的行为,只能操作类变量,不能操作实例变量
        print("总行的钱有:%s" % cls.total_money)

    def __init__(self, name, money):
        # 通过实例变量,表示支行的钱
        # 表示总行的钱
        self.name = name
        self.money = money
        # 从总行中扣除当前支行的钱
        ICBC.total_money -= money


i01 = ICBC("天坛支行", 100000)
# print(ICBC.total_money)
ICBC.print_total_money()
i02 = ICBC("天安门支行", 200000)
print(ICBC.total_money)


# 练习:统计一个类,创建了多少对象(记录init调用次数)
class Count:
    count = 0

    @classmethod
    def print_count(cls):
        print("统计次数%s" % cls.count)

    def __init__(self):
        Count.count += 1


c01 = Count()
c02 = Count()
c03 = Count()
Count.print_count()


# 静态方法
# 1. 语法
#  (1) 定义：
#    @staticmethod
#    def 方法名称(参数列表):
#            方法体
#  (2) 调用：类名.方法名(参数列表)
#      不建议通过对象访问静态方法
# 2. 说明
# -- 使用@ staticmethod修饰的目的是该方法不需要隐式传参数。
# -- 静态方法不能访问实例成员和类成员
# 3. 作用：定义常用的工具函数。
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod  # 调用当前方法时,不会传递任何信息
    def get_right():
        return Vector2(1, 0)  # 向右

    @staticmethod
    def get_left():
        return Vector2(-1, 0)  # 向左

    @staticmethod
    def get_up():
        return Vector2(0, 1)  # 向上

    @staticmethod
    def get_down():
        return Vector2(0, -1)  # 向下


pos01 = Vector2(1, 2)
# 通过向右的方法,获取向右的的方向
right = Vector2.get_right()
pos02 = Vector2(pos01.x + right.x, pos01.y + right.y)
print(pos02.x, pos02.y)
# 通过向左的方法,获取向左的的方向
left = Vector2.get_left()
pos03 = Vector2(pos01.x + left.x, pos01.y + left.y)
print(pos03.x, pos03.y)
# 通过向上的方法,获取向上的的方向
up = Vector2.get_up()
pos04 = Vector2(pos01.x + up.x, pos01.y + up.y)
print(pos04.x, pos04.y)
# 通过向下的方法,获取向下的的方向
down = Vector2.get_down()
pos05 = Vector2(pos01.x + down.x, pos01.y + down.y)
print(pos05.x, pos05.y)
