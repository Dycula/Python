"""
栈模型的顺序存储
重点代码
思路分析:1.列表即顺序存储,但是功能太多,不符合栈模型
    　　2.利用列表,封装类,提供栈的接口方法
"""

# 自定义异常类
class SstackError(Exception):
    pass

# 顺序栈类封装
class Sstack:
    def __init__(self):
        # 属性为空列表,这个列表就是栈的存储空间
        # 列表最后一个元素为栈顶元素
        self._elems = []

    # 判断栈是否为空
    def is_empty(self):
        return self._elems == []

    # 入栈
    def push(self, elem):
        self._elems.append(elem)

    # 出栈
    def pop(self):
        # self._elems为空则if语句为真
        if not self._elems:
            raise SstackError("Sstack is empty")
        return self._elems.pop()  # 弹出列表最后一个

    # 查看栈顶元素
    def top(self):
        # self._elems为空则if语句为真
        if not self._elems:
            raise SstackError("Sstack is empty")
        return self._elems[-1]

if __name__ == "__main__":
    st = Sstack()  # 初始化栈
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())#30 20 10


# 练习:一段文字,在文字中可能存在括号配对错误的情况,
# 要求:写一段代码来检测这段文字中有没有括号书写错误.括号包含:{} []()

text = "hjo{lfspj(fpouji9ogpfhjog)vh[jn]aosdihgv)aolp}ihnldnmlskn"
parens = "{} [] ()"  # 需要验证的字符
left_parens = "{ [ ("
opposite = {"}": "{", "]": "[", ")": "("}  # 验证配对是否正确
st = Sstack()  # 初始化一个类

# 负责提供遍历的括号
def parent(text):
    """
    遍历字符串,提供括号字符和其位置
    """
    i, text_len = 0, len(text)
    while True:
        # 循坏遍历字符串到结尾结束,遇到括号提供给ver
        while i < text_len and text[i] not in parens:
            i += 1
        if i >= text_len:
            return
        else:
            yield text[i], i
            i += 1

# 字符是否匹配的验证工作
def ver():
    for pr, i in parent(text):
        if pr in left_parens:
            st.push((pr, i))  # 左括号人栈
        elif st.is_empty() or st.pop()[0] != opposite[pr]:
            print("Unmatching is found at %d for %s" % (i, pr))
            break
            # for循环正常结束
    else:
        if st.is_empty():
            print("All parenthess are matched")
        else:
            p = st.pop()
            print("Unmatching is found at %d for %s" % (p[1], p[0]))

# 主程序只负责最括号的验证
ver()

#-----------------------------

"""
　栈的链式存储
重点代码

思路分析：
1. 基本的实现模型源于　链表
2. 栈顶位置？
"""
# 自定义异常类
class StackError(Exception):
    pass

#节点类
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

#栈操作类
class Lstack:
    def __init__(self):
        #定义栈顶位置属性
        self._top=None

    # 判断栈是否为空
    def is_empty(self):
        return self._top is None

    #入栈
    def push(self,elem):
        self._top=Node(elem,self._top)

    #排栈
    def pop(self):
        if self._top is None:
            raise StackError("stack is empty")
        value=self._top.data
        self._top=self._top.next
        return value

    #查看栈顶值
    def top(self):
        if self._top is None:
            raise StackError("stack is empty")
        return self._top.data

if __name__=="__main__":
    ls=Lstack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    print(ls.top())#30
    ls.pop()
    print(ls.top())#30 20

# 练习:基于链式栈,完成一个逆波兰表达式的借口程序
ls = Lstack()
while True:
    exp = input()
    tmp = exp.split(" ")
    for i in tmp:
        if i not in ["+", "-", "p"]:
            ls.push(float(i))  # 入栈数字
        elif i == "+":
            x = ls.pop()
            y = ls.pop()
            ls.push(y + x)
        elif i == "-":
            x = ls.pop()
            y = ls.pop()
            ls.push(y - x)
        elif i == "p":
            print(ls.pop())  # 查找栈顶元素

''''''
'''
队列的顺序存储
重点代码
思路分析:1.基于列表完成存储结构
        2.通过封装规定对头和队尾操作
'''
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

"""
链式队列
重点代码
思路分析:1.基于链表模型完成链式栈
        2.链表开端作为队头,尾端作为队尾
        3. 头尾指向同一个节点时作为空队列
"""
#自定义队列异常
class QueueError(Exception):
    pass

#节点类
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

#链式队列类
class Lqueue:
    def __init__(self):
        #初始头尾指向一个没有意义的节点
        self.front = self.rear = Node(None)

    def is_empty(self, elem):
        return self.front == self.rear

    #入队(尾动)
    def enqueue(self,elem):
        self.rear.next=Node(elem)
        self.rear=self.rear.next

    #出队(头动)
    def dequeue(self):
        if self.front==self.rear:
            raise QueueError("Queue is empty")
        self.front=self.front.next
        return self.front.data

if __name__=="__main__":
    lq=Lqueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())#10