import redis
import pymysql


def update_mysql(age, username):
    db = pymysql.connect("127.0.0.1", "root", "123456", "userdb", charset="utf8")
    cursor = db.cursor()
    upd = "update user set age=%s where username=%s"
    try:
        cursor.execute(upd, [age, username])
        db.commit()
    except Exception as e:
        db.rollback()
        print("Error", e)
    cursor.close()
    db.close()


def update_redis(age):
    r = redis.Redis(host="127.0.0.1", port=6379, db=0)
    r.hset("user","age",age)
    print("已同步到redis")
    #设置过期时间
    r.expire("user",30)
    #测试
    print(r.hget("user","age"))


if __name__ == "__main__":
    username=input("请输入用户名")
    age=input("请输入更改后的年龄")
    update_mysql(age,username)
    update_redis(age)
