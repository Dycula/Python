"""
mysql数据库读操作演示
select语句
"""

import pymysql

# 连接套接字
db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")
#获取游标(用于进行数据操作的对象,承载操作结果)
cur=db.cursor()
#执行sql语句
sql="select * from student where sex='m';"
cur.execute(sql)#执行查询后cur使会拥有查询结果

#获取一个查询结果
one_row=cur.fetchmany()
print(one_row)

#获取一个查询结果
many_row=cur.fetchmany(2)
print(many_row)

#获取全部查询结果
all_row=cur.fetchmany()
print(all_row)

db.commit()  # 可以执行多个sql语句一同提交

db.rollback()  # 退回到commit之前的状态

#关闭数据库
cur.close()
db.close()




