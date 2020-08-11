#day06作业
#1.三合一
#2.每天独立完成练习
#3.将1970~2050年中的闰年存入列表
list_year=[]
for year in range(1970,2051):
    if year%4==0 and year%100!=0 or year%400==0:
        list_year.append(year)
print(list_year)

#4.描述多个商品信息,在控制台中逐行显示出来
#        酒:1000元
dict={}
while True:
    name=input("录入商品信息")
    if name =="esc":
        break
    price=int(input("输入商品的价格"))
    id=input("输入商品的产地")
    dict[name]=[price,id]
for key,value in dict.items():
    print("%s的商品价格是%d,产于%s"%(key,value[0],value[1]))

#5.描述全国各个城市的景区与美食
#    北京:
#        景区:故宫,天安门,天坛
#        美食:烤鸭,炸酱面
dict={}
while True:
    city=input("请输入一个城市：")
    if city=="esc":
        break
    list_view=[]
    list_eat=[]
    while True:
        view=input("请输入景区名称:")
        eat=input("请输入美食名称:")
        if view=="esc" or eat=="esc":
            break
        list_view.append(view)
        list_eat.append(eat)
    dict[city]=[list_view,list_eat]
print(dict)


#6.计算一个字符串中的字符以及出现的次数
#    hjhhjhhjoijkhk#
str=input("请输入一个字符串")
list=[]
n=0
while n<len(str):
    for i in range(len(str)):
        number=str[i]
        if number not in list:
            list.append(number)
        else:
            continue
    n+=1
print(list)

#将每个字符以及出现的次数存入一个容器
str_input=input("输入一个字符串")
dict_result={}
for  item in str_input:
    #该字符在字典中不存在,则新增字符与次数
    if item not in dict_result:
        dict_result[item]=1
    #如果存在，则增加出现次数
    else:
        dict_result[item]+=1
print(dict_result)


#7.扩展:猜拳游戏:石头剪刀布'''
#系统随机选择一个
#用户输入一个
#判断输赢
import random
dict_wins={"石头":"剪刀","剪刀":"布","布":"石头"}
list_items=("石头","剪刀","布")
random_number=random.randint(0,2)
sys_input=list_items[random_number]
print(sys_input)
str_user_input=input("用户输入一个")
if str_user_input == sys_input:
    print("平局")
elif dict_wins[str_user_input]==sys_input:
    print("胜利")
else:
    print("失败")



#8.阅读python从入门到实践第六章



#容器：存储一系列数据
#字符串：存储字符
#列表：存储变量,可变(预留空间),有序,灵活(索引/切片)
#元组：存储变量,不可变(不预留空间,按需分配)
#字典：存储键值对,可变,无序(散列),读写速度快(利用空间换取)
list01=[1,2]
print(id(list01))#140688368743112
list01+=[3,4]
print(id(list01))#140688368743112
print(list01)#[1, 2, 3, 4]


tuple01=(1,2)
print(id(tuple01))#140688368744456
tuple01+=(3,4)
print(id(tuple01))#140688368727208
print(tuple01)#(1, 2, 3, 4)

dict01={"as":99}
dict02={"wwe":111}
dict03={**dict01,**dict02}
print(dict03)#{'as': 99, 'wwe': 111}
