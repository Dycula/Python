import requests
url='http://hbimg.b0.upaiyun.com/ac0a5f64360b9c55a6ea4ba395203543d48a8e401bcf7-6q2JJL_fw658'
headers={"User-Agent":"Mozilla/5.0"}
res=requests.get(url=url,headers=headers)
html=res.content
with open("girl.jpg","wb") as f:
    f.write(html)