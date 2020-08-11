#day05作业
#1.三合一
#2.每天作业独立完成
#3.计算列表中的最小值(不使用min)
list=[213,54,5641,857,787]
min_number=list[0]
for i in range(1,len(list)):
    if min_number>list[i]:
        min_number=list[i]
print(min_number)

#4.彩票　　双色球
#红色7个：1~33之间的整数　　不能重复
#蓝色1个：1~17之间的整数
#(1)随机产生一注彩票[7个红球1个篮球]
import random
list=[]
n=0
random_bull = random.randint(1, 17)
list.insert(0, str(random_bull))

while True:
    random_red= random.randint(1,33)
    if n<7 and random_red not in list:
        list.append(str(random_red))
    elif random_red in list:
       continue
    n+=1
    print(list)

#第二种方法
import random
list_ticket=[]
while len(list_ticket)<7:
    random_red= random.randint(1,33)
    if random_red not in list_ticket:
        list_ticket.append(str(random_red))
    elif random_red in list:
        print("号码重复，请重新输入")
        continue
random_bull = random.randint(1, 17)
list_ticket.insert(0, str(random_bull))
print(list_ticket)


#(2)在控制台中购买一注彩票
#提示："请输入第1个红球号码："
#　　　"请输入第2个红球号码："
#    　"号码不在范围内"
#    　"号码已经重复"
#    　"请输入篮球号码"

list01=[]
n=0
while n<7:
    red_number=int(input("请输入第%d个红色球号"%(n+1)))
    n += 1
    if 0< red_number < 34 and red_number  not in list01:
            list01.append(red_number)
    elif red_number in list01:
        print("号码重复，请重新输入")
    else:
        print("号码不在范围内，请重新输入")
        continue

bull_number=int(input("请输入蓝色球号"))
if bull_number>17 or bull_number<1:
    print("号码不在范围内,请重新输入蓝色球号")
else:
    list01.insert(0,bull_number)
print(list01)

#第二种方法
list_ticket=[]
count=0
while len(list_ticket)<7:
    number=int(input("请输入第%d个红色球号"%(len(list_ticket)+1)))
    if number <1 or number >33:
        print("号码不在范围内,请重新输入红色球号")
    elif number in list_ticket:
        print("号码重复，请重新输入")
    else:
        list_ticket.append(number)

while True:
    number01 =int(input("请输入篮球号码"))
    if number01>17 or number01<1:
        print("号码不在范围内,请重新输入蓝色球号")
    else:
        list_ticket.insert(0,number01)
        break
print(list_ticket)
    
    
    
#5.阅读python入门到实践的第三章和第四章#

#容器：
#列表
#(1)内存图
#(2)定义
#(3)适用性
#(4)操作：
#    创建
#    添加: 列表名.append()
#    删除: 列表名.remove()或者del 列表名[索引或切片]
#    定位：列表名.insert(索引或切片,元素)
#    查询:
#       正向：
#       for 变量名 in 列表名:
#        反向：
#       for 索引名 in range(len(列表名)-1,-1,-1):











