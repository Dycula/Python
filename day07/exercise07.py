#day07作业
#1.三合一
#2.独立完成作业
#3.定义函数,在控制台中打印矩形函数
def print_rect(r_count,c_count,char):
#    '''

#    :param r_count: 行数量,int类型
#    :param c_count: 列数量,int类型
#    :param char: 填充矩形的字符,str类型
#    :return:
#    '''
    for r in range(r_count):
        #内循环控制列
        for c in range(c_count):
            print(char,end=" ")
        print()


print_rect(3,2,"*")
print_rect(5,4,"#")


#4.定义函数,在控制台中打印二维列表函数
list01=[[2,4,8,6],[3,6,9,1]]
def print_double_list(list_target):
    '''
    在控制台中打印二维列表
    :param list_target: 二维列表
    :return:
    '''
    for r in range(len(list01)):
        # 内循环控制列
        for c in range(len(list01[r])):
            print(list01[r][c],end=" ")
        print()

print_double_list(list01)



#5.(扩展)计算2~100之间的素数存入列表
#素数:只能被1和本身整除的数字2 3 4 5 6 7 8 9
#算法:判断从2开始到当前数字之间,是否存在可以被整除的数,\
#    如果存在则不是素数,如果存在则是素
#核心：从２到数字之间能否被整除
list=[]
for r in range(2,101):
    for c in range(2,r):
        if  r%c ==0:
            break
    else:
        list.append(r)
print(list)
#计算1~100之间的素数存入列表
list=[]
for r in range(1,101):
    if r == 1:
        continue
    for c in range(2,r):
        if  r%c ==0:
            break
    else:
        list.append(r)
print(list)
#复习：
#容器：
#str
#list：序列(有序),灵活(索引/切片)
#tuple
#dict:散列(无序),读取速度快
#set
#函数：
#  概念：功能
#   语法:
#      def 函数名(形式参数):
#           函数体
#
#       函数名(实际参数)'''