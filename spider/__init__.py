import urllib.request
from urllib import request
url="http://www.baidu.com/"
#向百度发请求,得到响应对象
response=urllib.request.urlopen(url)
#获取响应对象内容
result=response.read().decode("utf-8")
print(result)
#响应对象的方法
bytes=response.read()
string=response.read.decode("utf-8")
url=response.geturl()
code=response.getcode()
string.encode()
bytes.decode()

#定义常用变量
url1="http://httpbin.org/get"
headers={"User-Agent":"Mozilla/5.0"}
#构建请求对象
req=request.Request(url1,headers)
#发请求获取响应对象
res=response.urlopen(req)
#读取响应对象内容
html=result.read().decode("utf-8")
print(html)

from urllib import parse
query_string_dict={"wd":"美女","pn":"50"}
query_string=parse.urlencode(query_string_dict)
url2="http://www.baidu.com/s?{}".format(query_string)
print(url2)

from urllib import request
from urllib import parse
def get_url(word):
    baseurl="http://www.baidu.com/s?"
    params=parse.urlencode({"wd":word})
    url3=baseurl+params
    return url3
def request_url(url3,filename):
    headers={"User-Agent":"Mozilla/5.0"}
    req=request.Request(url3,headers)
    res=request.urlopen(req)
    html=res.read().decode("utf-8")
    with open(filename,"w") as f:
        f.write(html)
if __name__=="__main__":
    word=input("请输入搜索内容：")
    url3=get_url(word)
    filename="{}.html".format(word)
    request_url(url3,filename)

from urllib import parse
string="美女"
print(parse.quote(string))
url="http://www.baidu.com/s?wd={}"
word=input("q请输入要搜索的内容：")
query_string=parse.quote(word)
print(url.format(query_string))

from urllib import parse
string= '%E7%BE%8E%E5%A5%B3'
result=parse.unquote(string)
print(result)

from urllib import request,parse
import time
import random
class BaiduSpider(object):
    def __init__(self):
        self.url="http://tieba.baidu.com/f?kw={}&pn={}"
        self.headers={"User-Agent":"Mozilla/5.0"}
    def get_page(self,url):
        req=request.Request(url=url,headers=self.headers)
        res=request.urlopen(req)
        html=res.read().decode("utf-8")
        return html
    def parse_page(self,html):
        pass
    def write_page(self,filename,html):
        with open(filename,"w") as f:
            f.write(html)
    def main(self):
        name=input("请输入贴吧名：")
        start=int(input("请输入起始页"))
        end=int(input("请输入终止页"))
        for page in range(start,end+1):
            pn=(page-1)*50
            kw=parse.quote(name)
            url=self.url.format(kw,pn)
            html=self.get_page(url)
            filename="{}--第{}页.html".format(name,page)
            self.write_page(filename,html)
            #提示
            print("第{}页爬取成功".format(page))
            #控制爬取速度
            time.sleep(random.randint(1,3))
if __name__=="__main__":
    spider=BaiduSpider()
    spider.main()
