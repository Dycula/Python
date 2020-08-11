import redis

# 创建连接对象
r = redis.Redis(host='127.0.0.1',port=6379,db=0)

# r.keys('*') -> 列表
key_list = r.keys('*')
for key in key_list:
  print(key.decode())

# b'list'
print(r.type('mylist2'))
# 返回值: 0 或者 1
print(r.exists('spider::urls'))
# 删除key
r.delete('mylist2')













