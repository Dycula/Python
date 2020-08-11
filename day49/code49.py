"""
需求：
1.老师的信息:姓名,年龄,性别,爱好
2.课程信息:课程名称,课时
3.学员信息:姓名,年龄,毕业院校,班级,专业
4.考试信息：某位学员某一门课考了多少分
"""
"""
1.表关系
(1)外键－－－Foreign Key
作用：约束当前表的某列值必须取自于另一张表的主键列值
外键所在的列称之为"外键列"
外键所在的表称之为"外键表"或"子表"
被外键列所引用的表称之为"主表"或"主键表"
(2)语法
    1.在创建表的同时指定外键
    create (字段　类型,
    constraint 外键名　foreign key(字段)　references 主键表(主键列));
    例如：create table Course(id int primary key auto_increment, cname varchar(32));
    create table Treacher(id int primary key auto_increment,
    tname varchar(32),course int,
    constraint fk_course_teacher foreign key(course) references Course(id))
    2.对已有表增加外键
    alter table 表名　add constraint 外键名　foreign key(字段)　references 主键表(主键列);
(3)级联操作
    1.语法
    alter table 表名　
    add constraint 外键名
    foreign key(字段)
    references 主键表(主键)
    on delete 级联操作
    on update 级联操作
    2.级联操作取值
    cascade ---数据的级联删除、更新
    restrict(默认)---子表中有关联数据,那么主表中就不能删除和更新数据
    set null---主表删除数据时,子表中的相关数据会设置为null
(4)表的连接查询
    1.交叉连接－－笛卡尔积
    select 字段名列表 from 表名列表;
    例如：查询teacher和student表中的所有数据
    select * from teacher,student;
    2.多表连接
    select 字段名列表 from 表名列表 where 条件;
    3.内连接－－在关联的俩张表中,把满足条件的数据筛选出来
    select 字段,....
    from 表1　
    inner join 表2　
    on　条件　
    inner join 表3　
    on 条件
    例如:使用内连接查询teacher和course表中的数据(姓名　年龄　课程)
    select * from teacher as t
    inner join course as c
    on t.course_id=c.id;
    练习:查询学员的姓名,年龄,班级,专业名称
    select student.name,student.age,classinfo.class,major.name
    from student
    inner join classinfo
    on student.class_id=classinfo.id
    inner join major
    on student.major_id=major.id;
    练习:查询学员的姓名,院校,班级,考试科目,考试成绩
    select student.name,student.school,classinfo.class,course.cname,score.score
    from student
    inner join classinfo
    on student.class_id=classinfo.id
    inner join score
    on student.id=score.stu_id
    inner join course
    on score.course_id=course.id;

"""
