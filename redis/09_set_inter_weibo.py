import redis
r=redis.Redis(host="127.0.0.1",port=6379,db=0)
#user1关注的人
r.sadd("user1:focus","peiqi","qiaozhi","danni")
#user2关注的人
r.sadd("user2:focus","peiqi","qiaozhi","lingyang")
#共同和关注:求交集
focus_set=r.sinter("user1:focus","user2:focus")
print(focus_set)
result=set()
for i in focus_set:
    a=i.decode()
    result.add(a)
print(result)