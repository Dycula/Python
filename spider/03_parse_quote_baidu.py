"""
总结
1.urllib.request
(1)req=urllib.request(url,headers)
(2)res=urllib.request.urlopen(req)
(3)html=res.read().decode(res)
    res的方法:
    (1)res.read()
    (2)res.getcode()
    (3)res.geturl()
2.urllib.parse
(1)urllib.parse.urlopen({})
(2)urllib.parse.quote(string)
(3)urllib.parse.unquote(string)
"""""
from urllib import request
from urllib import parse


# 拼接url地址
def get_url(word):
    url = "https://www.baidu.com/s?wd={}"
    params = parse.quote(word)
    url = url.format(params)
    return url


# 发请求,保存本地文件
def request_url(url, filename):
    headers = {"User-Agent": "Mozilla/5.0"}
    # 1.创建请求对象
    req = request.Request(url=url, headers=headers)
    # 2.获取响应对象
    res = request.urlopen(req)
    # 3.提取响应内容
    html = res.read().decode("utf-8")
    # 4.保存到本地文件
    with open(filename, 'w') as f:
        f.write(html)


if __name__ == "__main__":
    word = input('请输入搜索内容:')
    url = get_url(word)
    filename = '{}.html'.format(word)
    request_url(url, filename)
