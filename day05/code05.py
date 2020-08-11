#创建列表
list01=[]
list01=list()

#创建具有默认元素的列表
list01=[1,"大","true"]
print(list01)#[1, '大', 'true']

list01=list(range(5))
print(list01)#[0, 1, 2, 3, 4]

list01=list("大小小大")
print(list01)#['大', '小', '小', '大']

#1.添加元素
#append   #追加
list01=list(range(5))
print(list01)#[0, 1, 2, 3, 4]

list01.append("小大")
print(list01)#[0, 1, 2, 3, 4, '小大']

#2.insert    #插入
list01.insert(1,"大小")
print(list01)#[0, '大小', 1, 2, 3, 4, '小大']

#3.remove     #删除
#   del 列表名[索引或切片]
list01.remove("大小")  #del list01[1]
print(list01)#[0, 1, 2, 3, 4, '小大']

#4.修改
list01[1]="大大"
print(list01)#[0, '大大', 2, 3, 4, '小大']

#5.索引和切片
#(1)通过切片获取新的列表
list02=list01[:3]
print(list02)#[0, '大大', 2]

#(2)通过切片可以修改元素
list01[:3]=["a"]
print(list01)#['a', 3, 4, '小大']

#6.查询
#获取列表中的每个元素
#	正向：
#	for 变量名 in 列表名:
#		变量名就是元素
#	反向：
#	for 索引名 in range(len(列表名)-1,-1,-1):
#		列表名[索引名]就是元素
#


#练习：在控制台中录入所有学生的成绩
#   "请录入学生总数＂
#   "请录入第一个学生的成绩＂
#   (1)获取总分(2)获取最高分数(3)获取最低分
list_student_score=[]
student_count=int(input("请录入学生总数："))
for i in range(student_count):
    student_score=float(input("请录入第%d个学生成绩:"%(i+1)))
    list_student_score.append(student_score)
print("总分：%.1f"%sum(list_student_score))
print("最高分：%.1f"%max(list_student_score))
print("最低分：%.1f"%min(list_student_score))

#list01是变量，存储列表对象的地址
#引用列表
list01=["张无忌","赵敏","周芷若"]
list02=list01
#修改的是列表第一个元素存储的对象地址
list01[0]="老张"
print(list02[0])#老张
print(list02)#['老张', '赵敏', '周芷若']

list01=["张无忌","赵敏","周芷若"]
list02=list01
#修改的是变量存储的对象地址
list01="老张"
print(list02[0])#张无忌
print(list01)#老张

list01=["张无忌","赵敏","周芷若"]
#通过切片复制列表(拷贝了列表中的变量，而没有变量指向的对象)
list02=list01[:]
list01[0]="老张"
print(list02[0])#张无忌
print(list01)#['老张', '赵敏', '周芷若']
print(list02)#['张无忌', '赵敏', '周芷若']


list01=["张无忌",["赵敏","周芷若"]]
list02=list01
#修改列表第二个元素的第二个元素
list01[1][1]="芷若"
print(list01[1][1])#芷若
print(list01)#['张无忌', ['赵敏', '芷若']]
print(list02)#['张无忌', ['赵敏', '芷若']]


list01=["张无忌",["赵敏","周芷若"]]
list02=list01.copy()#浅拷贝
list01[1][1]="芷若"
print(list01[1][1])#芷若
print(list01)#['张无忌', ['赵敏', '芷若']]
print(list02)#['张无忌', ['赵敏', '芷若']]

#练习：在控制台中录入所有学生姓名，如果有重复的姓名不存入姓名
#       如果输入esc,则停止录入，在每行打印学生姓名
list_student=[]
while True:
    student_name=str(input("录入学生姓名"))
    if student_name =="esc":
        break
    if student_name in list_student:
        continue
    list_student.append(student_name)
#正向
for item in list_student:
    print(item)
#倒序获取列表中元素，通过索引获取元素
for i in range(len(list_student)-1,-1,-1):
    print(list_student[i])

#练习：将list_score列表中大于６０的元素存入list01中
#       list_score=[60,85,35,26,20,90]
list_score=[60,85,35,20,26,90]
list01=[]
for i in list_score:
    if i>60:
        list01.append(i)
print(list01)

#练习：获取list_score列表中的最大值
#       list_score=[60,85,35,26,20,90]

list_score=[60,85,35,20,26,90]
max_value=list_score[0]
for i in range(1,len(list_score)):
    if max_value<list_score[i]:
        max_value=list_score[i]
print(max_value)

#函数：
#   将多个字符串拼接为一个。
#   result = "连接符".join(列表)
#
#   将一个字符串拆分为多个。
#   列表 = “a-b-c-d”.split(“分隔符”)

#在控制台中重复录入字符串，直到输入esc为止，
#   最后打印拼接后的字符串
list=[]
while True:
    str_number=input("录入字符串")
    if str_number == "esc":
        break
    list.append(str_number)
str_result="".join(list)
print(str_result)

#练习：英文单词反转
# how are you-->you are how
english="how are you"
list_english=english.split(" ")
str_english=" ".join(list_english[::-1])
print(str_english)

#列表推导式
# 语法：
#   变量 = [表达式 for 变量 in 可迭代对象]
#   变量 = [表达式 for 变量 in 可迭代对象 if 条件]
#如果if真值表达式的布尔值为False,则可迭代对象生成的数据将被丢弃。
#列表推导式嵌套

#练习：将list01=[56,36,68,44,868]中所有元素的个位存储到lsit02中
list01=[56,36,68,44,868]
list02=[]
for i in list01:
        list02.append(i%10)
print(list02)#传统方法

list02=[i%10 for i in list01]
print(list02)#推导方法
