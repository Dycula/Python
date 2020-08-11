"""
复习
1.修改操作
findOneAndUpdate()
findOneAndReplace()
2.修改器的使用
$set   $unset   $rename  $inc  $mul   $setOnInsert
$max   $min
$push   $pushAll  $pull  $pullAll   $pop  $addToSet
$each   $position   $sort
3.删除操作
deleteOne()
deleteMany()
remove()
findOneAndDelete()
4.数据类型
*时间类型
newDate()
Date()
ISODate()
valueOf()
*Null类型 ： null
*Object类型: 外部域.内部域取内部域内容
5.索引操作
创建索引：createIndex()  createIndexes()     ensureIndex()
查看索引: getIndexes()
删除索引：dropIndex()    dropIndexes()
6.聚合操作

聚合函数 ： db.collection.aggregate([])

聚合操作符： $group:  $sum  $avg  $max $min $first  $last
$project
$match
"""
#** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
"""
一.聚合操作（续）

1. $limit   显示集合中前几条文档
e.g.显示前3个文档内容
db.class0.aggregate([{$limit: 3}])

2. $skip    跳过前几个文档显示后面的内容
e.g.跳过前3个文档显示后面内容
db.class0.aggregate([{$skip: 3}, {$project: {_id: 0}}])

3. $sort    对集合文档排序
e.g.对文档按年龄排序
db.class0.aggregate([{$sort: {age: 1}}, {$project: {_id: 0}}])

聚合操作符文档：
https: // docs.mongodb.com / manual / reference / operator / aggregation /

练习 ： 使用grade
1.将所有男生按照年龄升序排序，结果不显示_id
aggregate([{$match: {sex: 'm'}}, {$sort: {age: 1}}, {$project: {_id: 0}}])
2.统计班级中是否存在重名同学
aggregate([{$group: {_id: '$name', num: {$sum: 1}}}, {$match: {num: {$gt: 1}}}])


二.固定集合

定义： 指mongodb中创建的固定大小的集合
特点： 1.淘汰早期数据
      2.可以控制集合大小
      3.数据插入查找速度较快
应用： 日志处理，临时缓存
创建： db.createCollection(collection, {capped: true, size: 1000, max: 20})

capped: true    创建固定集合
size: 1000      表示固定集合大小字节
max ：20         最多存放文档数量

三.文件存储

1.文件存储数据库方式

【1】存储路径：将本地文件所在路径以字符串存储到数据库

优点： 节省数据库空间，方便操作获取
缺点： 当数据库或者文件变动就必须修改数据库内容

【2】存储文件本身：将文件转换为二进制存储到数据库

优点： 文件在数据库中，不易丢失
缺点： 占用数据库空间大，存取效率不高

2.GridFS文件存储方法
目的: 更方便的存取MongoDB中的大文件（ > 16M）

GridFS方案说明：
1.在mongodb数据库中创建两个集合共同存储文件
2.fs.files集合用于存储文件基本信息
3.fs.chunks集合用于建立与fs.files关联，将文件分块以二进制存储

存取方法

1.存储： mongofiles - d  dbname  put file

e.g.将test.jpg存到grid数据库
mongofiles - d  grid  put test.jpg

2.提取： mongofiles - d  dbname  get file

e.g.从grid中提取test图片
mongofiles - d  grid  get  test.jpg

优缺点：
    优点：存储方便，提供了较好的存储命令
    缺点：效率低，不建议存储小文件

四.mongo shell对JavaScript支持

*mongoshell 界面中支持简单的js语句操作
*通过js编程处理数据库中基本的逻辑问题

五.Python操作MongoDB

1.第三方模块： pymongo
安装 ： sudo pip3 install pymongo

2.操作步骤

【1】 创建mongodb数据库连接

conn = pymongo.MongoClient('localhost', 27017)

【2】 生成操作的数据库对象

db = conn.stu
db = conn['stu']

【3】 生成集合对象

myset = db.class0
myset = db['class0']

【4】 集合对象调用接口完成数据库操作

【5】 关闭数据库连接

        db.close()

3.插入文档

insert_one() 插入一条文档

insert_many() 插入多条文档

insert() 插入一条或多条文档

save() 保存文档，当_id冲突时覆盖原有文档

4.查找文档

cursor = find(query，field)
功能: 查找文档
参数：同mongoshell格式
返回值：查找结果的游标对象

操作符使用：在python中所有操作符使用引号作为字符串处理
e.g.  $exists --> '$exists'

数据类型对应： true --> True
             false --> False
             null --> None

cursor对象属性函数：

【1】 next()获取下一个文档
【2】 limit(n)获取前n条文档
【3】 skip(n)跳过前n条文档
【4】 count()统计数量
【5】 sort()排序

*使用for或者next取游标后不能再调用limit  skip  sort
*sort排序将字典改为列表嵌套元组
e.g.{name: 1} -->  [('name', 1)]

find_one(query, field)
功能: 查找一条文档
参数：同find
返回值：字典

3.修改文档

update_one()修改一个文档
update_many()修改多个文档
update()修改一个或多个文档

4.删除文档

delete_one()删除一个文档
delete_many()删除多个文档
remove()删除一个或多个

5.复合操作
find_one_and_update()
find_one_and_delete()

6.索引操作

create_index()
功能：创建索引
参数: 二元元组列表
e.g.[('age', 1)]表示对age创建正序索引
返回值： 索引名称

* 　直接传入域名　如'name'表示[('name', 1)]
*特殊类型索引以关键字传参传入  如唯一索引则添加 unique = True

list_indexes()查看索引

drop_index()删除索引
*参数为索引名称或者索引键值对e.g.[(name, 1)]

drop_indexes()删除所有索引

7.聚合操作

aggregate()
功能: 完成聚合操作
参数：写法同mongoshell中聚合
返回值： 数据操作结果游标对象

练习： 使用class0集合，为集合中的每个文档添加一个域结构如下

score: {'Chinese': 78, 'Math': 95, 'English': 80}

*注意，分数为60 - - 100的随机整数

然后使用聚合完成：打印所有男生成绩按照英语降序排序，不显示_id

六.文件存储

1.bson数据格式模块

import bson

2.存储图片方法

【1】 数据库连接，生成集合对象
【2】 将文件rb方式读取
【3】 将读取内容使用bson格式转换为mongodb存储内容

import bson.binary
content = bson.binary.Binary(data)
功能: 将python bytes数据转换为bson数据格式

【4】 将内容使用insert插入数据库


"""






