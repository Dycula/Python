"""
复习:复习关系型数据库和非关系型数据库
1. 关系型数据库和非关系型数据库对比

  * Nosql不是关系模型构建的数据库，不保证数据一致性，结构灵活

  * Nosql弥补了关系型数据库在处理高并发数据请求时读写速度慢的缺点

  * Nosql种类多样，技术成熟度不如关系型数据库，没有统一的操作语句，发展速度较快

2. MongoDB数据库特点，安装，命令设置

3. MongoDB的组成结构

4. 创建数据库

   * use  database  创建数据库
   * db.dropDatabase()  删除数据库
   * show dbs  查看数据库

   数据库命令： mongodump 备份
   		mongorestore  恢复
		mongostat  数据库监控
		mongotop   监控读写时长

5. 集合操作

   db.createCollecion()  创建集合
   db.collection.insert()  集合不存在自动创建
   db.collection.drop()  删除集合
   db.collection.renameCollection()   重命名
   db.getCollection()  获取集合对象
   show  collections  查看集合

6. 文档

   * bson数据类型
   * 键必须为字符串

7. 插入文档

   insertOne()  插入单个文档
   insertMany()  插入多条文档
   insert()  可以插入一条或者多条文档
   save()  当_id冲突时可以修改原文档

"""
"""
一、查找操作
命令：db.collection.find(query,field)
功能：查找所有符合条件的文档,参数为空表示查找集合所有内容
参数：query　　表示查找条件,是一个键值对文档
    　field　　表示要查找(展示)的域　０表示不该展示的域　１表示该展示的域
返回：返回所有符合要求查找的文档
[1]query ： 通过键值对表示条件关系 
    例如： {age:17} ==>  age=17
[2]field:选择要展示的域
1.以键值对的形式给每个域赋值为0,1表示是否要显示的域
2.如果给域设置为0,则其他域自动为1,如果给某个域设置为1,则其他自动为0,俩者不能混用
3._id比较特殊,默认为1,如果不想显示则设置为0,_id为0时其他的是可以为1的
例如：查找所有年龄17的name age域
    db.class0.find({age:17},{_id:0,name:1,age:1})
db.collection.findOne(query,field)
功能:查找第一个符合条件的文档
参数:同find
返回:返回查找的文档
例如:查找第一个性别为男的文档
db.class0.findOne({sex:"m"},{_id:0})
二、query操作符
操作符:mongodb中使用$符号注明的一个有特殊意义的字符串,用以表达丰富的含义

(1)比较操作符
[1]$eq  等于  =
例如:年龄等于18
db.class0.find({age:{$eq:18}},{_id:0})
[2]$lt  小于　<
例如：字符串可以比较大小
db.class0.find({name:{$lt:"Lily"}},{_id:0})
[3]$gt  大于　>
例如：查找一个区间范围
db.class0.find({age:{$gt:17,$lt:20}},{_id:0})
[4]$lte  小于等于  <=
[5]$gte  大于等于　>=
[6]$ne   不等于　　!=
*如果某个文档没有age这个域也会显示为不等于
[7]$in   包含
例如：查找年终在数组范围的
db.class0.find({age:{$in:[17,19,30]}},{_id:0})
[8]$nin   不包含
例如：查找年终不在数组范围的
db.class0.find({age:{$nin:[17,19,30]}},{_id:0})

(2)逻辑操作符
[1]$and   逻辑与
例如：查找年龄小于20并且为女的
db.class0.find({$and:[{age:{$lt:20}},{sex:"w"}]},{_id:0})
[2]$or    逻辑或
例如：查找年龄大于18或为女的
db.class0.find({$or:[{age:{$gt:18}},{sex:"w"}]},{_id:0})
[3]$not 　逻辑非
例如：查找年龄不大于18
db.class0.find({age:{$not:{$gt:18}}},{_id:0})
[4]$nor   逻辑异或（既不也不）
例如：查找年龄不大于18也不为男的
db.class0.find({$nor:[{age:{$gt:18}},{sex:"m"}]},{_id:0}))
[5]混合条件语句
例如：年龄大于等于20或者小于18并且为男的
db.class0.find({$and:[$or:[{age:{$gte:20}},{age:{$lt:18}}]},{sex:"m"}]},{_id:0})

(3)数组操作符
数组 ： 一组数据的有序集合,用[]表示  
	   * 有序性
	   * 数组中数据类型可以混合
[1]查找数组中包含元素(某一项)
例如：查找数组中元素包含大于89的文档
db.class0.find({score:{$gt:89}},{_id:0})
例如：查找数组中第一项大于90
db.class0.find({'score.0':{$gt:90}},{_id:0})
* 通过序列号表示数组某一项时必须加引号
[2]$all 查找数组中包含多项的文档
例如：查找数组中包含87,89的文档
db.class0.find({score:{$all:[87,89]}},{_id:0})
[3]$size 根据数组元素的个数查找
例如：查找数组中包含3个元素的文档
db.class0.find({score:{$size:3}},{_id:0})
[4]$slice用于field参数,表示查找数组哪些项
例如:查找数组中的前俩项
db.class0.find({},{_id:0,score:{$slice:2}})
例如:跳过数组第一项,查找数组中的后面俩项
db.class0.find({}),{_id:0,score:{$slice:[1,2]}})
[5]$exists 判断一个域是否存在
例如：查找有sex域的文档
db.class0.find({sex:{$exists:true}},{_id:0})
[6]$mod通过整除余数筛选
例如：查找age除以2余数为1的文档
db.class0.find({age:{$mod:[2,1]}},{_id:0})
[7]$type 根据数据类型筛选
例如：查找age域值为字符串类型的
db.class0.find({age:{$type:2}},{_id:0})
*数据类型与数字对应查看type表
[8]通过数组索引进行查找
例如：查找数组第二项大于80的文档
db.class0.find({"score.1":{$gt:80}},{_id:0])
*通过score.1表示第二项,需要加引号表达其他操作
三、数据操作函数
(1)distinct()
功能：查看一个集合中某个域的值锁覆盖的范围
例如：查看class0集合中文档age域都包含那些值
    db.class0.distinct("age")
(2)pretty()
功能:将find查询结果格式化显示
    db.class0.find({}).pretty()
(3)limit(n)
功能：查询结果显示前n个文档
例如：显示查询结果的前三条文档
    db.class0.find({},{_id:0}).limit(3)
(4)skip(n)
功能：对查询结果跳过前n条进行显示
例如：跳过前2条进行显示
    db.class0.find({},{_id:0}).skip(2)
(5)count()
功能：对查询结果进行计数统计
例如：统计age为22的文档个数
    db.class0.find({age:22},{_id:0}).count()
(6)sort()
功能：按照指定的字段进行排序
参数：键值对某个域按照升序排序则值为1,降序排序则值-1
例如：查询结果按照age降序进行排序
    db.class0.find({age:{$type:1}},{_id:0}).sort({age:-1})
复合排序(第一排序项相同时按照第二项排序)
    db.class0.find({age:{$type:1}},{_id:0}).sort({age:-1,name:1})
[7]函数的连续调用获取更丰富结果 
例如：查找年龄最大的三位同学
     db.class0.find().sort({age:-1}).limit(3)
[8]通过序列号直接获取查找结果某一项	
例如：获取第二个男生文档
     db.class0.find({sex:'m'},{_id:0})[1]
[9]删除文档
db.collection.remove(query.justOne)
功能：删除文档
参数：query  定位要删除的文档数据 　类似于sql where子句用法的查找相同
    　justOne  bool值　默认为false,删除所有符合条件的文档

四、修改操作
[1]db.collection.updateOne(query,update,upsert,multi)
功能：修改第一个符合条件的文档
参数：query      筛选条件　同find
     update     要修改的数据,需要同时修改操作符使用
     upsert　   bool值,默认为false,如果query没有筛选到文档不插入新的文档
                upsert=true,如果query没有筛选到文档则插入新的文档
     multi      bool值,默认为false,表示默认只修改一个文档,
                multi=true,表示修改所有符合条件的文档
例如：修改所有年龄20的为年龄21
	db.class0.update({age:20},{$set:{age:21}},false,true)
例如： 将dail年龄修改为16 
	 db.class0.updateOne({name:'Dail'},{$set:{age:16}})
例如： 如果没有找到Alex则插入新的文档
	 db.class0.updateOne({name:'Alex'},{$set:{age:19}},{upsert:true})
[2]updateMany(query,update,upsert)
功能：修改所有符合条件的文档
参数：用法同updateOne
例如：修改所有不存在sex域年龄为20
	db.class0.updateMany({sex:{$exists:false}},{$set:{age:20}}) 
[3]db.collection.findOneAndUpdate(query,update)
功能: 查找第一个复合条件文档，并修改
参数：query  查找条件
	 update  修改内容
返回值：修改前的文档
例如：查找到Jame并修改年龄为20
	db.class0.findOneAndUpdate({name:'Jame'},{$set:{age:20}})
[4]db.collection.findOneAndReplace(query,doc)
功能: 查找一个文档并用新文档替换
参数：query 查找条件
	 doc 替换文档
返回值：返回查找到的文档
例如：查找到第一个文档并替换之
	db.class0.findOneAndReplace({},{name:'Alex',age:19})                  
"""