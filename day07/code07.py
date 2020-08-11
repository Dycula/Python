#字典推导式
#1. 定义：
#   使用简易方法，将可迭代对象转换为字典。
#2. 语法:
#    {键:值 for 变量 in 可迭代对象}
#    {键:值 for 变量 in 可迭代对象 if 条件}

list=["无忌","赵敏","周芷若"]
dict={}
for item in list:
    dict[item]=len(item)
    print(dict)

list01=["无忌","赵敏","周芷若"]
list02=["101","102","103"]
dict={}
for item in range(len(list01)):
    dict[list01[item]]=list02[item]
print(dict)

#需求:根据值找键
#解决:交换键值:键->值　值->键(如果值相同,反过来做为键,会丢失数据)

#1. 创建空集合：
#   集合名 = set()
#   集合名 = set(可迭代对象)
s01=()

#2. 创建具有默认值集合：
#   集合名 = {1, 2, 3}
#   集合名 = set(可迭代对象)
s02={1, 2, 3}
s03=set("fduytfu")
print(s03)#{'f', 'd', 'u', 't', 'y'}

#3. 添加元素：
#   集合名.add(元素)
s03.add("uihi")
print(s03)#{'f', 'd', 'uihi', 'u', 't', 'y'}

# 4. 删除元素：
#   集合名.discard(元素)
s03.remove("u")
print(s03)#{'f', 'd', 't', 'uihi', 'y'}

s1 = {1, 2, 3}
s2 = {2, 3, 4}
#交集＆：得到的是相同的元素
s3 = s1 &s2
print(s3)# {2,3}

#并集：得到的是所有不重复的元素
s3=s1|s2
print(s3)# {1,2,3,4}

#补集-：返回只属于其中之一的元素
s3=s1-s2
print(s3)#  {1}  属于s1但不属于s2

#补集^：返回不同的的元素
s3=s1^s2
print(s3)# # {1, 4}  等同于(s1-s2 | s2-s1)

#子集<：判断一个集合的所有元素是否完全在另一个集合中
#超集>：判断一个集合是否具有另一个集合的所有元素
s1 = {1, 2, 3}
s2 = {2, 3}
s2 < s1  # True
s1 > s2  # True

#相同或不同== !=：判断集合中的所有元素是否和另一个集合相同。
s1 = {1, 2, 3}
s2 = {3, 2, 1}
s1 == s2  # True
s1 != s2  # False

#子集或相同 <=
#超集或相同>=

#练习:在控制台中随意录入字符串,输入esc则停止,然后打印所有不重复的字符串
s01=set()
while True:
    str=input("请输入字符串")
    if str == "esc":
        break
    else:
        s01.add(str)
print(s01)

#练习:
#经理:曹操,刘备,孙权
#技术员:曹操,刘备,张飞,关羽
s01=frozenset(["曹操","刘备","孙权"])
s02=frozenset(["曹操","刘备","张飞","关羽"])
print(s01&s02)

#俩个for循环
for r in range(2):
    for c in range(3):
        print("*",end=" ")
    print()

for r in range(3):
    for c in range(5):
        if c%2==0:
            print("*",end=" ")
        else:
            print("#",end=" ")

    print()

for r in range(4):
        for c in range(r+1):
            print("#", end=" ")
        print()

#练习:从小到大排序[3,4,45,5,7,9]
#重点:列表中的元素俩俩比较
#思想:
# 拿第一个元素与后面的元素进行比较3  6
# 拿第二个元素与后面的元素进行比较
# 拿第三个元素与后面的元素进行比较(进行到倒数第二个)
#交换：发现后面的元素更小,交换俩个元素
list=[3,4,45,5,7,9]
for r in range(len(list)-1):
    for c in range(r+1,len(list)):
        if list[r]>list[c]:
            list[r],list[c]= list[c],list[r]
print(list)


#练习:判断列表中是否有相同的元素
#思路:列表中所有元素俩俩比较,发现相同元素就得出结论
#    所有元素比较后,没有发现元素就得出结论
list=[3,4,45,5,7,5]
result=False
for r in range(len(list)-1):
    for c in range(r+1,len(list)):
        if list[r]==list[c]:
           print("发现相同元素")
           result=True
           break
        if result:
            break
if not result:
    print("没有发现相同元素")


#定义函数
#1. 语法：
#   def 函数名(形式参数):
#       函数体
#2. 说明：
#   def 关键字：全称是define，意为”定义”。
#   函数名：对函数体中语句的描述，规则与变量名相同。
#   形式参数：方法定义者要求调用者提供的信息。
#   函数体：完成该功能的语句。
#3. 函数的第一行语句建议使用文档字符串描述函数的功能与参数。
#
def attack():
    print("左勾拳")
    print("右勾拳")

attack()
attack()

def attack_repeat(count):
    for i in range(count):
        print("左勾拳")
        print("右勾拳")
attack_repeat(3)

def number(char,row):
    
    for r in range(row):
        for c in range(r+1):
            print(char,end=" ")
        print()

number("$",4)
number("@",3)

























































