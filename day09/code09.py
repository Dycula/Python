# if语法：
#   变量 = 结果1 if 条件 else 结果2
# 列表推导式 语法：
#   变量 = [表达式 for 变量 in 可迭代对象]
#   变量 = [表达式 for 变量 in 可迭代对象 if 条件]
# 列表推导式嵌套语法：
#   变量 = [表达式 for 变量1 in 可迭代对象1 for 变量2 in可迭代对象2]
# 字典推导式语法:
#   {键:值 for 变量 in 可迭代对象}
#   {键:值 for 变量 in 可迭代对象 if 条件}
# 集合推导式语法:
#   {表达式 for 变量 in 可迭代对象}
#   {表达式 for 变量 in 可迭代对象 if 条件}

# 定义类
# 1.代码
#   class 类名:
#	    “””文档说明”””
#	def _init_(self,参数列表):
#		self.实例变量 = 参数
#          方法成员
# 2.说明
# --  类名所有单词首字母大写.
# --  _init_ 也叫构造函数，创建对象时被调用，也可以省略。
# --  self 变量绑定的是被创建的对象，名称可以随意。

# 练习：
#   定义类：具体事物,抽象话的过程
#   创建对象:抽象事物,具体化的过程
# 定义汽车类:数据(品牌,型号,价格)
#         行为(启动,行驶)
# 创建俩个对象
class Car:
    # 俩个下划线开头,俩个下划线结尾
    def __init__(self, str_brand, str_model, price):
        self.brand = str_brand
        self.model = str_model
        self.price = price

    def start(self):
        print(self.brand + "汽车启动")

    def move(self):
        print(self.brand + "汽车行驶")


c01 = Car("宝马", "X5", 600000)
c01.start()
c01.move()


# 练习：定义,做人类,具有数据(姓名,攻击力,攻击距离,生命值)
#     行为(print＿self 在控制台中输出对象数据)
class People:
    def __init__(self, name, attack, length, blood):
        self.name = name
        self.attack = attack
        self.length = length
        self.blood = blood

    def print_self(self):
        print(self.name, self.attack, self.length, self.blood)


people01 = People("luckly", "500", "100", "100")
people01.print_self()

# 练习:在控制台中录入三个敌人,存入列表中
# 并在控制台中循环调用print_self方法
list_all_people = []
for i in range(3):
    name = input("请输入姓名")
    attack = input("请输入攻击力")
    length = int(input("请输入攻击距离"))
    blood = int(input("请输入生命值"))
    people01 = People(name, attack, length, blood)
    list_all_people.append(people01)
    people01.print_self()
