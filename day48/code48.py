""""
1.数据库
    存储数据的仓库
    mysql,Oracle
2.mysql特点
    1.关系型数据库
    2.跨平台
    3.支持多款编程语言
    4.基于磁盘存储,数据是以文件的形式保存在/var/lib/mysql
3.启动链接
1.sudo/etc/initd/mysql  start|stop|restart|status
2.sudo service mysql  start|stop|restart|status
客户端链接:Navicat for mysql
mysql -hIP地址　-u用户名 -p密码　数据库
本地连接可以省略
4.基本的sql命令
1.库管理
    1.创建数据库
    create database 库名　[charset=utf8]
    create database 库名　default charset utf8 collate utf8_general_ci;
    2.查看已有的数据库
    show databases;
    3.查看已有数据库
    show create database 库名;
    4.切换数据库
    use 库名
    5.删除库
    drop database 库名;
2.表管理
    1.创建表
    create table 表名(字段名　数据类型　字段说明,字段名　数据类型　字段说明);
    2.查看表结构
    desc 表名;
    3.修改表结构
    alter table 表名......
    4.删除表
    drop table 表名;
3.表记录管理
    1.增加----create
    (1)向所有列中插入数据
    insert into 表名　values(值1,值2....),(值1,值2....);
    (2)向部分列中插入数据
    insert into 表名(字段1,字段2...) values(值1,值2....);
    2.查询----retrieve
    (1)select 字段名 from 表名;
    (2)select 字段名 from 表名 where 条件;
    模糊查询(like)和正则查询
    (3)select 字段名 from 表名 where 条件  order by 字段名[desc];
    分页查询：1.当前要看第几页2.每页显示多少条数据
    set @current=5,@pageSize2
    select id, name,age,email from users limit(@current-1)*@pageSize,@pageSize
    (4)联合查询
    select expression1, expression2, ... expression_n
    from tables
    [where conditions]
    UNION [ALL | DISTINCT]
    select expression1, expression2, ... expression_n
    from tables
    [where conditions];
    3.更新----update
    update 表名　set 字段=值,字段=值 where 条件;
    4.删除----delete
    delete from 表名　where 条件;
5.数据类型
1.数字
2.字符串
3.日期和时间
"""
""""
练习:
1.创建数据库:country,编码为utf8,排序校对:utf8_general_ci;
create database country default charset utf8 collate utf8_general_ci;
2.创建表sanguo(id,name,attack,defense,gender,country)
use country;
 create table sanguo(id int primary key auto_increment,name varchar(32) not null,attack float default 0.0,defense float default 0.0,gender enum("w","m"),country varchar(32) not null);

3.插入5条记录
诸葛亮,司马懿,貂蝉,张飞,赵云
攻击(attack>100),防御(defense<100)
insert into sanguo values(1,"诸葛亮",110,80,"m","蜀国"),(2,"司马懿",90,70,"m","魏国");
insert into sanguo values(3,"貂蝉",110,80,"w","魏国"),(4,"张飞",150,120,"m"," 蜀国");
insert into sanguo values(5,"赵云",140,110,"m","蜀国"),(6,"孙权",90,70,"m","吴国");

4.查询所有蜀国人的信息
select * from sanguo where country="蜀国";

5.将赵云的攻击力改为360,防御为68
update sanguo set attack=360,defense=68 where name="赵云";
6.将吴国英雄中攻击值为90的英雄攻击值改为100,防御为60
update sanguo set attack=100,defense=60 where country="吴国" and attack=90;

7.找出攻击值高于100的蜀国的英雄的名字和攻击力
select name,attack from sanguo where country="蜀国" and attack>100;
8.将蜀国英雄按照攻击力从高到底排序
select *  from sanguo where country="蜀国" order by attack desc;

9.魏蜀俩国英雄中名字为三个字的按防御值升序排序
select * from sanguo where (country="蜀国" or country="魏国") and name like "___" order by defense;

10.在蜀国英雄中,查找攻击力前三名并且名字不为null的姓名,攻击力和国家
select name,attack,country from sanguo where country="蜀国" and name is not null order by attack desc limit 3;
"""
"""""
1.mysql普通查询
(1)聚合函数(聚合查询)
函数名　　　　　　　功能
avg(字段名)　　　　求指定字段的平均值
max(字段名)　　　　求指定字段的最大值
min(字段名)　　　　求指定字段的最小值
sum(字段名)　　　　求指定字段的和
count(字段名)　　　求指定字段的记录的个数
聚合函数使用语法
select 聚合函数1,聚合函数2 from 表名
例如:找出sanguo表中最大的攻击力值是多少
select max(attack) from sanguo;

例如:表中共有多少个英雄
 select count(id) from sanguo;

例如:找出sanguo表中最低的防御力值是多少
select min(defense) from sanguo;

例如:蜀国英雄中攻击值大于100的英雄的数量
select count(id) from sanguo where country="蜀国" and attack>100;

注意:聚合函数在默认情况下是不能与其他列一起做查询的
例如:select name,max(attack) from sanguo;

(2)分组查询+聚合查询
分组：分组列,值相同的数据会被划分到一组
语法:
select 分组列,聚合函数(列)
from 表名
where 条件
group by 分组列,...
order by ...
limit... 

例如：求sanguo表中每个国家的总攻击力是多少
select country,sum(attack) from sanguo group by country;
例如:计算每个国家的总攻击力和平均攻击力,总防御力和平均防御力
select country,sum(attack),sum(defense),avg(attack),avg(defense) from sanguo group by country;
例如：所有国家的男英雄中,英雄数量最多的前2名国家名称以及英雄数量
select country,count(id) from sanguo where gender="m" group by country order by count(id) desc limit 2;

(3)分组筛选---having
作用:分组后做组内筛选,配合着group by 联用
语法:
select 分组列,聚合函数(列)
from 表名
where 条件
group by 分组列,...
having 条件
order by ...
limit...
例如：查询出平均攻击力大于105的国家名称
select country,avg(attack) from sanguo group by country having avg(attack)>105;

2.distinct函数:去重
语法:select distinct(列)　from 表名；
例如：查询sanguo表中共有多少个国家
select distinct(country) from sanguo;
3.查询表记录时做数学运算
运算符：＋　－　*　/　% **
例如：查询时显示攻击力翻倍
select attack*2 from sanguo;
例如：更新蜀国所有的英雄攻击力*2
update sanguo set attack=attack*2 where country="蜀国";
例如：查询攻击力＋100之后大于200的英雄的姓名和国家
select name,country from sanguo where attack+100>200;

"""
"""
索引：对数据库表的一列或多列的值进行排序的一种结构
优点：加快数据的检索速度
缺点：占用物理存储空间;对表中数据进行更新时,索引也会动态维护,会降低维护速度
索引的比对手段：
(1)查询系统时间
(2)执行查询
(3)查看执行时间
在某列上创建索引：
(1)查询系统时间
(2)执行查询
(3)查看执行时间
索引的分类：
(1)主键索引
特点：(1)增加主键之后,主键列自动会被增加索引
     (2)增加主键[索引]
     实施手段：
     1.已有表添加主键
     alter table 表名　add primary key(id);
(2)唯一索引
特点:(1)可以有多个
    (2)唯一索引所在的列的值必须唯一
    实施手段：
    1.创建表的时候指定唯一性
    create table xxx(id int primary key auto_increment,phone varchar(20) unique);
    2.对已有表创建索引
    create unique index 索引名　on 表名(字段名);
    create unique index uq_name on sanguo(name);
(3)普通索引
    实施手段:
    1.创建表同时指定普通索引
    create table 表名(id xxx xxx,country varchar(32),index(country),index(字段名));
    2.对已有表增加普通索引
    create index 索引名　on 表名(字段名)；
取消索引：drop index 索引名称　on 表名;
查询索引：show index from 表名;
"""










