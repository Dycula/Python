import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0)
# 设置
r.hset("user1", "name", "bujingyun")
# 更新
r.hset("user1", "name", "kongci")
# 取数据
print(r.hget("user1", "name"))

# 一次性设置多个filed和value
user_dict = {
    "password": "123456",
    "gender": "F",
    "height": "165"
}
r.hmset("user1", user_dict)
# 获取所有数据
print(r.hgetall("user1"))
# 获取所有的fields和values
print(r.hkeys("user1"))
print(r.hvals("user1"))
