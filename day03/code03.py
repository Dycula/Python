sex=input("请输入性别")
if sex == "男":
    print("您好,先生")
elif sex== "女":
    print("您好,女士")
else:
    print("性别未知")

#调试:让程序中断,逐步运行语句,审查程序执行过程(流程,变量取值)
#步骤:
#1.加入断点(单击左键)
#2.调试运行(单击右键,运行Debug)
#3.逐过程执行(F8)
#4.停止调试(Ctrl+F2)

#练习: 在控制台中录入商品单价
#再录入商品数量
#最后获取金额, 计算应该找回多少钱
price = float(input("输入商品单价"))
amount = int(input("输入商品数量"))
number3 = int(input("总金额"))
number4=float(price * amount)
result =float(number3 - number4)
if result>= 0:
    print("应找回" +str(result))
else:
    print("还应给:"+str(result*-1))

#练习:在控制台中获取季度.显示该季度有多少个月
a=str(input("请输入季度"))
if a=="春":
    print("春天的月份:1,2,3")
elif a=="夏":
    print("夏天的月份:4,5,6")
elif a=="秋":
    print("秋天的月份:7,8,9")
else:
    print("冬天的月份:10,11,12")

#练习:在控制台中获取俩个数字,一个运算符(+-*/)
#根据运算符,计算俩个数字(备注:如果输入的运算符有误,提示:输入的运算符有误)
number1=float(input ("输入第一个数字"))
number2=float(input("输入第二个数字"))
a=input("请输入运算符")
if a == "+":
    result=number1+number2
    print(result)
elif a == "-":
    result=number1-number2
    print(result)
elif a == "*":
    result=number1*number2
    print(result)
elif a == "/":
    result=number1/number2
    print(result)
else:
    print("输入的运算符有误")

#在控制台中录入四个数字,显示最大的数字
number1=float(input("输入第一个数字"))
number2=float(input("输入第二个数字"))
number3=float(input("输入第三个数字"))
number4=float(input("输入第四个数字"))
max=number1
if max<number2:
    max=number2
elif max<number3:
    max=number3
elif max<number4:
    max=number4
    print(max)

#练习:在控制台中录入一个成绩,显示优秀/良好/及格/不及格/有误
#优秀:90-100
#良好:80-90
#及格:60-80
#不及格:0-60
socre=float(input("录入一个成绩"))
if 100>socre >=90:
    print("优秀")
elif 90>socre >= 80:
    print("良好")
elif 80>socre >= 60:
    print("及格")
elif 60>socre >= 0:
    print("不及格")
else:
    print("录入有误")

#练习:在控制台中录入一个年份,如果是闰年,给变量month02赋值:29,否则赋值28
number=int(input("录入一个年份"))
if number%4==0 and number%100!=0 or number%400==0:
    month02=29
    print(month02)
else:
    month02=28
    print(month02)      #第一种方法

number=int(input("录入一个年份"))
result=number%4==0 and number%100!=0 or number%400==0
month02=29 if result  else 28
print(month02)

#练习:在控制台中录入一个整数,如果是奇数,给变量state赋值"奇数",否则赋值"偶数"
state =int(input("录入一个整数"))
if state%2!=0:
    state="奇数"
    print(state)
else:
    state="偶数"
    print(state)  #第一种方法
    
state =int(input("录入一个整数"))
state="奇数" if state%2!=0 else "偶数"
print(state)  #第二种方法

state =int(input("录入一个整数"))
if state%2:         #if bool(state%2)真值表达式
    state = "奇数"
    print(state)
else:
    state = "偶数"
    print(state)  #第三种方法

#练习:在控制台中获取一个开始值和一个结束值,将中间的数字显示出来
begin=int(input("输入一个开始值"))
end=int(input("输入一个结束值"))
while begin<end-1:
    begin +=1
    print(begin)

#练习:一张纸的厚度是0.01毫米,请计算:对折多少次超过珠穆朗玛峰的高度8833.43米
thickness=0.01/1000
count=0
while thickness<=8844.43:
    thickness*=2
    count+=1
    print(count)

#猜数字游戏
#游戏运行产生1...100之间的额随机数
#让玩家重复猜测,直到猜对为止
#提示:大了,小了,猜对了
import random
random_number = random.randint(1,100)
print(random_number)
count=0
while True:
    count += 1
    input_number=int(input("请输入整数:"))
    if random_number>input_number:
        print("小了")
    elif random_number<input_number:
        print("大了")
    else:
        print("猜对了,总共猜了"+str(count)+"次")
        break


