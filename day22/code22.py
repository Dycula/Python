#自定义队列异常
class QueueError(Exception):
    pass

#队列操作类
class Squeue:
    def __init__(self):
        self._elems=[]

    #判断队列空
    def is_empty(self):
        return self._elems==[]

    #入队(从列表的尾部)
    def enqueue(self,elem):
            self._elems.append(elem)

    #出队(从列表的开头)
    def dequeue(self):
        if not self._elems:
            raise QueueError("Queue is empty")
        return self._elems.pop(0)
if __name__=="__main__":
    sq=Squeue()
    sq.enqueue(10)
    sq.enqueue(20)
    sq.enqueue(30)
    while not sq.is_empty():
        print(sq.dequeue())#10 20 30

#递归思想和实践
#编写一个函数,传入一个整数,返回该整数的阶乘.
def multiply(n):
    number=1
    for i in range(1,n+1):
        number*=i
    return number
print(multiply(6))

#求n的阶乘
def recursion(n):
    #递归的终止条件
    if n<1:
        return 1
    return n*recursion(n-1)
print("n!=",recursion(6))

#计算1到n的总和
def add(n):
    if n<1:
        return 0
    return  n+add(n-1)
print(add(100))

"""
二叉树的实现
思路分析:1.使用链式存储,节点设计上有俩个属性变量引用左孩子和右孩子
        2.操作类完成二叉树的遍历
"""

#二叉树的节点
class TreeMode:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

#二叉树的操作类
class Bitree:
    def __init__(self,root=None):
        self.root=root  #获取树根

    #先序遍历
    def preOrder(self,node):
        if node is None:
            return
        print(node.data,end=" ")
        self.preOrder(node.left)
        self.preOrder(node.right)

    # 中序遍历
    def minOrder(self, node):
        if node is None:
            return
        self.minOrder(node.left)
        print(node.data, end=" ")
        self.minOrder(node.right)

    # 后序遍历
    def lastOrder(self, node):
        if node is None:
            return
        self.lastOrder(node.left)
        self.lastOrder(node.right)
        print(node.data, end=" ")

    #层次遍历
    def levelOrder(self,node):
        sq=Squeue()
        sq.enqueue(node)    #从node遍历
        while not sq.is_empty():
            node=sq.dequeue()   #出队一个
            print(node.data,end=" ")
        if node.left:
            self.levelOrder(node.left)
        if node.right:
            self.levelOrder(node.right)



if __name__=="__main__":
    #后序遍历ＢＦＧＤＩＨＥＣＡ
    #构建数
    b=TreeMode("B")
    f=TreeMode("F")
    g=TreeMode("G")
    d=TreeMode("D",f,g)
    i=TreeMode("I")
    h=TreeMode("H")
    e=TreeMode("E",i,h)
    c=TreeMode("C",d,e)
    a=TreeMode("A",b,c)#树根
    #初始化树对象,得到树根
    bt=Bitree(a)
    #先序
    bt.preOrder(bt.root)
    print()
    # 中序
    bt.minOrder(bt.root)
    print()
    # 后序
    bt.lastOrder(bt.root)
    print()
    #层次遍历
    bt.levelOrder(bt.root)
    print()


"""
基本排序算法
"""
#冒泡排序
def bubble(list):
    #外层循坏表达比较多少轮
    for i in range(len(list) - 1):
        #内层循坏把控比较次数
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
list=[12,21,125,3,65,54,13,574,8]
bubble(list)
print(list)

#选择排序
def select(list):
    # 外层循坏表达比较多少轮
    for i in range(len(list) - 1):
        min=i   #假设list[i]是最小值
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min=j
        if min!=i:
            list[i], list[min] = list[min], list[i]

list=[12,21,125,3,65,54,13,574,8]
select(list)
print(list)

"""
def select(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
"""
#插入排序
def insert(list):
    for i in range(1,len(list)):
        x=list[i]
        j=i-1
        while j>=0 and list[j]>x:
            list[j+1]=list[j]
            j-=1
            list[j+1]=x
list=[12,21,125,3,65,54,13,574,8]
insert(list)
print(list)


# 完成一轮排序过程
def sub_sort(list,low,high):
  #　基准数
  x = list[low]
  while low < high:
    #　后面的数小于ｘ放到前面的空位
    while list[high] >= x and high > low:
      high -= 1
    list[low] = list[high] #　将数往前甩
    while list[low] < x and low < high:
      low += 1
    list[high] = list[low]
  list[low] = x #　将基准数插入
  return low

#　快排 low 第一个数序列号　high 最后一个数序列号
def quick(list,low,high):
  if low < high:
    key = sub_sort(list,low,high)
    quick(list,low,key - 1)
    quick(list, key+1, high)

l = [3,7,6,5,8,3,4,2]
quick(l,0,7)
print(l)


"""
基本查找方法
"""
#对有序数列进行二分查找
def search(list,key):
  low,high = 0,len(list) - 1
  while low <= high:
    mid = (low + high) // 2
    if list[mid] < key:
      low = mid + 1
    elif list[mid] > key:
      high = mid - 1
    else:
      return mid

l = [1,2,3,4,5,6,7,8,9,10]
print("Key index is:",search(l,6))









