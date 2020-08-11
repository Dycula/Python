# 练习:一段文字,在文字中可能存在括号配对错误的情况,
# 要求:写一段代码来检测这段文字中有没有括号书写错误.括号包含:{} []()
from day21.code21 import Sstack

text = "hjo{lfspj(fpouji9ogpfhjog)vh[jn]aosdihgv)aolp}ihnldnmlskn"
parens = "{} [] ()"  # 需要验证的字符
left_parens = "{ [ ("
opposite = {"}": "{", "]": "[", ")": "("}  # 验证配对是否正确
st = Sstack()  # 初始化一个类

# 负责提供遍历的括号
def parent(text):
    """
    #遍历字符串,提供括号字符和其位置
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


"""
# 练习:基于链式栈,完成一个逆波兰表达式的借口程序
from day21.code21 import Lstack

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
            print(ls.pop())  # 查找栈顶元素"""

#day21
#1.编写一个函数,传入一个整数,返回该整数的阶乘.
#2.将线性结构的代码整理总结(类似操作和存储差别)

def multiply(n):
    number=1
    for i in range(1,n+1):
        number*=i
    return number
print(multiply(6))
"""
day21
栈的模型
逻辑结构:线性结构
存储结构:顺序存储,链式存储

队列模型:先进先出
逻辑结构:线性结构
存储结构:顺序存储,链式存储

树:一对多模型
二叉树:最多有俩个分支
"""