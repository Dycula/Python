import redis

r = redis.Redis(host='localhost',port=6379,db=0)

r.set('username','guods')
print(r.get('username'))
# mset参数为字典
r.mset({'username':'xiaoze','password':'123456'})
# 列表: [b'xiaoze', b'123456']
print(r.mget('username','password'))
# 6
print(r.strlen('username'))

# 数值操作
r.set('age','25')
r.incrby('age',10)
r.decrby('age',10)
r.incr('age')
r.decr('age')
r.incrbyfloat('age',3.3)
r.incrbyfloat('age',-3.3)
print(r.get('age'))

r.delete('username')























