-- 左外连接：左表teacher 右表course 关联条件teacher.course_id=course.id
select * from teacher left join course on teacher.course_id=course.id
右外连接：左表teacher 右表course 关联条件teacher.course_id=course.id
select * from teacher right join course on teacher.course_id=course.id
完整外连接：左表teacher 右表course 关联条件teacher.course_id=course.id
select * from teacher full join course on teacher.course_id=course.id
select * from student left join score on student.id=score.stu_id;
子查询　查询student 表中比“李四”年龄大的学员信息
select * from student where age>
(select age from student where name="李四");

查询考试“齐天大圣”老师所教课程的学员的信息
select * from student where id in
(select stu_id from score where score.course_id=
(select course_id from teacher where name="齐天大圣"));

查询在score表中有成绩的学员的信息
select * from student where id in
(select stu_id from score );

查询"python基础"课程并且分数在80分数以上的学员姓名和毕业院校
select name ,school from student
where id in (select stu_id from score
where course_id=(select id from course
 where cname="python基础") and score>80);

查询和"张三"相同班级以及相同专业的同学的信息
select * from student
where name !="张三" and class_id=(select class_id
from student where name ="张三") and major_id=(
select major_id from student where name ="张三");

create table wife(id int primary key auto_increment,
name varchar(32) not null,age int not null,teacher_id int,
constraint fk_teacher_wife foreign key (teacher_id) references teacher(id),
unique(teacher_id));

insert into wife values(1,"白骨精",18,1),(2,"杜蕾斯",32,2),(3,"少年",20,3);


create table goods(id int primary key auto_increment,name varchar(32) not null,
price float not null);
insert into goods values(1,"iphone",8888),(2,"huawei",6666),(3,"vivo",5555);


create  table shopping(id int primary key auto_increment,
t_id int not null,g_id int not null,count int default 1,
constraint fk_teacher_shopping foreign key (t_id) references teacher(id),
constraint fk_goods_shopping foreign key (g_id) references goods(id)
);

insert into shopping(t_id,g_id) values(1,1),(1,2);
insert into shopping(t_id,g_id) values(2,3),(2,3),(3,3);


Navicat for Mysql　数据库管理和开发工具

power Designer 数据库建模















