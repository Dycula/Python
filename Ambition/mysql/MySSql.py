import pymysql


class MySSql:
    def __init__(self, host, userName, password, dbName, charset, port=3306):
        self.config = {
            "host": host,
            "port": port,
            "user": userName,
            "password": password,
            "db": dbName,
            "charset": charset,
        }
        self.db = pymysql.connect(**self.config)
        self.cursor = self.db.cursor()

        self.fields = []

    # affait:事务操作函数
    # sql:接收SQL指令
    # 说明:该函数主要用于insert update delete的数据库操作.
    def affair(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print("affair error:", e)
            self.db.rollback()

    # get_fields:获取字段名函数
    # tableName:指定数据表名
    # 说明:该函数用于获取tableName结构信息中的字段名
    #       函数执行完毕,self.fields存放tableName的字段名信息.
    def get_fields(self, tableName):
        sql = "select * from %s;" % (tableName)
        self.cursor.execute(sql)
        # 清空self.fileds列表
        self.fields.clear()
        # self.cursor.description结果是一个可迭代的二维元组对象
        # 举例它的结果样式：
        # (('id', 3, None, 11, 11, 0, False), ('name', 253, None, 32, 32, 0, False), ('age
        for item in self.cursor.description:
            # item：某一个元组元素->例如('id', 3, None, 11, 11, 0, False)
            # item[0]：元组元素内的首项元素->元组首项元素对应字段名
            # 我们把字段名信息存放到self.fileds列表中.
            # 不插入'id'字段信息
            if item[0] == 'id':
                continue
            self.fields.append(item[0])

    # create:插入记录函数
    # tableName:指定操作数据表名
    # llist:接收一个列表对象->[值1, 值2, 值3, ...]
    # sql指令样式:insert into 表名(字段1,...) values (值1,...);
    def create(self, tableName, llist):
        # 获取tableName字段名信息
        self.get_fields(tableName)
        # 对files和values进行字符串拼接,构造sql指令
        files = ", ".join(self.fields)
        values = ", ".join(llist)
        sql = "insert into %s(%s) values (%s);" % (tableName, files, values)
        print("MySSql>", sql)
        self.affair(sql)

    # delete:删除记录函数
    # tableName:指定操作数据表名
    # where:指定where子句后的删除条件
    # sql指令样式:delete from 表名 [where 条件];
    def delete(self, tableName, where=None):
        sql = "delete from %s where %s;" % (tableName, where)
        if where == None:
            sql = "delete from %s;" % (tableName)
        print("MySSql>", sql)
        self.affair(sql)

    # update:修改记录函数
    # tableName:指定操作数据表名
    # llist:接收一个列表对象 -> ["字段1=值1", "字段2=值2", "字段3=值3", ...]
    # where:where子句后的更新条件
    # sql指令样式：update 表名 set 字段1=值1,字段2=值2,... where 条件;
    def update(self, tableName, llist, where):
        set = ", ".join(llist)
        sql = "update %s set %s where %s;" % (tableName, set, where)
        print("MySSql>", sql)
        self.affair(sql)

    # read:查询记录函数
    # tableName:指定操作数据表名
    # where:where后条件
    # like:like后条件
    # regexp:regexp后条件
    # order_by:order by后条件
    # return:返回查询结果元组对象
    # sql指令样式:select * from 表名 [where 条件] [like 条件] [regexp 条件] [order by 条件];
    def read(self, tableName, where=None, like=None, regexp=None, order_by=None):
        sql = "select * from %s" % (tableName)
        if where is not None:
            sql += " where %s" % (where)
            if like is not None:
                sql += " like %s" % (like)
            if regexp is not None:
                sql += " regexp %s" % (regexp)
            if order_by is not None:
                sql += " order by %s" % (order_by)
        sql += ";"
        print("MySSql>", sql)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # create_table:创建数据表函数
    # tableName:创建数据表表名
    # llist:接收一个list对象->["id int primary key auto_increment",
    #                       "name varchar(32) not null",
    #                       "age int not null", ...]
    # sql指令样式：create table 表名(
    #               字段名 数据类型,
    #               字段名 数据类型,
    #               ...
    #               字段名 数据类型
    #           );
    def create_table(self, tableName, llist):
        fields = ", ".join(llist)
        sql = "create table %s(%s);" % (tableName, fields)
        self.cursor.execute(sql)
