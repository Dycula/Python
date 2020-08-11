"""
redis相关文件存放路径
1.配置文件:/etc/redis/redis.conf
2.备份文件:/var/lib/redis/*.rdb|*.aof
3.日志文件:/var/log/redis/redis-server.log
4.启动文件:/etc/init.d/redis-server
5./etc/下存放配置文件
6./etc/init.d/下存放服务启动文件

mysql锁机制
1.读锁(共享锁):加读锁后,别人可以查,但是不能改
2.写锁(互斥锁,排他锁):加写锁后,别人不能查,也不能改
"""""
import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0)
# mobile-001
day01_dict = {
    "huawei": 5000,
    "oppo": 4000,
    "iphone": 3000
}
# mobile-002
day02_dict = {
    "huawei": 5200,
    "oppo": 4300,
    "iphone": 3230
}
# mobile-003
day03_dict = {
    "huawei": 5500,
    "oppo": 4660,
    "iphone": 3580
}
r.zadd("mobile-001", day01_dict)
r.zadd("mobile-002", day02_dict)
r.zadd("mobile-003", day03_dict)
#并集
r.zunionstore(
    "mobile-001:003",
    ("mobile-001","mobile-002","mobile-003"),
    aggregate="max"
)
#逆序
rlist=r.zrevrange("mobile-001:003",0,2,withscores=True)
for r in rlist:
    print("品牌：{}　销量:{}".format(r[0].decode(),r[1]))