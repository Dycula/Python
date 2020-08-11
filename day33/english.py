import pymysql
import re

f = open('dict.txt')

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='123456',
                     database='stu',
                     charset='utf8')

# 获取游标(用于进行数据操作的对象,承载操作结果)
cur = db.cursor()

sql = "insert into words (word,mean) \
      values (%s,%s)"

for line in f:
  # 获取 word 和 mean
  tup = re.findall(r"(\S+)\s+(.*)",line)[0]
  try:
    cur.execute(sql,tup)
    db.commit()
  except:
    db.rollback()

f.close()
cur.close()
db.close()


