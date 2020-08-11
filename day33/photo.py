#create table photo(id int primary key auto_increment,filename varchar(32),data longblob);
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


#存储文件
with open("a.jpg","rb") as fd:
    data=fd.read()
try:
    sql="insert into photo values(1,'a.jpg',%s);"
    cur.execute(sql,[data])
    db.commit()  # 可以执行多个sql语句一同提交
except:
    db.rollback()  # 退回到commit之前的状态
    """
# 获取图片
sql = "select * from photo \
      where filename='a.jpg'"
cur.execute(sql)

# (1,name,xxxxx)
img = cur.fetchone()
with open(img[1],'wb') as f:
  f.write(img[2])
"""
#关闭数据库
cur.close()
db.close()
