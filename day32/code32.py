"""
**正则表达式

元字符使用
普通字符
匹配规则:每个普通字符匹配其对应的字符,也可以匹配中文
"""
import re

s = "你好abcdefgfhj你好abafgadgab"
result = re.findall("你好ab", s)
print(result)
# ['你好ab', '你好ab']

"""
或关系
元字符: |
匹配规则: 匹配 | 两侧任意的正则表达式即可
"""
print(re.findall('com|cn', "www.baidu.com/www.tmooc.cn"))
# ['com', 'cn']
print(re.findall("张三|李四", "张三 李四　王五"))
# ['张三', '李四']
"""
匹配单个字符
元字符: .
匹配规则:匹配除换行外的任意一个字符
"""
print(re.findall("张.f","张三f　张四f　张五f"))
#['张三f', '张四f', '张五f']
"""
匹配字符集
元字符: [字符集]
匹配规则: 匹配字符集中的任意一个字符
表达形式:
[abc#!好] 表示 [] 中的任意一个字符
[0-9],[a-z],[A-Z] 表示区间内的任意一个字符
[_#?0-9a-z] 混合书写,一般区间表达写在后面
"""
print(re.findall("[aieou]","how are you"))
#['o', 'a', 'e', 'o', 'u']
print(re.findall("[0-9]","12saf67ggaga35hgfh81"))
#['1', '2', '6', '7', '3', '5', '8', '1']

"""
匹配字符集反集
元字符:[^字符集]
匹配规则:匹配除了字符集以外的任意一个字符
"""
print(re.findall('[^0-9]',"Use 007 port"))
#['U', 's', 'e', ' ', ' ', 'p', 'o', 'r', 't']
"""
匹配字符串开始位置
元字符: ^
匹配规则:匹配目标字符串的开头位置
"""
print(re.findall('^Jame',"Jame,hello Jame"))
#['Jame']
"""
匹配字符串的结束位置
元字符: $
匹配规则: 匹配目标字符串的结尾位置
"""
print(re.findall('Jame$',"Hi,Jame"))
#['Jame']
"""
匹配字符重复
元字符: *
匹配规则:匹配前面的字符出现0次或多次
"""
print(re.findall('wo*',"wooooo~~w!"))
#['wooooo', 'w']
"""
元字符:+
匹配规则: 匹配前面的字符出现1次或多次
"""
print(re.findall('[A-Z][a-z]+',"Hello World"))
#['Hello', 'World']
"""
元字符:?
匹配规则: 匹配前面的字符出现0次或1次
"""
print(re.findall('-?[0-9]+',"Jame,age:18, -26,-gh"))
#[28]: ['18', '-26']

"""
元字符:{n}
匹配规则: 匹配前面的字符出现n次
"""
#匹配手机号码
print(re.findall('1[0-9]{10}',"Jame:13886495728"))
#['13886495728']
"""
元字符:{m,n}
匹配规则: 匹配前面的字符出现m-n次
"""
#匹配qq号
print(re.findall('[1-9][0-9]{5,10}',"Baron:1259296994"))
#['1259296994']
"""
匹配任意(非)数字字符
元字符: \d \D
匹配规则:\d 匹配任意数字字符,\D 匹配任意非数字字符
"""
#匹配端口
print(re.findall('\d{1,5}',"Mysql: 3306, http:80"))
#['3306', '80']
print(re.findall('\D+',"Mysql: 3306, http:80"))
#['Mysql: ', ', http:']
"""
匹配任意(非)普通字符
元字符: \w \W
匹配规则: \w 匹配普通字符,\W 匹配非普通字符
说明: 普通字符指数字,字母,下划线,汉字。
"""
print(re.findall('\w+',"server_port = 8888"))
#['server_port', '8888']
"""
匹配任意(非)空字符
元字符: \s \S
匹配规则: \s 匹配空字符,\S 匹配非空字符
说明:空字符指 空格 \r \n \t \v \f 字符
"""
print(re.findall('\w+\s+\w+',"hello world"))
#['hello world']
"""
匹配开头结尾位置
元字符: \A \Z
匹配规则: \A 表示开头位置,\Z 表示结尾位置
匹配(非)单词的边界位置
元字符: \b \B
匹配规则: \b 表示单词边界,\B 表示非单词边界
说明:单词边界指数字字母(汉字)下划线与其他字符的交界位置。
"""
print(re.findall(r'\bis\b',"This is a test."))
#['is']
print(re.findall("-?\d+\.?/?\d*%?","6hjj1.2jhjh1/3dgf10%hgghj-5"))
#['6', '1.2', '1/3', '10%', '-5']
"""
正则表达式的转义
1.如果使用正则表达式匹配特殊字符则需要加 \ 表示转义
2.在编程语言中,常使用原生字符串书写正则表达式避免多重转义的麻烦。
"""
#匹配特殊字符 . 时使用 \. 表示本身含义
print(re.findall('-?\d+\.?\d*',"123,-123,1.23,-1.23"))
#['123', '-123', '1.23', '-1.23']
#python字符串-->正则 --> 目标字符串
#"\\$\\d+"解析为\$\d+   匹配 "$100"
#"\\$\\d+"等同于r"\$\d+"
"""
贪婪模式和非贪婪模式
1. 定义
贪婪模式: 默认情况下,匹配重复的元字符总是尽可能多的向后匹配内容。比如: * + ? {m,n}
非贪婪模式(懒惰模式): 让匹配重复的元字符尽可能少的向后匹配内容。
2. 贪婪模式转换为非贪婪模式
在匹配重复元字符后加 '?' 号即可
"""
print(re.findall("ab*?","ababbb"))
#['a', 'a']
print(re.findall(r"\[.+?\]","hello[a#@de] world[world]"))
#['[a#@de]', '[world]']

