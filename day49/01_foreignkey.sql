-- 单行注释
/*多行注释*/
-- 创建course表:id cname eduration
/*create table course(
    id int primary key auto_increment,
    cname varchar(32) not null,
    eduration int not null
);
-- 向course表中插入测试数据
insert into course(cname,eduration)
values ("python基础",20),("python高级",18),
("web基础",10),("python web",15),("爬虫",10),("人工智能",20);*/
-- 创建teacher表:id name age gender hobby course_id
/*create table teacher(
    id int primary key auto_increment,
    name varchar(32) not null,
    age int not null,
    gender varchar(2) not null,
    hobby varchar(64) not null,
    course_id int,
    -- 外键的表
    constraint fk_course_teacher foreign key(course_id) references course(id)
);*/
-- 向teacher插入测试数据
/*insert into teacher values
(null,"齐天大圣",20,"m","取经",1),
(null,"Maria",30,"w","拍片",2),
(null,"少女",18,"w","看景",3);*/
-- 创建major表:id name
/*create table major(id int primary key auto_increment,name varchar(32) not null);
insert into major(name) values ("AID"),("WEB"),("UID"),("JSD");*/

-- 创建student表：id name age school gender class_id major_id
/*create table student (id int primary key auto_increment,
name varchar(32) not null, age int not null,school varchar(64) not null,
gender char(2) not null,class_id int not null,major_id int not null);
-- 更新student表,增加外键关系在major_id上,引用major表的主键id
alter  table student add constraint fk_major_student foreign key(major_id) references major(id);
insert into student values
(1,"张三",20,"哈佛大学","m",5,1),
(2,"李四",22,"麻省理工学院","m",4,1),
(3,"王二",21,"蓝翔技校","f",4,3),
(4,"刘五",24,"五道口技术学院","f",3,3);
create table classinfo(id int primary key auto_increment,class varchar(32) not null,status tinyint);
alter table student add constraint fk_classinfo_student foreign key(class_id) references classinfo(id);
insert into classinfo values
(1,"1901",0),
(2,"1902",1),
(3,"1903",1),
(4,"1904",1),
(5,"1905",1);
create table score(id int primary key auto_increment,
stu_id int not null,course_id int not null,score int not null,
constraint fk_student_score foreign key(stu_id) references student(id),
constraint fk_course_score foreign key(course_id) references course(id));
insert into score values
(1,1,1,98),
(2,2,1,90),
(3,1,2,92),
(4,4,2,88);*/
-- 删除score表中的fk_student_score外键
alter table score drop foreign key fk_student_score;
-- 为score表中的stu_id增加外键,引用自student主键id,并设置级联操作
alter table score add constraint fk_student_score foreign key(stu_id)
references student(id)
on delete cascade
on update cascade;