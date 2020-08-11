import requests
from lxml import etree

class RenrenLogin(object):
  def __init__(self):
    self.url = 'http://www.renren.com/967469305/profile'
    self.headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

  # 获取字典形式cookie的函数
  def get_cookie_dict(self):
    cookie_dict = {}
    cookies = 'td_cookie=18446744073093166409; anonymid=jzc3yiknvd9kwr; depovince=GW; jebecookies=67976425-f482-44a7-9668-0469a6a14d16|||||; _r01_=1; JSESSIONID=abcp_jUgWA4RdcgwXqtYw; ick_login=f502b729-d6cb-4085-8d74-4308a0a8a17d; _de=4DBCFCC17D9E50C8C92BCDC45CC5C3B7; p=cae86d9f12c5a1ba30901ad3d6ac992f5; first_login_flag=1; ln_uact=13603263409; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20181101/1550/h_main_qz3H_61ec0009c3901986.jpg; t=6d191b90a0236cea74f99b9d88d3fbd25; societyguester=6d191b90a0236cea74f99b9d88d3fbd25; id=967469305; xnsid=6cbc5509; ver=7.0; loginfrom=null; jebe_key=bd6eb791-92b2-4141-b8ed-53d17551d830%7C2012cb2155debcd0710a4bf5a73220e8%7C1565838783310%7C1%7C1565838784555; jebe_key=bd6eb791-92b2-4141-b8ed-53d17551d830%7C2012cb2155debcd0710a4bf5a73220e8%7C1565838783310%7C1%7C1565838784558; wp_fold=0'
    for kv in cookies.split('; '):
      # kv: 'td_cookie=184xxx'
      key = kv.split('=')[0]
      value = kv.split('=')[1]
      cookie_dict[key] = value

    return cookie_dict

  def get_html(self):
    # 获取cookies
    cookies = self.get_cookie_dict()
    print(cookies)
    html = requests.get(
      url=self.url,
      headers=self.headers,
      cookies=cookies,
    ).text
    self.parse_html(html)

  def parse_html(self,html):
    parse_html = etree.HTML(html)
    r_list = parse_html.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()')
    print(r_list)

if __name__ == '__main__':
  spider = RenrenLogin()
  spider.get_html()

















