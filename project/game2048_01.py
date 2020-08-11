#2048的核心算法
#1.定义函数,将列表中的0元素移到末尾
#   [2,0,2,0]-->[2,2,0,0]
#   [2,0,0,2]-->[2,2,0,0]
#   [2,4,0,2]-->[2,4,2,0]
def zero_to_end(list_target):
    for r in range(len(list_target) - 1, -1, -1):
        if list_target[r]==0:
            list_target.append(0)
            del list_target[r]
list_target= [2, 0, 2, 0]
zero_to_end(list_target)
print(list_target)
#2.定义函数,合并列表中的相同元素
#   [2,0,2,0]-->[4,0,0,0]
#   [2,0,0,2]-->[2,2,0,0]-->[4,0,0,0]
#   [2,2,0,2]-->[4,0,0,2]-->[4,2,0,0]
#   [2,2,0,4]-->[4,0,0,4]-->[4,4,0,0]
def merge(list_target):
    zero_to_end(list_target)
    for r in range(len(list_target)-1):
            if list_target[r]==list_target[r+1]:
                list_target[r]+=list_target[r+1]
                del list_target[r+1]
                list_target.append(0)
list_target= [2, 2, 0, 4]
merge(list_target)
print(list_target)
#3.定义函数,向左移动二维列表
#[   [2,2,0,2],
#    [0,2,0,4],
#    [2,0,4,2],
#    [0,4,2,2],]
def move_left(map):
    #思想:将每行(二维列表的每个元素)传递给合并函数
    for row in map:
        #传递给merege函数的二维列表
        merge(row)
list=[
    [2,2,0,2],
    [0,2,0,4],
    [2,0,4,2],
    [0,4,2,2],
    ]
move_left(list)
print(list)
#4.定义函数,向右移动二维列表
#[   [2,2,0,2],
#    [0,2,0,4],
#    [2,0,4,2],
#    [0,4,2,2],]
def move_right(map):
    for i in range(len(map)):
        list_merge=list[i][::-1]
        merge(list_merge)
        list[i][::-1]=list_merge
list=[
    [2,2,0,2],#2020      4000   4442
    [0,2,0,4],#2204      4400   0424
    [2,0,4,2],#0042      4200   0004
    [0,4,2,2],#2422      2440   0000
    ]
move_right(list)
print(list)

#5.定义函数,向上移动二维列表
# (核心思想:从上到下获取列数据,形成一维列表,交给合并方法,最后恢复)
#依次获取第一,二,三,四个列表的第一个数,依次获取第一,二,三,四个列表的第二个数
#依次获取第一,二,三,四个列表的第三个数,依次获取第一,二,三,四个列表的第四个数
#组成一个新的列表,调用函数1和2,最后还原
def move_up(map):
    for r in range(len(map)):
        list_merge=[]
        for c in range(4):
            list_merge.append(map[c][r])
        merge(list_merge)
        for c in range(4):
            map[c][r]= list_merge[c]
list=[
    [2,2,0,2],#0202     0004    /   4000
    [0,2,0,4],#4022     0044    /   4400
    [2,0,4,2],#2400     0024    /   2400
    [0,4,2,2],#2242     0442    /   0000
    ]
move_up(list)
print(list)
#6.定义函数,向下移动二维列表
# (核心思想:从下到上获取列数据,形成一维列表,交给合并方法,最后恢复)
def move_down(map):
  # 30  20  10  00
  for c in range(4):
    list_merge = []
    for r in range(3, -1, -1):
      list_merge.append(map[r][c])
    merge(list_merge)
    # list_merge(从左到右) 赋值给 二维列表(从下到上)
    for r in range(3, -1, -1):  # 3 2 1 0
      map[r][c] = list_merge[3 - r]
list=[
    [2,2,0,2],#
    [0,2,0,4],#
    [2,0,4,2],#
    [0,4,2,2],#
    ]
move_right(list)
print(list)