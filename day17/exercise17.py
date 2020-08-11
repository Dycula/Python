#day17
#1.三合一
#2.当天练习独立完成
#3.定义学生类(姓名,年龄,性别,成绩)
#    定义生成器函数:获取列表中所有女学生
#    定义生成器函数:获取列表中年龄大于30的所有学生
#    定义生成器函数:获取列表中年成绩小于60的所有学生
class Student:
    def __init__(self, name, age, sex,score):
        self.name = name
        self.age = age
        self.sex= sex
        self.score = score
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, vaule):
        self.__name = vaule

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, vaule):
        self.__age = vaule

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, vaule):
        self.__sex = vaule

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, vaule):
        self.__score = vaule

    def print_self(self):
        print(self.name, self.age,self.sex, self.score)

list=[
    Student("张三",33,"男",90),
    Student("李四",22,"女",59),
    Student("赵五",23,"男",50)
      ]
def fun(list):
    for item in list:
        if item.sex=="女":
            yield item
#调用方法不执行,返回生成器对象
result=fun(list)
#延迟惰性操作的优点:不会将所有结果计算出来.存储在内存中
#缺点:通过索引/切片灵活的访问结果
#解决:将延迟操作转为立即操作
for item in result:
    print(item.name)

#result=(item for item in list if item.sex=="女")
#for item in result:
#    print(item.name)

def fun01(list):
    for item in list:
        if item.age>30:
            yield item
result=fun01(list)
for item in result:
    print(item.age)

#result=(item for item in list if item.age>30)
#for item in result:
#    print(item.age)

def fun02(list):
    for item in list:
        if item.score<60:
            yield item
result=fun02(list)
for item in result:
    print(item.score)

#result=(item for item in list if item.score<60)
#for item in result:
#    print(item.score)

#4.准备面向对象的答辩
#5.阅读重构和headfirst



#day17复习
#迭代
#    可迭代对象iterable:__iter__()
#    迭代器iterator:__next__()
#生成器:
#        可迭代+
#    生成器函数:函数体包含yield语句,返回生成器对象
#                def 函数名():
#                    ...
#                    yield 数据
#                    ...
