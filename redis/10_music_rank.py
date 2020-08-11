import redis
r=redis.Redis(host="127.0.0.1",port=6379,db=0)
r.zadd("ranking",{"song1":1,"song2":1,"song3":1,"song4":1})
r.zadd("ranking",{"song5":1,"song6":1,"song7":1,"song8":1})
r.zincrby("ranking",50,"song3")
r.zincrby("ranking",60,"song4")
r.zincrby("ranking",70,"song7")
#获取前3名
rlist=r.zrevrange("ranking",0,2,withscores=True)
i=1
for name in rlist:
    #第一名:song7　播放次数：71
    #第二名:song4　播放次数：61
    #第三名:song3　播放次数：51
    print("第{}名：{} 播放次数：{}".format(i,name[0].decode(),int(name[1])))
    i+=1