list01=["无忌","赵敏","周芷若"]
list02=["101","102","103"]
dict={}
for item in range(len(list01)):
    dict[list01[item]]=list02[item]
print(dict)
#需求:根据值找键
#解决:交换键值:键→值 值→键(如果值相同,反过来做为键,会丢失数据)
# [(键,值),(键,值)]
list03 = [(key,value) for key,value in dict.items()]
print(list03)

def fun01(p1):
    p1[0]=300
number=[100,200]
fun01(number)
print(number[0])#300
print("==========")

g01 = 500
def fun01():
  g01 = 600# 没有修改全局变量g01，而是创建了局部变量g01
  print(g01)#600
  # 局部作用域
  l01 = 100

def fun02():
  print(g01)
  # 局部作用域
  l01 = 200

def fun03():
  # 通过global语句，定义g01为全局变量
  global g01
  g01 = 400# 修改的是全局变量


fun03()
fun01()#600
fun02()#300


#剑指offer python版/leetcode
#十大排序python版本[快速排序和归并排序]
#网络IO/TCP/HTTP
#tronado(IO|OOP)/gevent
#跨域
#http://127.0.0.1:8000/index
#http://127.0.0.1:8000
#1.协议 http/https
#2.ip地址:127.0.0.1
#3.端口:8000
a=[2,11,1,2,1,2,1,2,1]
#用集合
#m=set(list)
#print(m)
#用字典
c={}
c=c.fromkeys(a)
d=list(c.keys())
print(d)
print("=====")
#用字典并保持顺序
l1 = ['b','c','d','b','c','a','a']
l2 = list(set(l1))
l2.sort(key=l1.index)
print(l2)
#列表推导式
l1 = ['b','c','d','b','c','a','a']
l2 = []
result=[l2.append(i) for i in l1 if not i in l2]
print(l2)

def fun(p):
    p[0]=100
a=[200,300]
fun(a)
print(a[0])
print(a)

def fun(a):
    a=500
num=600
fun(num)
print(num)

def fun(a):
    a=[100,200]
num=[200,300]
fun(num)
print(num)

g01=500
def fun01():
    g01=600 #600 没有修改全局变量 g01, 而是创建了局部变量 g01
print(g01)

list01=[1,2,1,3,4,8,5,7,4,5,42,5,4586]
iterator=list01.__iter__()
while True:
    try:
        item=iterator.__next__()
        print(item)
    except StopIteration:
        break

tuple01=(2,12,15,45,78,45,246,4,5)
iterator=tuple01.__iter__()
while True:
    try:
        item=iterator.__next__()
        print(item)
    except StopIteration:
        break

dict01={"张三":100,"李四":200}
iterator=dict01.__iter__()
while True:
    try:
        key=iterator.__next__()
        value=dict01[key]
        print(key,value)
    except StopIteration:
        break
        
pre=[1,2,4,7,3,5,6,8]
tin=[4,7,2,1,5,3,8,6]
a=pre[0]
b=pre[1:tin.index(a)+1]
c=tin.index(a)
print(b)
print(c)


def fun01():
    a = 1 # 对于 fun02 而言,属于外部嵌套作用域
    def fun02():
        b = 2
    # print(a)# 可以直接访问外部嵌套变量
    # a = 111 # 又创建了局部变量 a,没有修改外部嵌套变量.
        nonlocal a # 声明外部嵌套变量
        a = 111
        print(a)
    fun02()
    print(a)
fun01()
print(a)

def give_life_money(money):
    print("得到压岁钱：",money)
    def child_buy(target,price):
        nonlocal money
        if money>=price:
            print("孩子需要花钱%d钱,买%s"%(price,target))
        else:
            print("钱不够")
        return child_buy
action_buy=give_life_money(30000)

a=lambda x,y:x+y
s=a(3,11)
print(s)
#请用自己的算法,按升序合并如下两个List , 并去除重复的元素
List1 = [2,3,8,4,9,5,6]
List2 = [5,6,10,17,11,2]
list=List1+List2
print(list)
for i in range(len(list)-1):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
a=set(list)
print(a)