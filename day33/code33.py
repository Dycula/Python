"""
开源数据库和非开源数据库
开源:MySQL、SQLite、MongoDB
非开源:Oracle、DB2、SQL_Server
"""
"""

常见的关系型数据库
MySQL、Oracle、SQL_Server、DB2 SQLite
认识关系型数据库和MySQL

1. 数据库结构 (图库结构)
数据元素 --> 记录 -->数据表 --> 数据库
数据表 : 存放数据的表格
字段: 每个列,用来表示该列数据的含义
记录: 每个行,表示一组完整的数据

1.查看已有库
show databases;

2.创建库(指定字符集)
create database 库名 [character set utf8];

创建stu数据库,编码为utf8
create database stu character set utf8;
create database stu charset=utf8;

3.查看创建库的语句(字符集)
show create database 库名;

查看stu创建方法
show create database stu;

4.查看当前所在库
select database();

5.切换库
use 库名;

使用stu数据库
use stu;

6.删除库
drop database 库名;

客户端连接
命令格式
mysql -h主机地址 -u用户名 -p密码
mysql -hlocalhost -uroot -p123456

关闭连接
ctrl-D
exit

SQL语句使用特点
SQL语言基本上独立于数据库本身
各种不同的数据库对SQL语言的支持与标准存在着细微的不同
每条命令必须以 ; 结尾
SQL命令关键字不区分字母大小写
数字类型:
整数类型(精确值) - INTEGER,INT,SMALLINT,TINYINT,MEDIUMINT,BIGINT
定点类型(精确值) - DECIMAL
浮点类型(近似值) - FLOAT,DOUBLE
比特值类型 - BIT
对于精度比较高的东西,比如money,用decimal类型提高精度减少误差。列的声明语法是
DECIMAL(M,D)。
M是数字的最大位数(精度)。其范围为1~65,M 的默认值是10。
D是小数点右侧数字的数目(标度)。其范围是0~30,但不得超过M。
比如 DECIMAL(6,2)最多存6位数字,小数点后占2位,取值范围-9999.99到9999.99。
比特值类型指0,1值表达2种情况,如真,假

字符串类型:
CHAR和VARCHAR类型
BINARY和VARBINARY类型
BLOB和TEXT类型
ENUM类型和SET类型
char:定长,效率高,一般用于固定长度的表单提交数据存储,默认1字符
varchar:不定长,效率偏低

text用来存储非二进制文本
blob用来存储二进制字节串

enum用来存储给出的一个值
set用来存储给出的值中一个或多个值

创建表(指定字符集)
create table 表名(字段名 数据类型,字段名 数据类型,...字段名 数据类型);
如果你想设置数字为无符号则加上 unsigned
如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL, 在操作数据库时如果输入该字段的数据为NULL ,就会报错。
DEFAULT 表示设置一个字段的默认值
AUTO_INCREMENT定义列为自增的属性,一般用于主键,数值会自动加1
PRIMARY KEY关键字用于定义列为主键。主键的值不能重复

#create table student (id int primary key auto_increment,name varchar(32) not null,age int unsigned not null,sex enum('w','m'),socre float default 0.0);
#create table interest (id int primary key auto_increment,name varchar(32) not null,hobby set("sing","dance","draw"),course char,price decimal(6,2),commet text);
#练习：创建表
#1.创建一个游戏人物
#要求包含:名称　职业　技能　皮肤数量　攻击力
#create table game(id int primary key auto_increment,name varchar(32) not null,profession set("战士","法师"),skill set("旋风斩","眩晕"),skin int unsigned not null,attack float default 0.0);
#2.创建一个　购买衣服　分类表
#要求包含:衣服类型　价格　颜色　喜爱程度
#create table 人物 (名称 varchar(128),职业 enum("法师","射手"," 战士"),核心技能 varchar(32),皮肤数量 int,攻击力 float);
#create table student (id int primary key auto_increment,name varchar(32) not null,age int unsigned not null,sex enum('w','m'),socre float default 0.0);
#create table class (name varchar(32) not null,sex enum("w","m"),age int unsigned not null,socre float default 0.0);

查看数据表   show tables;
查看已有表的字符集   show create table 表名;
查看表结构      desc 表名;
删除表    drop table 表名;
插入(insert)
insert into 表名 values(值1),(值2),...;
insert into 表名(字段1,...) values(值1),...;
查询(select)
select * from 表名 [where 条件];
select 字段1,字段名2 from 表名 [where 条件];
更新表记录(update)
update 表名 set 字段1=值1,字段2=值2,... where 条件;
删除表记录(delete)
delete from 表名 where 条件;
注意:delete语句后如果不加where条件,所有记录全部清空

表字段的操作(alter)
语法 :alter table 表名 执行动作;
* 添加字段(add)
alter table 表名 add 字段名 数据类型;
alter table 表名 add 字段名 数据类型 first;
alter table 表名 add 字段名 数据类型 after 字段名;

* 删除字段(drop)
alter table 表名 drop 字段名;

* 修改数据类型(modify)
alter table 表名 modify 字段名 新数据类型;

* 修改字段名(change)
alter table 表名 change 旧字段名 新字段名 新数据类型;

* 表重命名(rename)
alter table 表名 rename 新表名;

时间格式
date :"YYYY-MM-DD"
time :"HH:MM:SS"
datetime :"YYYY-MM-DD HH:MM:SS"
timestamp :"YYYY-MM-DD HH:MM:SS"
注意
1、datetime :不给值默认返回NULL值
2、timestamp :不给值默认返回系统当前时间
日期时间函数
now() 返回服务器当前时间
curdate() 返回当前日期
curtime() 返回当前时间
date(date) 返回指定时间的日期
time(date) 返回指定时间的时间
日期时间运算
语法格式
select * from 表名 where 字段名 运算符 (时间-interval 时间间隔单位);
时间间隔单位: 1 day | 2 hour | 1 minute | 2 year | 3 month
select * from timelog where shijian > (now()-interval 1 day);
模糊查询和正则查询
LIKE用于在where子句中进行模糊查询,SQL LIKE 子句中使用百分号 %字符来表示任意字符。
使用 LIKE 子句从数据表中读取数据的通用语法:
SELECT field1, field2,...fieldN
FROM table_name
WHERE field1 LIKE condition1
e.g.
mysql> select * from class_1 where name like 'A%';
mysql中对正则表达式的支持有限,只支持部分正则元字符
SELECT field1, field2,...fieldN
FROM table_name
WHERE field1 REGEXP condition1
e.g.
select * from class_1 where name regexp 'B.+';
排序
ORDER BY 子句来设定你想按哪个字段哪种方式来进行排序,再返回搜索结果。
使用 ORDER BY 子句将查询数据排序后再返回数据:
SELECT field1, field2,...fieldN from table_name1 where field1
ORDER BY field1 [ASC [DESC]]
默认情况ASC表示升序,DESC表示降序
select * from class_1 where sex='m' order by age;
分页
LIMIT 子句用于限制由 SELECT 语句返回的数据数量 或者 UPDATE,DELETE语句的操作数量
带有 LIMIT 子句的 SELECT 语句的基本语法如下:
SELECT column1, column2, columnN
FROM table_name
WHERE field
LIMIT [num]
联合查询
UNION 操作符用于连接两个以上的 SELECT 语句的结果组合到一个结果集合中。多个 SELECT 语句
会删除重复的数据。
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION [ALL | DISTINCT]
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];
select * from class_1 where sex='m' UNION ALL select * from class_1 where age > 9;
多表查询
多个表数据可以联合查询,语法格式如下
select
字段1,字段2... from 表1,表2... [where 条件]

数据备份
1. 备份命令格式
mysqldump -u用户名 -p 源库名 > ~/***.sql
--all-databases 备份所有库
库名 备份单个库
-B 库1 库2 库3 备份多个库
库名 表1 表2 表3 备份指定库的多张表

例如：现有两个库school1和school2,
要求将两个库中所有内容备份为school.sql并存放在用户主目录下
mysqldump –uroot –p –B school1 school2 > ~/school.sql 
lm
2. 恢复命令格式
mysql -uroot -p 目标库名 < ***.sql
从所有库备份中恢复某一个库(--one-database)
mysql -uroot -p --one-database 目标库名 < all.sql

例如：现有两个库school1和school2，要求将两个库中所有内容备份为school.sql并存放在用户主目录下，
现school1中所有表不小心被删除了，如何从school.sql中恢复school1中所有的表
mysql –uroot –p -–one-database school1 < school.sql 

pymysql使用流程
1. 建立数据库连接(db = pymysql.connect(...))
2. 创建游标对象(c = db.cursor())
3. 游标方法: c.execute("insert ....")
4. 提交到数据库 : db.commit()
5. 关闭游标对象 :c.close()
6. 断开数据库连接 :db.close()

常用函数
db = pymysql.connect(参数列表)
host :主机地址,本地 localhost
port :端口号,默认3306
user :用户名
password :密码
database :库
charset :编码方式,推荐使用 utf8

数据库连接对象(db)的方法
db.commit() 提交到数据库执行
db.rollback() 回滚
cur = db.cursor() 返回游标对象,用于执行具体SQL命令
db.close() 关闭连接

游标对象(cur)的方法
cur.execute(sql命令,[列表]) 执行SQL命令
cur.close() 关闭游标对象
cur.fetchone() 获取查询结果集的第一条数据 (1,100001,"河北省")
cur.fetchmany(n) 获取n条 ((记录1),(记录2))
cur.fetchall() 获取所有记录
"""
# pymysql操作数据库基本流程
import pymysql

