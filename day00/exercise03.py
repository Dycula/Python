"""
从尾到头打印链表
题目描述：
输入一个链表：按链表值从尾到头的顺序返回一个ArrayList
"""
#链表结构
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None
#思路：读取链表中的每个元素,放入list中,再倒序输出
class Solution:
    def printListFromTailToHead(self,listNode):
        list=[]
        while listNode:
            list.append(listNode.val)
            listNode=listNode.next
        return list[::-1]
"""
什么是链表？
python数据结构（链表）
"""