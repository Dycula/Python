import urllib.request
print('test---')
response=urllib.request.urlopen('https://www.baidu.com/')
#获取响应内容
html=response.read().decode("utf-8")
print(html)
#获取HTTP响应码
code=response.getcode()
#获取返回实际数据的URL的地址
url=response.geturl()

print(code,url)