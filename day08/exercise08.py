#day08作业
#1.三合一
#2.每天作业独立完成
#3.自学字符串/列表/字典常用函数(参照菜鸟教程)
#4.删除列表中所有的偶数[3,2,4,6,8,8,8,5,3]
#5.玩2048游戏(了解游戏规则)
#6.重构shopping.py程序
#7.阅读python从入门到实践第八章

list=[3,2,4,6,8,8,8,5,3]
for i in range(len(list)-1,-1,-1):
    if list[i]%2==0:
        del list[i]
print(list)

list=[3,2,4,6,8,8,8,5,3]
list01=[]
for item in list:
    if item%2!=0 :
        list01.append(item)
print(list01)

def not_even_number(list):
    list01=[]
    for i in range(len(list)):
        item=list[i]
        if item % 2 != 0 :
            list01.append(item)
    return list01

list=[3,2,4,6,8,8,8,5,3]
a=not_even_number(list)
print(a)



#if语法：变量 = 结果1 if 条件 else 结果2
#列表推导式 语法：
#   变量 = [表达式 for 变量 in 可迭代对象]
#   变量 = [表达式 for 变量 in 可迭代对象 if 条件]
#列表推导式嵌套语法：
#   变量 = [表达式 for 变量1 in 可迭代对象1 for 变量2 in可迭代对象2]
#字典推导式语法:
#   {键:值 for 变量 in 可迭代对象}
#   {键:值 for 变量 in 可迭代对象 if 条件}
#集合推导式语法:
#   {表达式 for 变量 in 可迭代对象}
#   {表达式 for 变量 in 可迭代对象 if 条件}

#复习：
#函数：
#1.定义:一个/单一         的功能
#2.语法:  　def 函数名(形式参数)
#              函数体
#        参数:要求调用者必须提供的信息,根据形参传递信息
#        返回值:函数定义者告诉定义者的信息
#        作用：代码重用　　　(维护性高)结构清晰
#3.实际参数：
#        位置传参
#        序列传参
#        关键字传参
#        字典传参
#　　形式参数：
#        默认/缺省参数
#        位置形参
#        星号元组形参
#        命名关键字形参
#        双星号字典形参