"""
正则表达式分组
1. 定义
在正则表达式中,以()建立正则表达式的内部分组,子组是正则表达式的一部分,可以作为内部整
体操作对象。
"""
#可以被作为整体操作,改变元字符的操作对象
print(re.search(r'(ab)+',"ababababab").group())
#ababababab
print(re.search(r'(王|李)\w{1,3}',"王者荣耀").group())
#王者荣耀

"""
捕获组
可以给正则表达式的子组起一个名字,表达该子组的意义。这种有名称的子组即为捕获组。
格式: (?P<name>pattern)
"""
print(re.search(r'(?P<pig>ab)+',"ababababab").group('pig'))
#ab
"""
正则表达式匹配原则
1. 正确性,能够正确的匹配出目标字符串.
2. 排他性,除了目标字符串之外尽可能少的匹配其他内容.
3. 全面性,尽可能考虑到目标字符串的所有情况,不遗漏.
"""

"""
re.findall(pattern,string,flags = 0)
功能:根据正则表达式匹配目标字符串内容
参数:pattern 正则表达式
    string   目标字符串
    flags    功能标志位,扩展正则表达式的匹配
返回值: 匹配到的内容列表,如果正则表达式有子组则只能获取到子组对应的内容

"""
import re
s="Alex:1994,Sunny:1993"
pattern=r"(\w+):\d+"
#re模块调用findall
l=re.findall(pattern,s)
print(l)
#['Alex', 'Sunny']
"""
regex = compile(pattern,flags = 0)
功能: 生产正则表达式对象
参数: pattern 正则表达式
flags 功能标志位,扩展正则表达式的匹配
返回值: 正则表达式对象
"""
#使用compile对象调用
regex=re.compile(pattern)
l=regex.findall(s,0,6)
print(l)#['Alex']
"""
re.split(pattern,string,flags = 0)
功能: 使用正则表达式匹配内容,切割目标字符串
参数: pattern 正则表达式
     string 目标字符串
     flags 功能标志位,扩展正则表达式的匹配
返回值: 切割后的内容列表
"""
#匹配内容切割字符串
a=re.split(r":|,",s)
print(a)
#['Alex', '1994', 'Sunny', '1993']

"""
re.sub(pattern,replace,string,max,flags = 0)
功能: 使用一个字符串替换正则表达式匹配到的内容
参数: pattern 正则表达式
     replace 替换的字符串
     string 目标字符串
     max 最多替换几处,默认替换全部
     flags 功能标志位,扩展正则表达式的匹配
返回值: 替换后的字符串
"""
#替换匹配到的字符串
s=re.sub(r"\s+","#","this is a test",2)
print(s)

"""
re.finditer(pattern,string,flags = 0)
功能: 根据正则表达式匹配目标字符串内容
参数: pattern 正则表达式
     string 目标字符串
     flags 功能标志位,扩展正则表达式的匹配
返回值: 匹配结果的迭代器
"""
s="2019年,建国70年"
pattern=r"\d+"
#返回迭代器
iter=re.finditer(pattern,s)
for i in iter:
    print(i)

"""
re.fullmatch(pattern,string,flags=0)
功能:完全匹配某个目标字符串
参数:pattern 正则
    string 目标字符串
返回值:匹配内容match object
"""
#完全匹配
m=re.fullmatch(r"\w+","Jame1")
print(m)

"""
re.match(pattern,string,flags=0)
功能:匹配某个目标字符串开始位置
参数:pattern 正则
    string 目标字符串
返回值:匹配内容match object
"""
#匹配开始位置
n=re.match(r"[A-Z]\w+","Hello world")
print(n)

"""
re.search(pattern,string,flags=0)
功能:匹配目标字符串第一个符合内容
参数:pattern 正则
    string 目标字符串
返回值:匹配内容match object
"""
#匹配第一处
n=re.search(r"[A-Z]\w+","Hello world")
print(n)


import re
pattern=r"(ab)cd(?P<pig>ef)"
regex=re.compile(pattern)
obj=regex.search("abcdefghi")#math对象
"""
#属性变量
print(obj.pos)#匹配的目标字符串开始位置
print(obj.endpos)#匹配的目标字符串结束位置
print(obj.re)#正则表达式
print(obj.srting)#目标字符串
print(obj.lastgroup)#最后一组的名称
print(obj.lastindex)#最后一组的序号
"""
#属性方法
print(obj.span()) #获取匹配内容的起止位置
print(obj.start()) #获取匹配内容的开始位置
print(obj.end())#获取匹配内容的结束位置
print(obj.groupdict()) #获取捕获组字典,组名为键,对应内容为值
print(obj.groups()) #获取子组对应内容
print(obj.group())#获取match对象匹配内容

"""
flags参数扩展
A == ASCII 元字符只能匹配ascii码
I == IGNORECASE 匹配忽略字母大小写
S == DOTALL 使 . 可以匹配换行
M == MULTILINE 使 ^ $可以匹配每一行的开头结尾位置
X == VERBOSE 为正则添加注释
"""
import re
s="""Hello
北京
"""
#只能匹配ASCII
regex=re.compile(r"\w+",flags=re.A)
l=regex.findall(s)
print(l)#['Hello']
#不区分大小写
regex=re.compile(r"[a-z]+",flags=re.I)
l=regex.findall(s)
print(l)#['Hello']
#让.匹配换行
regex=re.compile(r".+",flags=re.S)
l=regex.findall(s)
print(l)#['Hello\n北京\n']
#^$匹配每行开头结尾
regex=re.compile(r"Hello$",flags=re.M)
l=regex.findall(s)
print(l)#['Hello', '北京']

#使用多个flag
#方法:使用按位或连接
flags = re.I | re.A










