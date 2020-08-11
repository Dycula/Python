"""
#客户端连接
mysql -hlocalhost -uroot -p123456

#查库
show databases;

#创建库
create database Project default charset utf8 collate utf8_general_ci;

#使用库
use Project;

#创建表格myssql_weather
create table myssql_weather(
id int primary key auto_increment,
PROVINCE varchar(4) NOT NULL,
CITY varchar(10) NOT NULL,
DAY varchar(20) NOT NULL,
WIND_POW varchar(5) NOT NULL,
TEMP varchar(5) NOT NULL,
WIND_DIR varchar(5) NOT NULL,
WEATHER varchar(5) NOT NULL,
);

#插入(insert)
insert into 表名 values(值1),(值2),...;
insert into 表名(字段1,...) values(值1),...;
例如：插入一组数据
    insert into myssql_weather values(458,西藏,阿里,周三(7月24日)白天,<3级,11,无持续风向,晴);

#查询(select)
select * from 表名 [where 条件];
select 字段1,字段名2 from 表名 [where 条件];
例如：查询id=236的城市天气信息
select * from myssql_weather where id=236;
 
 
#更新表记录(update)
update 表名 set 字段1=值1,字段2=值2,... where 条件;

#删除表记录(delete)
delete from 表名 where 条件;   
"""""
