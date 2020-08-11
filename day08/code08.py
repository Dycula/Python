#返回值
#(1) 定义：方法定义者告诉调用者的结果。
#(2) 语法：return 数据 
#(3) 说明：
#   return后没有语句，相当于返回 None
#   函数体没有return，相当于返回None

#例如：定义一个函数，计算俩个数相加
def add(number01,number02):
    #number01=float(input("输入第一个数"))
    #number02=float(input("输入第二个数"))
    result=number01+number02
    return result

a=float(input("输入第一个数"))
b=float(input("输入第二个数"))
c=add(a,b)
print("结果是："+str(c))


#体会:参数　　是调用者传递定义者的信息
#    返回值　　是定义者告诉调用者的信息
#    品质     一个功能（职责第一）

#例如:输入时间计算秒数
def input_second(hour,minute,second):
    result=hour*3600+minute*60+second
    return result


a=int(input("输入小时"))
b=int(input("输入分钟"))
c=int(input("输入秒数"))
d=input_second(a,b,c)
print(d)
print(input_second(a,b,c))

#练习:在控制台中录入一个成绩,显示优秀/良好/及格/不及格/有误
#优秀:90-100
#良好:80-90
#及格:60-80
#不及格:0-60
score=float(input("录入一个成绩"))
if 100>score>=90:
    print("优秀")
elif 90>score>= 80:
    print("良好")
elif 80>score>= 60:
    print("及格")
elif 60>score>= 0:
    print("不及格")
else:
    print("录入有误")

#return 可以退出函数
def get_score_level(a):
    if 100 > a >= 90:
        return "优秀"
        #代码运行到57行,return退出函数
        #代码运行到60行,57行代码没有运行
    if 90 >a >= 80:
        return "良好"
    if 80 > a>= 60:
        return "及格"
    if 60 > a >= 0:
        return "不及格"
    return "录入有误"

a=float(input("输入分数"))
level=get_score_level(a)
print(level)

#定义函数,判断是否是闰年
def is_leap_yaer(year):
    return year%4==0 and year%100!=0 or year%400==0

year=input("输入年份")
b=is_leap_yaer(year)
print(b)

#定义函数,根据月份计算天数
def year_month(year,month):
    if month<1 or month>12:
        return"输入月份有误"
    if month in (4,6,9,11):
        return 30
    if month in (1,3,5,7,8,10,12):
        return 31
    if year%4==0 and year%100!=0 or year%400==0:
        return 29
    return 28

year=int(input("输入年份"))
month=int(input("输入月份"))
a=year_month(year,month)
print(a)


#定义函数,计算指定范围内的素数
def sushu(a,b):
    '''
    获取范围内的素数
    :param a: 开始数值(包含)
    :param b: 结束数值,b+1(包含)
    :return:
    '''
    list=[]
    for r in range(a,b+1):
        if r == 1:
            continue
        for c in range(a+1,r):
            if  r%c ==0:
                break
        else:
            list.append(r)
    return list

print(sushu(1,100))


#在内存的方法区存储函数的字节码
def fun01(p1):
    #修改的是变量指向的第一个元素
    p1[0]=300

number=[100,200]
#调用函数,会在内存中开辟空间(栈帧),存储函数内定义的变量
fun01(number)
#函数执行完毕后,栈帧立即失效
print(number[0])#100


#定义函数,对列表的升序排列
#传入的是可变型对象,函数体内部修改可变对象,无需通过返回值,返回结果
def asc(list):
    #外层循环拿数据
    for r in range(len(list)-1):
        #内层循环做比较
        for c in range(r+1,len(list)):
            #发现更小的数据则进行交换
            if list[r]>list[c]:
                list[r],list[c]= list[c],list[r]
    #return list
list=[2,0,5,32,55,14,65,47,98]
asc(list)
print(list)

#Local局部作用域：函数内部
#Global全局作用域：模块(.py文件)内部
g01=500
def fun01():
    g01=600#600  没有修改全局变量g01,而是创建了局部变量g01
    print(g01)

def fun02():
    print(g01)#500
    f01=200

def fun03():
    global g01
    g01=300
fun03()
fun01()#600
fun02()#300

#练习:统计一个函数的执行次数
number=0
def count():
    global number
    number+=1
count()
count()
count()
print("执行了%d次"%(number))


def fun1(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
#位置传参:实参与形参的位置依次对应
fun1(1,2,3,4)

#序列传参:*号作用是将序列拆分开后与形参位置依次对应
list01=[1,2,3,4]
fun1(*list01)

#关键字传参:实参根据形参的名称进行对应
#     作用:可以选择行的为形参赋值
fun1(b=2,c=4,d=3,a=5)
fun1(1,2,d=5,c=3)#先位置传参,再关键字传参可以运行
#fun1(d=5,c=3,2,4)#先关键字传参，后位置传参不可以运行

#字典传参:**将字典拆分后与形参的名字进行对应
dict01={"d":4,"c":3,"b":1,"a":2}
fun1(**dict01)

#默认参数：如果不传递参数，可以使用默认值参数
def fun2(a,b=2,c=3,d=4):
    print(a)
    print(b)
    print(c)
    print(d)

#关键字传参+默认参数:可以选择性的为形参赋值
fun2(5,6,7,8)
fun2(b=6)#为参数b赋值
fun2(2)#为参数a赋值

def fun01(a,b,c):
    pass

#星号元组形参:＊让实参个数无限制
def fun02(*a):
    print(a)
#可以不传递参数,也可以传递多个参数
fun02()#()
fun02(1,2,3)#(1, 2, 3)

#练习:定义函数,数值相加的函数
def add(*args):
    sum=0
    for item in args:
        sum+=item
    return sum
print(add(1,2,3,4,))#10

#位置形参(必写)+星号元组形参(可选)
def fun04(a,b,*args):
    print(a)
    print(b)
    print(args)
fun04(1,3,5,4)#1  3  (5,4)

#命名关键字形参:要求实参必须以关键字传递
def fun05(*,a,b):
    print(a)
    print(b)
fun05(a=1,b=2)
#a,b  是命名关键字形参

def fun06(*args,a,b):
    print(args)
    print(a)
    print(b)
fun06(1,2,3,4,5,a=1,b=3)#(1, 2, 3, 4, 5)  1   3
#print(*args,sep=' ',end='\n')
print(1,2,sep="-")#1-2

#双星号字典形参数:实参可以传递多个关键字参数
def fun07(**kwargs):
    print(kwargs)
fun07(a=1,b=2,c=3)#{'a': 1, 'b': 2, 'c': 3}

#万能传参：位置参数无限制,关键字参数无限制
def fun08(*args,**kwargs):
    pass
fun08()




























