from MySSql import *


def main():
    config = {
        "host": "localhost",
        "userName": "root",
        "password": "123456",
        "dbName": "stu",
        "charset": "utf8"
    }
    mydb = MySSql(**config)

    # #添加记录测试
    # mydb.create("class", ["'史蒂芬库里'", "'男'", '35', '95'])

    # #删除记录测试
    # mydb.delete("class", where="年龄 < 10")

    # #更新记录测试
    # mydb.update("class", ["年龄=28", "分数=96"], where="姓名='史蒂芬库里'")

    # # 查询记录测试
    # result = mydb.read('user', where="name", like="'T%%'")
    # print(result)
    # #order_by: "字段名 [desc]"
    # result = mydb.read('user', where="name='chvv'", order_by="id desc")
    # print(result)

    # #创建数据表测试
    # llist = ["id int primary key auto_increment",
    #          "name varchar(32) not null",
    #          "age int not null"]
    # mydb.create_table('Test', llist)


if __name__ == "__main__":
    main()
