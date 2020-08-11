"""
MongoDB（芒果）
""""""
一、基础概念
1.数据：能够输入到计算机中并被识别处理的信息集合
2.数据结构:研究一个数据集合中,数据之间关系的学科
3.数据库：按照数据结构,存储管理数据的仓库.
数据仓库是在数据库管理系统管理控制下在一定介质中构建的
4.数据管理系统：数据库管理软件,用于维护建立数据库
5.数据库系统：是数据库和数据库管理系统等开发工具的聚合


二、关系型数据库和非关系型数据库
关系型数据库：采用关系模型(二维表)来组织数据结构的数据库
常用关系型数据库：Oracle 　DB2 　SQLServer 　Mysql 　SQLite
优点：(1)逻辑清晰,容易理解,结构类似常见的表格
　　　(2)使用sql语句操作,技术成熟,使用方便
     (3)数据一致性高
     (4)关系型数据库比较成熟,复杂的数据操作较多
缺点：(1)每次操作需要专门sql语句解析,降低了速度
     (2)关系型数据库内部往往进行加锁处理,也影响了处理速度
     (3)不能很好的处理海量数据并发请求的需要,读写能力差
非关系型数据库(Nosql--->Not only sql)
常见非关系型数据库
(1)键值型数据库：Redis
(2)列存储数据库：HBase
(3)文档型数据库：MongoDB  CouchDB
(4)图形数据库:Graph
优点：(1)读写速度快,可以更好应对并发方案
     (2)使用灵活,容易扩展
缺点:(1)没有sql那样统一的成熟的语句操作
    (2)技术成熟度较差,缺少复杂的数据操作
应用场景：(1)对数据的格式要求比较灵活
        (2)对数据处理速度特别是并发情况下处理速度读要求较高
        (3)某些特定场景：做缓存等
MongoDB数据库
特点：(1)非关系型数据库,是文档型数据库
　　　(2)开源数据库,使用广泛,更新较快
　　　(3)由C++编写的数据库管理系统
　　　(4)支持丰富的存储类型和数据操作
　　　(5)方便扩展,部署,众多 语言提供了操作接口


三、MongoDB的安装
(1)Linux:sudo apt-get install mongodb
(2)Mac os :brew install  mongodb
(3)windows:www.mongodb.com  下载软件安装
Linux安装目录
　安装位置：/var/lib/mongodb...
  配置文件:/etc/mongodb.conf
  命令集：/usr/bin
cookie:
    环境变量:系统指定的查找路径.当加载一个文件时如果当前目录找不到会自动从环境变量目录查找
(4)MOngoDB命令
[1]Mongod  配置的mongodb的基本信息
mongodb 的默认端口好为27017
命令：
mongod -h查看帮助信息
mongod --port [port] 设置端口号
mongod --dbpath   [dir]设置数据库存储路径
[2]mongo  进入数据库mongoshell界面
shell  保护内核　shell>bash
quit()   ctrl+c   退出界面


四、Mongodb数据库数据结构
1.数据组织结构:键值对-->文档-->集合-->数据库
    id      name      age
    1       Lily      18
    2       Lucy      20
{"_id":1,"name":"Lily","age":18},{"_id":2,"name":"Lucy","age":20},
2.概念对比
Mysql       Mongodb        含义
database    database       数据库
table       collection     表/集合
culumn      field          字段/域
row         document       记录/文档
index       index          索引


五、数据库的操作
1.创建数据库:use [database]
例如：创建一个stu数据库
    use stu
    **use实际是选择使用哪个数据库,当这个数据库不存在时则自动建立
    **use创建数据库并不会立即创建,而是当真正插入数据时才会建立
2.查看数据库：show dbs
3.数据库命名规则
    *使用utf-8字符串
    *不能含有空格　.  /  \  '\0'字符
    *不能超过64字节
    *不要和系统数据库重名
4.全局变量db:代表当前正在使用的数据库
    *不选择任何数据库时　db=test
5.删除数据库：db.dropDatabase()
6.数据库的备份和恢复
[1]数据库备份命令
mongodump -h [host] -d [database] -o [path]
例如：备份当前主机中stu数据库到bak目录下 
mongodump -h localhost -d stu -o ./bak
[2]数据库的恢复
mongorestore -h [host:port] -d [db] [bak_dir]
例如：将stu数据库恢复到当前主机中student数据库下
mongorestore -h 127.0.0.1:27017 -d student bak/stu
7.数据库监控
[1]查看数据库的运行状态:mongostat
insert query update delete:每秒增删改查的次数
command:每秒mongo命令的执行次数
flushes:每秒的磁盘刷新频率
vsize  res:
time:时间
[2]监控数据库中数据的读写情况：mongotop
ns:数据集合
total:每秒读写时长
read:每秒读时长
write:每秒写时长


六、集合操作
[1]创建集合
db.createCollection(collectionName)
例如：创建名为class1的集合
db.createCollection("class1")
[2]插入数据库时,如果指定集合不存在会自动创建
db.collection.insert(...)
例如：如果class不存在则自动创建
db.class2.insert({"name":"Lily","age":18})
[3]查看数据库中集合:show collections
        show tables
[4]集合命名规则
    *使用utf-8字符
    *不能含有"\0"字符
    *不能以system.开头(这是系统集合默认开头)
    *不要和关键字重名
[5]删除集合：db.collection.drop()
例如:删除class集合
db.class.drop()
[6]集合重命名
db.collection.renameCollection(newName)
例如：将class重命名为class1
db.class.renameCollection("class1")


七、文档
1.什么是文档?
*文档是mongodb数据库中基本的数据组织单元
*文档有多个键值对构成,每个键值对表达一个数据项
*mongodb中文档数据实际为bson数据格式
2.文档键值对
特点：[1]文档中键值对是无序的
     [2]文档中的键不能重复
     [3]文档通过键取值
     [4]文档的键为utf-8格式,不能有"\0"
键:表示文档的数据域,即数据的信息含义
值：即数据库中存储的数据
数据类型支持：
String      字符串
Int         整型
Double      浮点型
Boolean     布尔型　true false
ObjectId    Id对象
*在插入数据时,如果不自己指定_id域则会自动添加这个域,
值为ObjectId数据,用于作为文档主键
3.集合中的文档设计
[1]一个集合中的文档尽量表达相同的数据内容
[2]集合中文档的层次嵌套不宜过多,如果层次过多时可以考虑可否分为多个集合
[3]集合中文档相互独立,可以根据实际情况选择不同的域结构
八、数据的基本操作
1.插入文档
[1]插入单个文档
命令:db.collection.insertOne(doc);
例如：向class中插入一个文档
db.class.insertOne({"name":"Lily","age":18});
*数据操作时,键可以不加引号,默认为UTF-8字符串
*可以自己添加_id域,但是_id域的值不能重复
[2]插入多个文档
db.collection.insertMany([doc, ....])
例如：向class插入多个文档
db.class.insertMany({"name":"Lily","age":18},{"name":"Lucy","age":20})
[3]一个综合函数
命令：db.collection.insert()
说明:综合insertOne和insertMany功能,官方不推荐
[4]save保存文档
命令:db.collection.save()
说明:使用方法同insert(),但是_id重复时会覆盖原有文档
补充:获取集合对象方法:db.getCollection(collectionName)
"""