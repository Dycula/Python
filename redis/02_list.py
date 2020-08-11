import redis

r = redis.Redis(host='localhost',port=6379,db=0)

# pylist: ['pythonweb','socket','pybase']
r.lpush('pylist','pybase','socket','pythonweb')
# pylist: ['spider','pythonweb','socket','pybase']
r.linsert('pylist','before','pythonweb','spider')
# 4
print(r.llen('pylist'))
# [b'spider', b'pythonweb', b'socket', b'pybase']
print(r.lrange('pylist',0,-1))
# b'pybase'
print(r.rpop('pylist'))
# [b'spider', b'pythonweb']
r.ltrim('pylist',0,1)

while True:
  # 如果列表中为空时,则返回None
  result = r.brpop('pylist',1)
  if result:
    print(result)
  else:
    break


r.delete('pylist')























