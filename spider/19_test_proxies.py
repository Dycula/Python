#使用代理ip访问测试网站,查看结果
import requests
url="http://httpbin.org/get"
headers = {'User-Agent':'Mozilla/5.0'}
proxies={"http":"http://183.6.183.35:8010",
         "https":"https://183.6.183.35:8010"}
#发请求,获取响应内容,查看origin
html=requests.get(url,proxies=proxies,headers=headers,timeout=5).text
print(html)