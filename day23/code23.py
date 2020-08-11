"""
字节串(bytes)
在python3中引入了字节串的概念,与str不同,字节串以字节序列值表达数据,更方便用来处理二进程
数据.因此在python3中字节串是常见的二进制数据展现方式.
普通的ascii编码字符串可以在前面加b转换为字节串,例如: b'hello'
字符串转换为字节串方法: str.encode()
字节串转换为字符串方法: bytes.decode()
"""
str="hello"
str.encode()#b'hello'

bytes=b'hello'
bytes.decode()#'hello'

"""
文件读取演示
1. 读取文件

read([size])
功能:用来直接读取文件中字符。
参数:如果没有给定size参数(默认值为-1)或者size值为负,文件将被读取直至末尾,给定size
最多读取给定数目个字符(字节)。
返回值: 返回读取到的内容
注意:文件过大时候不建议直接读取到文件结尾,读到文件结尾会返回空字符串。

readline([size])
功能:用来读取文件中一行
参数:如果没有给定size参数(默认值为-1)或者size值为负,表示读取一行,给定size表示最多
读取制定的字符(字节)。
返回值:返回读取到的内容

readlines([sizeint])
功能:读取文件中的每一行作为列表中的一项
参数:如果没有给定size参数(默认值为-1)或者size值为负,文件将被读取直至末尾,给定size
表示读取到size字符所在行为止。
返回值:返回读取到的内容列表

文件对象本身也是一个可迭代对象,在for循环中可以迭代文件的每一行。
"""
#打开文件
try:
    fd=open("text","r")
except FileNotFoundError as e:
    print(e)

#read循环读取文件
while True:
    #一次性最多读取1024个字节
    data=fd.read(1024)
    #读到文件结尾得到空字符串,此时跳出循环
    if not data:
        break
    print("读取内容：",data)#读取内容： hello world

#关闭文件
fd.close()

"""
总结:如果文件是文本文件,则打开方式可以为文本方式或者二进制方式.
    如果是文本方式打开,读写都是一字符串方式读取或者写入内容;
    如果以二进制方式打开,读写都是一字节串读取或者写入内容.
    
"""

#readline读取一行内容
fd=open("text","r")
data=fd.readline()
print(data)#hello world
data=fd.readline()
print(data)#hai

#readlines读取所有内容,每行作为列表中的一个元素
fd=open("text","r")
data=fd.readlines()
print(data)#['hello world\n', 'hai']

#每次获取一行
fd=open("text","r")
for line in fd:
    print(line)#hello world       hai

#练习:从终端输入一个单词,打印出单词的解释.如果没有该单词则打印“没有找到该单词”
file=open("dict.txt","r")
word=input("输入一个单词")
for line in file:
    total_word=line.split(" ")[0]
    if total_word>word:
        print("没有找到该单词")#遍历的单词大于目标
        break
    elif total_word==word:
        print(line)
        break
else:
    print("没有找到该单词")
file.close()

"""
写入文件

write(string)
功能:把文本数据或二进制数据块的字符串写入到文件中去
参数:要写入的内容
    如果需要换行要自己在写入内容中添加\n
    
writelines(str_list)
功能:接受一个字符串列表作为参数,将它们写入文件。
参数:要写入的内容列表
"""

#原有的内容被清除
file=open("test","w")
file.write("Good morning\n")

#如果是wb打开要转换成字节串写入
file=open("test","wb")
file.write("hello".encode())

file=open("test","w")
file.writelines(["abc\n","def\n"])

"""
with操作
python中的with语句使用于对资源进行访问的场合,保证不管处理过程中是否发生错误或者异常都会执
行规定的“清理”操作,释放被访问的资源,比如有文件读写后自动关闭、线程中锁的自动获取和释放
等。
"""
with open("test") as f:
    #生成f文件对象
    data=f.read()
    print(data)
# with 语句块结束　ｆ自动销毁
"""
缓冲区
flush():该函数调用后会进行一次磁盘交互,将缓冲区中的内容写入到磁盘。
"""
f=open("test","w",1)
# 1表示行缓冲
while True:
    s=input(">>")
    f.write(s)
    #flush()将缓冲区内容写入磁盘
    f.close()

"""
文件偏移量

基本操作
tell()　　
功能:获取文件偏移量大小
seek(offset,[whence])　
功能:移动文件偏移量位置
参数:offset 代表相对于某个位置移动的字节数。负数表示向前移动,正数表示向后移动。
whence是基准位置的默认值为 0,代表从文件开头算起,1代表从当前位置算起,2 代表从文件末
尾算起。必须以二进制方式打开文件时基准位置才能是1或者2
"""

"""空洞文件"""
f = open('test','wb')
f.write(b'start')
f.seek(1000,2) # 结尾位置向后移动１０００字节
f.write(b'end')
f.close()

#若是w或者r打开文件则文件偏移量在开头
#若是a打开文件则文件偏移量在结尾
f=open("test","wb+")
f.write(b"hello\n")
f.flush()

print(f.tell())#打印当前文件偏移量
f.seek(10,0)#以开头为基准向后移动10字节

data=f.read()
print(data)

"""
文件描述符
1. 定义:系统中每一个IO操作都会分配一个整数作为编号,该整数即这个IO操作的文件描述符。
2. 获取文件描述符  
fileno():通过IO对象获取对应的文件描述符
"""

"""
文件管理函数

import os
1. 获取文件大小
os.path.getsize(file)

2. 查看文件列表
os.listdir(dir)

3. 查看文件是否存在
os.path.exists(file)

4. 判断文件类型
os.path.isfile(file)

5. 删除文件
os.remove(file)
"""