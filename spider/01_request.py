from urllib import request

url = "http://httpbin.org/get"
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64;Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media CenterPC 6.0; .NET4.0C; InfoPath.3)'
}
# 1.创建请求对象
req = request.Request(url=url, headers=headers)
# 2.获取响应对象
res = request.urlopen(req)
# 3.提取响应内容
html = res.read().decode("utf-8")
print(html)
