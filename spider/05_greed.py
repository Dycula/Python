import re
html='''
<html>
    <div><p>九霄龙吟惊天变</p></div>
    <div><p>风云际会浅水游</p></div>
    <div><p>金鳞岂是池中物</p></div>
    <div><p>一遇风云便化龙</p></div>
</html>
'''

#贪婪模式
pattern=re.compile("<div><p>.*</p></div>",re.S)
r_list=pattern.findall(html)
print(r_list)
#非贪婪模式
pattern1=re.compile("<div><p>.*?</p></div>",re.S)
r_list01=pattern.findall(html)
print(r_list01)


s = 'A B C D'
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))
# 分析结果是什么???['A B', 'C D']

p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))
# 分析结果是什么???['A', 'C']

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))
# 分析结果是什么???[('A', 'B'), ('C', 'D')]