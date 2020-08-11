"""
1.创建表设置外键
create table xxx(
    constraint 外键名　foreign key(字段)
    references 主表(主键)
    on delete cascade|restrict|set null
    on update cascade|restrict|set null
);
2.修改表增加外键
alter table 表名　
add constraint 外键名　
foreign key(字段)
references 主表(主键)
on delete cascade|restrict|set null
on update cascade|restrict|set null
"""

"""
连接查询
(1)外连接
    左外连接
        作用:左表中所有的数据都会查询出来(即便不满足条件),
        将右表中满足关联条件的数据查询出来,关联不上的数据关联字段将以null作为填充
        语法：select 字段　from A left join B on 关联条件
    右外连接
        作用:右表中所有的数据都会查询出来(即便不满足条件),
        将左表中满足关联条件的数据查询出来,关联不上的数据关联字段将以null作为填充
        语法：select 字段　from A right join B on 关联条件
    完整外连接
        作用：将俩张表的数据做关联查询,关联的上的则正常显示,
        关联不上的则以null值填充
        语法：select * from A full join B on 关联条件
"""


"""
子查询
什么是子查询？
将一个查询的结果作为外侧操作的一个条件出现
语法：select ... from 表名　where 条件＝(select .....)
　　　select ... from 查询
"""

"""
E-R模型
什么是E-R模型？
    Entity-Relationship模型(实体－关系模型)
    在数据库设计阶段一定会使用到,以图形的方式展示数据库中的表以及表关系
概念
    1.实体-Entity
    表示数据库的一个表
    图形表示:矩形框
    2.属性
    表示某实体中的某一特性,即表的字段
    图形表示：椭圆形
    3.关系-Relationship
    表示实体与实体之间的关联关系
    (1)一对一关系1:1
    A表中的一条记录只能关联到B表中的一条记录上
    B表中的一条记录只能关联到A表中的一条记录上
    在数据库中实现手段
    在任意一张表中增加：1.外键,并引用另一张主键　2.唯一索引/约束
    (2)一对多关系1:M
    A表中的一条记录能够关联到B表中的多条记录上
    B表中的一条记录只能关联到A表中的一条记录上
    在数据库中实现手段
    在“多”表中增加：1.外键,引用“一”表的主键
    (3)多对多关系M:M
    A表中的一条记录能够关联到B表中的多条记录上
    B表中的一条记录能够关联到A表中的多条记录上
    
    在数据库中的实现手段
    靠第三张关联表,来实现多对多
    1.创建第三张表
    2.一个主键,俩外键（外键分别引用自关联的俩张表的主键）
"""

"""
SQL语句的优化
1.索引:经常select,where,order by 的字段应该建立索引
2.单条查询最后添加 LIMIT 1,停止全表扫描
3.where子句中不使用 != ,否则放弃索引全表扫描
4.尽量避免 NULL 值判断,否则放弃索引全表扫描
优化前:select number from t1 where number is null;
优化后:
# 在number列上设置默认值0,确保number列无NULL值
5.尽量避免 or 连接条件,否则放弃索引全表扫描
优化前:select id from t1 where id=10 or id=20;
优化后:
6.模糊查询尽量避免使用前置 % ,否则全表扫描
select name from t1 where name like "%c%";
7.尽量避免使用 in 和 not in,否则全表扫描
优化前:select id from t1 where id in(1,2,3,4);
优化后:
8.尽量避免使用 select * ...;用具体字段代替 * ,不要返回用不到的任何字段
"""










