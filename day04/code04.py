#for 语句
#   1. 作用:
#   用来遍历可迭代对象的数据元素。
#迭代对象是指能依次获取数据元素的对象，例如：容器类型。
#   2. 语法:
#   for 变量列表 in 可迭代对象:
#       语句块1
#   else:
#       语句块2
#   3. 说明:
#   else子句可以省略。
#   在循环体内用break终止循环时,else子句不执行。

#for:相比while循环,做一定次数的循环更好
#while:不知道循环的次数时运用
thickness=0.01e-3
count=0
while count<5:
     thickness*=2
     count+=1
     print(thickness)

#for循环对折五次
thickness=0.01e-3
for count in range(5):
    thickness *= 2
    print(thickness)

#跳转语句
# break
#continue

#练习:累加1~100之间的整数
sum=0
for count in range(1,101,1):
    sum+=count
    print(sum)

#练习:累加5~58之间的整数
sum=0
for count in range(5,59,1):
    sum+=count
    print(sum)

#练习:累加6~20之间的偶数
sum=0
for count in range(6,21,2):
    sum+=count
    print(sum)

#练习:累加10~50之间个位是2,5,7的整数
sum=0
for count in range(10,51,1):
    if count % 10 == 2 or count % 10 == 5 or count % 10 == 7:
        sum+=count
        print(sum)

#练习:随机加法考试
#    随机产生俩个数字计算(1~10),在控制台中获取俩个数字相加
#    如果输入正确得10分
#    如果输入错误扣除5分
#    总计3道题

import random
#产生俩个随机数并计算俩个随机数之和
random_number01 = random.randint(1,10)
random_number02 = random.randint(1,10)
sum=0
a=int(input("请计算"+"random_number01"+"+"+"random_number02"+"=?"))
result=random_number01+random_number02
for a in range(1,4,1):
    if a==result:
        sum+=10
        print(sum)
    else:
        sum-=5
        print(sum)

#相关函数
#   1. bin(整数) :将整数转换为二进制字符串
#   2. ord(字符串):返回该字符串的Unicode码
#   3. chr(整数):返回该整数对应的字符串
#练习:在控制台中获取一个字符串,打印每个字符的编码值

number=str(input("输入一个字符串"))
for result in number:
    print(ord(result))

#练习:在控制台中重复录入一个编码值,打印字符
#     如果没有输入编码值,而直接回车,则退出循环
while True:
    str_code=input("请输入编码值")
    if str_code=="":
        break
    print(chr(int(str_code)))

#字符串格式化:
# 练习:  在控制台中按照如下格式输出:
#       圆形的面积是52.5,周长是35.25.
#       其中圆形是变量,面积和周长的值是变量
print("%s的面积是%.1f,周长是%.2f"%("圆形",52.5,35.25))

#练习:在控制台中显示120秒的倒计时,02:00-->01:59
for second in range(120,-1,-1):
    print("%02d:%02d"%(second//60,second%60))

#练习:在控制台中随机产生一个秒数(1~4000),并按照倒计时显示出来
import random
random_number = random.randint(1,4000)
for second in range(random_number,-1,-1):
    print("%02d:%02d:%02d"%(second//3600,second//60%60,second%60))

#数学运算符
# 1. +：用于拼接两个容器
# 2. +=：用原容器与右侧容器拼接,并重新绑定变量
# 3. *：重复生成容器元素
# 4. *=：用原容器生成重复元素, 并重新绑定变量
# 5. < <= > >= == !=：依次比较两个容器中元素,一但不同则返回比较结果#。
str_a="大"
str_b="小"
str_a=str_a+str_b
print(str_a)#大小
str_a+=str_b
print(str_a)#大小小
str_a=2*str_b
print(str_a)#小小
str_a*=2
print(str_a)#小小小小

#练习:在控制台中获取一个字符串
str_number="hellopython"
#如果长度是奇数,打印中间的字符
if len(str_number) % 2 == 1:
    print(str_number[len(str_number) // 2])
print(str_number[0])#打印第一个字符
print(str_number[-len(str_number)])#打印第一个字符
print(str_number[-1])#打印最后一个字符
print(str_number[len(str_number)-1])#打印最后一个字符
print(str_number[-3:])#打印倒数三个字符
print(str_number[::-1])#倒序打印字符

