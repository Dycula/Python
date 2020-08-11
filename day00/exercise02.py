"""
替换空格
请实现一个函数:
将一个字符串中的每个空格替换成“%20”
例如：当字符串为we are happy.则经过替换后的字符串为we%20are%20happy.

理解
如何对字符串进行替换操作
先看看字符串中有哪些常用方法
s.count(s1):计算字符串中s1在s中出现的次数
s.find(s1):返回子字符串s1在s中第一次出现时的索引值,如果s1不在s中,则返回-1
s.rfind(s1):功能与find相同,只是从s的末尾卡死反向搜索(rfind中的r表示反向)
s.index(s1):功能与find相同,只是如果s1不在s中,则抛出一个异常
s.index(s1):功能与index相同,只是从s的末尾开始
s.lower():将s中的所有大写字母转换为小写
s.replace(old,new):将s中出现过的所有字符串old替换为字符串new
s.rstrip():去掉s末尾的空白字符
s.split(d):使用d作为分隔符拆分字符串s,返回s的一个子字符串列表.
"""
#思路1
class Solution1:
    def replaceSpace(self,s):
        #源字符串s
        return s.replace(" ","%20")

#思路2:遍历替换
class Solution2:
    def replaceSpace(self,s):
        #源字符串s
        s_new=""
        for i in s:
            if i==" ":
                i="%20"
            s_new+=1
        return s_new

#方法3:
class Solution3:
    def replaceSpace(self,s):
        #源字符串s
        s=list(s)
        for i in range(len(s)):
            if s[i]==" ":
                s[i]="%20"
        return ".join(s)"
