import requests
import time
import random
from hashlib import md5


class YdSpider(object):
    def __init__(self):
        # url一定为F12抓到的headers-->General-->Requests
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "238",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=-1449945727@10.169.0.82;OUTFOX_SEARCH_USER_ID_NCOO = 1492587933.976261;JSESSIONID = aaa5_Lj5jzfQZ_IPPuaSw; ___rl__test__cookies = 1559193524685",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome / 74.0.3729.169Safari / 537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

    # 获取salt,sign,ts
    def get_salt_sign_ts(self,word):
        # 1.ts
        ts=str(int(time.time()*1000))
        # 2.salt
        salt=ts+str(random.randint(0,9))
        # 3.sign
        string="fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s=md5()
        s.update(string.encode())
        sign=s.hexdigest()
        return salt,sign,ts

    def attack_yd(self,word):
        # 1.先拿到salt,sign,ts
        salt, sign, ts=self.get_salt_sign_ts(word)
        # 2.定义form表单数据为字典
        data={
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': ts,
            'bv': 'cf156b581152bd0b259b90070b1120e6',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        # 3.直接发请求requests.post(url,data=data,headers=xxx)
        res=requests.post(url=self.url,data=data,headers=self.headers).json()
        result = res['translateResult'][0][0]['tgt']
        return result


    # 主函数
    def main(self):
        # 输入翻译单词
        word=input("请输入要翻译的单词：")
        result=self.attack_yd(word)
        print("翻译结果：",result)

if __name__ == "__main__":
    spider = YdSpider()
    spider.main()
