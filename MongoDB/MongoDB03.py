"""
复习
数据的查找
    find(query,field)
    findOne(query,field)
query 操作符
   比较： $eq  $lt  $gt  $lte  $gte  $ne  $in  $nin
   逻辑： $and  $or   $not   $nor
   数组： $all   $size
   其他： $exists   $mod   $type
数据处理函数
   pretty()  limit()   skip()   sort()   count()  distinct()
数据的删除操作
    remove(query,justOne)
    justOne true
更新数据
    update(query,update,upset,multi)
    upset true
    multi true
"""
"""
修改器：将数据修改为什么
一、数组修改器
[1]$set  修改一个域或增加一个域,同时可以修改多个项
例如：修改Lily sex域为"m",如果没有这个域会自动增添
db.class0.updateOne({sex:{$exist:false}},{$set:{sex:"m"}})
[2]$unset  删除一个域
例如：删除Lily的sex域
db.class0.updateOne({name:"Lily"},{$unset:{sex:""}})
[3]$rename　给域重命名
例如:给sex域重命名为gender
db.class0.updateMany({},{$rename:{sex:"gender"}})
[4]$inc    功能：对某个域的值进行加减修改
例如：给姓名为宝强的文档年龄age增加1(如果值为负数即为减少)
db.class0.update({name:"宝强"},{$inc:{age:1}})
[5]$mul    功能：对某个域的值进行乘法修改
例如：给姓名为宝强的文档年龄age乘以2(也可以是小数)
db.class0.update({name:"宝强"},{$mul:{age:2}})
[6]$min    功能：设定最小值,如果query到的文档指定域值小于min设定值则不做修改
如果query到的文档指定值大于min设定值则修改为min值
例如：如果宝强的年龄小于20则不变,大于20则改为20
db.class0.update({name:"宝强"},{$min:{age:20}})
[7]$max    功能：设定最大值,如果query到的文档指定域值大于max设定值则不做修改
如果query到的文档指定值小于max设定值则修改为max值
例如：将所有年龄不到17的文档修改为17
db.class0.update({},{$max:{age:17}},false,true)
修改器可以一起使用
例如：将阿花年龄增加2,性别修改为w
db.class0.update({name:"阿花"},{$inc:{age:2},$set:{gender:"w"}})
[8]$setOnInsert : 使用update*插入文档时，作为补充内容
例如：如果插入文档tel作为插入内容
	db.class1.updateOne({name:'Lily'},{$set:{age:18},$setOnInsert:{tel:'13855264728'}},{upsert:true})
* 一个update中可以同时使用多个修改器，每个修改器也可以修改多项
* 在一条语句中不能多个修改器同时修改同一个域
[9]$push   功能：向数组中添加一项
db.class0.update({name:"Lily"},{$push:{hobby:"Computer"}})
[10]$pushAll    功能：向数组中增加多项
db.class0.update({name:"Tom"},{$pushAll:{hobby:["Computer","python"]}})
[11]$each       功能：逐一取出其中的值进行操作
db.class0.update({name:"Tom"},{$push:{hobby:{$each:["chui","kan"]}}})
[12]$pull   功能：从数组中删除一个元素
db.class0.update({name:"Tom"},{$pull:{hobby:"chui"}})
[13]$pullAll    功能：从数组中删除多个元素
db.class0.update({name:"Tom"},{$pullAll:{hobby:["chui","gongfu"]}})
[14]$pop    功能：从数组的俩端弹出元素
弹出数组中的最后一项  1
db.class0.update({name:"Jame"},{$pop:{hobby:1}})
弹出数组中的第一项  -1
db.class0.update({name:"Jame"},{$pop:{hobby:-1}})
[15]$addToSet   功能：向数组中添加一个元素,该元素不能和其他元素重复
例如：如果hobby中已有Game则无法添加(但是push是可以的)
db.class0.update({name:"Jame"},{$addToSet:{hobby:"Game"}})
[16]$position: 配合each将元素插入到指定位置
例如：指定在1号位置插入10
    db.class1.updateOne({name:'小亮'},{$push:{score:{$each:[10],$position:1}}})
[17]$sort  对数组排序
例如：对数组按照升序排序
    db.class1.updateOne({name:'小红'},{$push:{score:{$each:[],$sort:1}}})
二. 删除操作

   1. 格式对比 
      
      mysql：delete  from  table  where ...

      mongo: db.collection.deleteOne(query)

   2. 删除函数
      
     【1】 deleteOne(query)
           功能： 删除第一个符合条件的文档
	   参数： 筛选条件

        e.g. 删除Lily
	db.class1.deleteOne({name:'Lily'})
      
     【2】 db.collection.deleteMany(query)

        e.g.  删除所有没有gender域的文档
	db.class0.deleteMany({gender:{$exists:false}})
       
     【3】 db.collection.remove(query,justOne)
	   功能： justOne = false 同deleteMany 
	          justOne = true  同deleteOne

	e.g. 删除第一个年龄为19的文档
	db.class0.remove({age:19},true)
      
     【4】 db.collection.findOneAndDelete(query)
           功能：查找一个文档并删除之
	   参数: 筛选条件
	   返回值：查找到的文档

	e.g. 查找并删除name为小亮的
	db.class1.findOneAndDelete({name:'小亮'})

三. 数据类型

  1. 时间类型

    【1】 获取当前时间方法
          
	  * new Date()  生成当前标准时间

	  e.g. 
	  db.class2.insertOne({book:'Python入门',date:new Date()})

	  * Date()  获取计算机系统时间生成时间字符串

	  e.g.
	  db.class2.insertOne({book:'Python精通',date:Date()})

    【2】 时间函数
          ISODate()
	  功能：将制定时间定义为mongodb标准时间
	  参数：默认表示当前标准时间
	        通过字符串制定时间
		 "2019-01-08 11:11:11"
		 "20190212 11:11:11"
		 "20190101"

          e.g.
	  db.class2.insertOne({book:'Python放弃',date:ISODate("2019-01-13 11:08:36")})

     【3】 获取时间戳

          valueOf()
	  功能： 根据标准时间生成时间戳

	  e.g.
	  db.class2.insertOne({book:'Python疯狂',date:ISODate().valueOf()})

  2. Null类型

    【1】 值： null
    【2】 含义 ： 表示某个域的值为空

          e.g.  price域值为空
	  db.class2.insertOne({book:'Python涅磐',price:null})
	  
        例如：某个域如果没有值却存在则可以设置为null
        db.class0.insert({name:"深圳",country:null})
        
        例如：表示某个域不存在也能够进行匹配
        db.class0.find({country:null})
  3. Object类型

    【1】定义：文档中的域的值为文档，则称为object类型数据

    【2】使用方法：当使用内部文档某个域时需要 "外部域.内部域" 的方法对内部域值进行操作

      e.g.
        db.class3.find({'book.title':'三国演义'},{_id:0})

      e.g.
      db.class3.updateOne({'book.title':'水浒传'},{$set:{'book.price':46.6}})

        文档类型数据
        (1)外部文档的域引用内部文档的域通过.的方法逐层引用
        查找内部文档title值为python　web 的文档
        　 
        数组数据的下标引用
        使用数组的域点引用下标的方式可以表示数组中具体某一项
        db.class0.find({"hobby.0":"song"})

练习： 使用grade
   
   1. 删除所有年龄小于8岁或者大于12岁的同学
      deleteMany({$or:[{age:{$lt:8}},{age:{$gt:12}}]})

   2. 给小红的第二项爱好变为跳舞
      updateOne({name:'小红'},{$set:{'hobby.1':'dance'}})

   3. 删除兴趣爱好中没有画画的同学
      deleteMany({hobby:{$nin:['draw']}})

   4. 给小王增加一个域  
       备注：{民族：'回族'，习俗:'注意饮食文化'}
      
      updateOne({name:'小王'},{$set:{备注：{民族：'回族'，习俗:'注意饮食文化'}}})

   5. 修改小王的备注域，增加一项  宗教:'伊斯兰'
      updateOne({name:'小王'},{$set:{'备注.宗教':'伊斯兰'}})


四. 索引操作  

  1. 什么是索引： 索引是建立文档所在位置的查找清单，使用索引可以方便快速查找，减少遍历次数提高查找效率

  2. 索引约束 
    
    【1】 当数据量很少的时候没有必要建立索引

    【2】 如果对数据操作大多是写操作而不是读操作不需要创建索引
  
  3. 创建索引

    【1】 db.collection.createIndex()
          功能: 创建索引
	  参数：索引域 和 索引选项

          e.g.  为name域创建索引
	  db.class0.createIndex({name:1})
	  
	  * _id域会自动创建索引，且不能删除
	  * 1 表示正向索引，-1表示逆向索引

    【2】 db.collection.getIndexes()
          功能：查看集合中的索引

    【3】 自定义索引名称
           
	  e.g. 为age域创建索引，取名为Age
	  db.class0.createIndex({age:1},{name:'Age'})
     
    【4】 其他创建索引方法

           ensureIndex()
	   功能:创建索引
	   参数：同createIndex()

	   createIndexes([{},{}])
	   功能：同时创建多个索引
	   参数：数组中写索引文档即可

	   e.g.  同时创建多个索引
	   db.class0.createIndexes([{age:-1},{name:-1}])
  
  4. 删除索引
     
     【1】 db.collection.dropIndex()
     	   功能：删除一个索引
	   参数：索引名称或者键值对

	   e.g.
	   db.class0.dropIndex('name_-1')
           
	   e.g.
	   db.class0.dropIndex({age:-1})


     【2】 db.collection.dropIndexes()
           功能：删除集合中所有索引 （除了_id）

   5. 其他类型索引

     【1】 复合索引：根据多个域创建一个索引

         e.g. 根据name和age创建复合索引
	 db.class0.createIndex({name:1,age:-1})

     【2】 子文档/数组索引：如果对某个值为object或者是数组的域创建索引，那么针对object和数组的索引查询都是索引查找

         e.g. 对book域创建索引则该查找也是索引查找
	 db.class3.find({'book.title':'水浒传'},{_id:0})
 
     【3】 唯一索引 ： 要求创建索引的域不能有重复值

         e.g. 对name域创建唯一索引
	  db.class0.createIndex({name:1},{unique:true})
      
     【4】 稀疏索引 ：如果创建索引时某些文档不存在指定域则忽略这些文档

         e.g. 对age创建稀疏索引
	  db.class0.createIndex({age:-1},{sparse:true})


五. 聚合操作

  1. 什么是聚合：对文档进行数据整理统计的操作

  2. 聚合操作函数
     
     db.collection.aggregate()
     功能: 完成聚合操作
     参数：聚合条件，配合聚合操作符完成

  3. 聚合操作符

    【1】 $group  分组聚合  配合一定的统计操作符
        
	* $sum  统计求和

	e.g. 按性别分组求每组人数
	 db.class0.aggregate({$group:{_id:'$gender',num:{$sum:1}}})

	* $avg 求平均数

	e.g. 按性别分组求每组的平均年龄
	db.class0.aggregate({$group:{_id:'$gender',num:{$avg:'$age'}}})

        * $max/$min   求最大值最小值

	e.g. 按性别分组求每组的最大值
	db.class0.aggregate({$group:{_id:'$gender',num:{$max:'$age'}}})
	
        * $first/$last   求第一项值和最后一项值

    【2】 $project   用于数据格式化展示
  
       * project 值的写法类似find函数field参数
       
       e.g. 以指定域名展示数据
       db.class0.aggregate({$project:{_id:0,Name:'$name',Age:'$age'}})

    【3】 $match  数据筛选
     
       * match 值的写法同find函数中query写法
    
       e.g. 筛选年龄大于18的文档
       db.class0.aggregate({$match:{age:{$gt:18}}})

  4. 聚合管道 
     
     定义： 指将第一个聚合的结果交给第二个聚合操作继续执行，直到所有聚合完成。

     形式： aggregate([{聚合1},{聚合2}...])

     e.g. 查找年龄大于18的文档，不显示_id
     db.class0.aggregate([{$match:{age:{$gt:18}}},{$project:{_id:0}}])


作业 ： 1. 通过文档自己学习两个聚合操作符用法 $limit  $sort
    　　2. 续银行：完成修改，删除操作
	　　3. 数量今天的操作符和函数用法

"""
