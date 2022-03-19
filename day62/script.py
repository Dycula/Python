s="A\nB\tC"
print(len(s))#5，\n相当于换行，\t相当于tab键
print(s)
s="\t"
print(len(s))#1
s="\n"
print(len(s))#1
s="A\0B\0C"
print(len(s))
a='sp\xc4m'
print(a)
a='\xc4'
print(a)

import re
a=re.match('o','hello')
b=re.search('o','hello')
print(a)
print(b)


