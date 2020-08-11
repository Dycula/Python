#1.三合一
#2.每天练习独立完成
#3.在控制台中获取月份,显示季度或者提示月份错误
month=int(input("输入月份"))
if 0<month<=3:
    print("该月份是春季")
elif month<=6:
    print("该月份是夏季")
elif month<=9:
    print("该月份是秋季")
elif month<=12:
    print("该月份是冬季")
else:
    print("提示:输入月份错误")
    
#4.在控制台中获取年份,月份,显示该月份的天数
#   2月闰年29天平年28天
year=int(input("输入年份"))
month=int(input("输入月份"))
if month<1 or month>12:
    print("输入月份有误")
elif month==4 or month==6 or month==9 or month==11:
    month=30
    print(month)
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    month = 31
    print(month)
elif year%4==0 and year%100!=0 or year%400==0:
    month02=29
    print(month02)
else:
    month02=28
    print(month02)
    
#5.根据身高体重,参照BMI返回身体状况
#   BMI:用体重千克数除以身高米数平方得出数字
#   中国参考标准:
#    体重过低BMI<18.5
#    正常范围18.5<=BMI<24
#    超重24<=BMI<28
#    I度肥胖28<=BMI<30
#    II度肥胖30<=BMI<40
#    III度肥胖BMI>40
weight=float(input("输入体重千克"))
height=float(input("输入身高米数"))
BMI=weight/(height**2)
if BMI<18.5:
    print("体重过低")
elif 18.5<=BMI<24:
    print("正常范围")
elif 24<=BMI<28:
    print("超重")
elif 28<=BMI<30:
    print("I度肥胖")
elif 30<=BMI<40:
    print("II度肥胖")
else:
    print("III度肥胖")
#6.累加1~100之间的整数
n=int(input("输入整数"))    #输入0
count=0
while count<100:
    count+=1
    n+=count
    print(n)
#7.阅读:程序员的数学第四章

