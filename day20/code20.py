"""
linklist.py 链表程序实现
重点代码
思路分析:1.创建节点类,生成节点对象,包含数据和下一个节点的引用
        2.链表类,生成链表对象,可以对链表进行数据操作
"""
#节点类
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
#链表类
class Linklist:
    """
    建立链表模型,进行链表操作
    """
    def __init__(self):
        """
        初始化链表,生成一个头节点,表示链表开始节点
        """
        self.head=Node(None)
    #添加一组链表节点
    def init_list(self,list_):
        p=self.head     #p为移动变量
        for item in list_:
            p.next=Node(item)
            p=p.next        #p向后移动一个节点

    def show(self):#遍历链表
        p=self.head.next    #第一个有效节点
        while p is not None:
            print(p.data,end=" ")
            p=p.next
        print()     #换行

    #获取链表长度
    def get_length(self):
        n=0
        p=self.head
        while p.next is not None:
            n+=1
            p=p.next
        return n

    #判断链表是否为空
    def is_empty(self):
        if self.get_length()==0:
            return True
        return False

    #清空链表
    def clear(self):
        self.head.next=None

    #尾部插入节点
    def append(self,data):
        node=Node(data)     #生成节点
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=node

    #选择位置插入节点
    def insert(self,index,data):
        if index<0 or index>self.get_length():
            raise IndexError("index out of range")
        p=self.head
        for i in range(index):
            p=p.next
        node=Node(data) #生成节点
        #插入
        node.next=p.next
        p.next=node

    #删除节点
    def delete(self,data):
        p=self.head
        while p.next and p.next.data!=data:
            p=p.next
            #判断循环结束的原因
            if p.next is None:
                raise ValueError("value is error")
            else:
                p.next=p.next.next

    #获取节点值
    def get_item(self,index):
        if index<0 or index>self.get_length():
            raise IndexError("index out of range")
        p=self.head.next
        for i in range(index):
            p=p.next
        return  p.data


#链表对象
# link-->head
# link.head--->data==None
# link.head--->next==None
link=Linklist()
l=[1,2,3,4,5]
link.init_list(l)
link.show()#1 2 3 4 5
print("link.length:",link.get_length()) #link.length: 5
link.append(6)
link.show()#1 2 3 4 5 6
link.insert(4,100)
link.show()#1 2 3 4 100 5 6
link.delete(3)
link.show()

