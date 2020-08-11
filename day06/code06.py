#1. 创建空元组：
#    元组名 = ()
#    元组名 = tuple()
list01=[1,2,3]#列表
tuple01=(1,2,3)#元组

#创建具有默认值的元组
tuple02=(1,"a")

#列表(可变)：预留空间
#元组(不可变)：按需分配

#列表扩容步骤：
#(1)开阔更大的空间
#(2)拷贝以前的数据
#(3)替换引用
tuple=(1)
print(tuple)#打印出来的为整数1,并非元素1

tuple=(1,)
print(tuple)#单个元素时添加逗号,此时打印出来的而是元素1

tuple=1,2,3,4   #创建元组时,可以省略小括号

#通切片/索引获取元素
print(tuple[::2])#切片
print(tuple[2])

#索引
#   正向：
#	for 变量名 in 列表名:
#		变量名就是元素
#	反向：
#	for 索引名 in range(len(列表名)-1,-1,-1):
#		元祖名[索引名]就是元素

#练习:根据月份计算天数，2月按28天算
tuple=(1,2,3,4,5,6,7,8,9,10,11,12)
month=int(input("请输入月份"))
if month not in tuple:
    print("输入错误")
elif month==2:
    print("28天")
elif  month in (4,6,9,11):
    print("30天")
else:
    print("31天")


#练习：在控制台中录入月份和日,计算这是那一年的第几天
month=int(input("请输入月份"))
day=int(input("请输入日"))
day_month=(31,28,31,30,31,30,31,31,30,31,30,31)
result=day
if month <0 or month >12 and day>31 or day<0:
    print("输入错误")
else:
    for item in range(0,month-1):
        number=day_month[item]
        result+=number
print("这是第"+str(result)+"天")

#哈希算法

#dict    字典
# 创建字典：
#字典名 = {键1：值1，键2：值2}
#字典名 = dict (可迭代对象)

dict0={}#空字典
dict01=dict()#空字典

dict={"zx":12 ,"as":34,"rt":56}#具有默认值
print(dict)

#添加/修改元素：
#语法:
#    字典名[键] = 数据
#说明:
#    键不存在，创建记录。
#    键存在，修改映射关系。
#获取元素：
#   变量 = 字典名[键]  # 没有键则错误
#遍历字典：
#	for 键名 in 字典名:
#		字典名[键名]
#   for 键名,值名 in 字典名.items():
#       语句
#删除元素：
#   del 字典名[键]


#在控制台中获取月份,显示对应的季度
season=input("输入季度")
dict_season={
    "春":(1,2,3),
    "夏":(4,5,6),
    "秋":(7,8,9),
    "冬":(10,11,12)}
if season in dict_season:
    months=dict_season[season]
    for item in months:
        print(str(item)+"月份")
else:
    print("输入错误")

#序列：　有序　灵活(索引)
#散序：  无序　　速度快　可读性更高

#在控制台中录入多个学生的信息(姓名,性别,年龄,成绩)
#如果姓名录入esc,则停止录入
dict_student={}
while True:
    student_name=input("录入学生姓名")
    if student_name == "esc":
        break
    student_sex=input("录入学生性别")
    student_age=int(input("录入学生年龄"))
    student_score=float(input("录入学生成绩"))
    dict_student[student_name]=[student_sex,student_age,student_score]
for key,value in dict_student.items():
    print("%s的性别是%s,年龄是%d,成绩是%.1f"%(key,value[0],value[1],value[2]))

#练习：创建调查问卷：
#"请输入姓名：(esc结束)"
#"请输入您的喜好：(esc结束)"
#"调查结束后，逐行显示所有信息
dict={}
while True:
    name=input("请输入姓名")
    if name=="esc":
        break
    like_list=[]
#    dict[name] = like_list
    while True:
        like=input("请输入您的喜好")
        if like =="esc":
            break
        like_list.append(like)#像列表添加元素同时向字典添加元素
    dict[name]=like_list
for key,value in dict.items():
    print("姓名%s,喜好是%s"%(key,value))































