result = input("123")
print("result")
A = input("录入学生信息")
str_name = input("请输入姓名")#string
int_age = input("请输入年龄")#int
float_score = input("请输入成绩")#float
str_sex = input("请输入性别")#string/bool
print(str_name, int_age, float_score, str_sex)


#作业:
#1.温度转换器:
#(1)摄氏度=(华氏度-32)/1.8
#(2)华氏度=摄氏度*1.8+32
#(3)开氏度=摄氏度+273.15
#在控制台中获取华氏度,计算摄氏度
h=float(input("输入华氏度"))
s=(h-32)/1.8
print(str(s))

#在控制台中获取摄氏度氏度,计算华氏度
s=float(input("输入摄氏度"))
h=s*1.8+32
print(str(h))

#在控制台中获取摄氏度氏度,计算开氏度氏度
h=float(input("输入摄氏度"))
k=h+273.15
print(str(k))
#2.在控制台中录入圆形的半径
#计算面积(3.14*r**2)与周长(2*3.14*r)
r=float(input("输入圆形的半径"))
s=3.14*r**2
l=2*3.14*r

#四舍五入,保留俩位数字用round()
s=round(s,2)
#四舍五入,保留三位数字
l=round(l,3)
print(str(s))
print(str(l))

#3.拓展在控制台中录入总秒数
#计算几小时零几分钟零几秒
s=int(input("输入总秒数s"))
s1=s%60
m=s//60%60
h=s//3600
print(str(h)+"小时"+str(m)+"分钟"+str(s1)+"秒数")
#4.阅读
#(1)python入门大实践,至少前俩章
#(2)程序员的数学,至少前三章



#数据的基本运算
#1.变量
#(1)语法:名称 = 数据
#(2)运用性:临时存储数据
#(3)内存:名称就是真实的内存地址的别名
#        变量存储数据的地址
#2.del语句
#(1)语法:del 变量
#(2)作用:删除变量
#(3)对象的引用计数:当对象引用计数时,对象被销毁
#3.数据类型
#(1)变量没有类型,指向的对象有类型
#(2)None:占位,解除绑定
#(3)整形int:整数
#(4)浮点型float:小数
#(5)字符串str:文本
#(6)布尔型bool:true(真)/false(假)
#(7)复数complex:实部和虚部 例如:1+2j
#4.转换
#int()  float()   str()
#bool(1.5)
#5.运算符
#算数运算符:+　－　＊　/
#        //(地板除)
#        %（求余）
#增强运算符：+=  -= *= /= //= %= **=
#比较运算符：>  <  ==
#          >=    <=  !=
#逻辑运算符：&&(与)　
#          ||(或)
#          ！(非)
#