# 连接套接字
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

# 获取游标(用于进行数据操作的对象,承载操作结果)
cur = db.cursor()

# 执行sql语句
sql = "insert into student (name,age,sex,socre) values('Lily',14,'w',89);"
cur.execute(sql)
db.commit()  # 将写操作提交到数据库

# 关闭数据库
cur.close()
db.close()

#mysql数据库写操作练习   * 增删改为写操作
import pymysql

# 连接套接字
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")

# 获取游标(用于进行数据操作的对象,承载操作结果)
cur = db.cursor()

# 执行sql语句
try:
    """
    name=input("name:")
    age=int(input("age:"))
    sex=input("sex:")
    socre=float(input("socre:"))
    #sql="insert into student (name,age,sex,socre) values('%s',%d,'%s',%f)"%(name,age,sex,socre);
    #sql="insert into interest values(4,'Jery','draw','B',5999,'表现优秀')"
    #cur.execute(sql)
    ##sql = "insert into student (name,age,sex,socre) values(%s,%s,%s,%s)"
    ##cur.execute(sql,[name,age,sex,socre])"""
    """
    #修改操作
    sql="update student set age=22 where name='Dysion';"
    cur.execute(sql)"""

    # 删除操作
    sql = "delete from student where name='Lily';"
    cur.execute(sql)
    db.commit()  # 可以执行多个sql语句一同提交
except Exception as e:
    db.rollback()  # 退回到commit之前的状态
    print(e)

# 关闭数据库
cur.close()
db.close()



