# 练习:在控制台中一次获取俩个变量,将俩个变量交换,再输出带控制台中
A = "XXX"
B = "YYY"
C = A
A = B
B = C
print(A, B)

A, B = B, A
print(A, B)

name1 = input("请输入变量1")
name2 = input("请输入变量2")
name = name1
name1 = name2
name2 = name
print(name1, name2)

name1, name2 = name2, name1
print(name1, name2)

#练习:在控制台中获取小时,再获取分钟,再获取秒数,
#        计算总秒数
h = int(input("获取小时"))  #hour
m = int(input("获取分钟"))  #minute
s = int(input("获取秒数"))  #second
result = h * 3600 + m * 60 + s
print("总秒数:" + str(result))

#练习: 在控制台中录入商品单价15
#再录入商品数量2
#最后获取金额, 计算应该找回多少钱
price = float(input("输入商品单价"))
amount = int(input("输入商品数量"))
number3 = int(input("总金额"))
result =float(number3 - price * amount)
print("应找回" +str(result))

#距离=初速度*时间+0.5*加速度*时间**2
#已知:距离,时间,初速度
x=int(input("输入距离"))
t=int(input("输入时间"))
v=int(input("输入初速度"))
a=(2*(x-v*t))/(t**2)
print("加速度为:"+str(a))

#练习:古代的称一斤等于16两,在控制台中获取两,计算几斤零几两
A=int(input("输入两数"))
b=A//16
c=A%16
print(str(b)+"斤"+str(c)+"两")

number=int(input("输入一个四位数"))#1234
d=number%10 #4
c=number//10%10#1234//10=123     123%10=3
b=number//100%10#1234//100=12    12%10=2
a=number//1000#1
result=d+c+b+a
print(str(result))

number=int(input("输入一个四位数"))
result=number%10
result+=number//10%10
result+=number//100%10
result+=number//1000
print(str(result))

# 练习:在控制台中获取一个年份,判断输入的是否式闰年
#   条件1:能被4整除但是不能被100整除
#  条件2:能被400整除
number = int(input("输入一个年份"))
a = number % 4 == 0 and number % 100 != 0
b = number % 400 == 0
result = a or b
print(str(result))
s=int(input("输入总秒数s"))
s1=s%60
m=s//60%60
h=s//3600

print(str(h)+"小时"+str(m)+"分钟"+str(s1)+"秒数")
r=int(input("输入圆形的半径"))
s=3.14*r**2
l=2*3.14*r
print(str(s))
print(str(l))

h=float(input("输入华氏度"))
s=(h-32)/1.8
print(str(s))

s=float(input("输入摄氏度"))
h=s*1.8+32
print(str(h))

h=float(input("输入摄氏度"))
k=h+273.15
print(str(k))

