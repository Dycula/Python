# day10作业
# 1.三合一
# 2.当天练习独立完成
# 3.定义学生类,具有(姓名,性别,成绩)数据
#            具有打印个人信息的行为

class Student:
    def __init__(self, name="", sex="", score=0):
        self.name = name
        self.sex = sex
        self.score = score

    def print_self(self):
        print(self.name, self.sex, self.score)


# 　　定义函数,在学生列表中查找姓名是"张无忌"的学生对象
def find01(list):
    for item in list:
        if item.name == "张无忌":
            return item


# 　　定义函数,在学生列表中查找成绩大于60的所有女学生对象
def find02(list):
    result = []
    for item in list:
        if item.score > 60 and item.sex == "女":
            result.append(item)
    return result


#    定义函数,计算成绩大于或等于60的所有学生总数
def find03(list):
    count = 0
    for item in list:
        if item.score >= 60:
            count += 1
    return count


#    定义函数,获取最高分的学生对象
def find04(list):
    max_number = list[0]
    for item in range(1, len(list)):
        if max_number.score < list[item].score:
            max_number = list[item]
    return max_number


#    定义函数,删除所有成绩低于60的学生对象
def find05(list):
    for item in range(len(list) - 1, -1, -1):
        if list[item].score < 60:
            del list[item]
    return list


list = [
    ["张无忌", "男", 99],
    ["李四", "男", 80],
    ["王麻子", "女", 65],
    ["陈二", "男", 70],
]

# 4.(扩展)定义函数,获取二维列表某个元素的某个方向的指定个的所有元素
# 获取下列二维列表,21位置元素,向右,3
# 结果是:22 23 24
"""
00 01 02 03 04
10 11 12 13 14
20 21 22 23 24
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod  # 调用当前方法时,不会传递任何信息
    def get_right():
        return Vector2(0, 1)  # 向右

    @staticmethod
    def get_left():
        return Vector2(0, -1)  # 向左

    @staticmethod
    def get_up():
        return Vector2(-1, 0)  # 向上

    @staticmethod
    def get_down():
        return Vector2(1, 0)  # 向下


def get_elements(target, vect_pos, vect_dir, count):
    result = []
    for i in range(count):
        # 改变位置:原位置 + 方向
        vect_pos.x += vect_dir.x
        vect_pos.y += vect_dir.y
        result.append(target[vect_pos.x][vect_pos.y])
    return result


list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
# "11","12"
pos = Vector2(1, 0)
dir = Vector2.get_right()  # 0 1
re = get_elements(list01, pos, dir, 2)
print(re)

# 面向对象
# 类
#    概念:抽象的
#    语法:
#        class 类名:
#            def __init__(self,参数):
#                self.变量名=参数
# 对象
#    概念:具体的
#    语法:
#        变量名=构造函数(参数列表)
#   设计角度讲:先有对象后有类--->抽象化的过程
#   编码角度讲:先有类后有对象--->实例化(具体化)的过程
# 类中成员
#    实例成员:
#     变量
#       概念:表示对象的数据(每个对象的数据都可以不一样)例如：杯子
#       语法:对象.名称=?
#       备注:通常在__init__方法中定义
#     方法
#        概念:表示类的行为,常用于操作实例变量
#        语法:def 方法名称(self):
#                 方法体
#    类成员:
#       概念:表示类的数据(所有对象共享的数据)例如:饮水机
#       语法:在类中,方法外，定义变量
#      方法
#        概念:表示类的行为,常用于操作类变量
#        语法:
# 　               @classmethod
#                def 方法名称(cls):
#                    方法体
#        备注:@classmethod的作用是,
#    静态方法
#       概念:将函数放到类中
#       语法:
#           @staticmethod
#           def 方法名称():
#               方法体
#        备注:@staticmethod的作用是,调用方法时不自动
#
#
#
#
