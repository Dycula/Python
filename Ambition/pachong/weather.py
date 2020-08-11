from bs4 import BeautifulSoup#网页解析
import requests#获取网页内容
import re#对爬取内容进行匹配和搜索

def get_page(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '错误'

def parse_page(html, return_list):
    soup = BeautifulSoup(html, 'html.parser')
    day_list = soup.find('ul', 't clearfix').find_all('li')
    for day in day_list:
        date = day.find('h1').get_text()
        wea = day.find('p',  'wea').get_text()
        hightem = day.find('p', 'tem').find('span').get_text()
        lowtem = day.find('p', 'tem').find('i').get_text()
        #win = re.search('(?<= title=").*?(?=")', str(day.find('p','win').find('em'))).group()
        win = re.findall('(?<= title=").*?(?=")', str(day.find('p','win').find('em')))
        wind = '-'.join(win)
        level = day.find('p', 'win').find('i').get_text()
        return_list.append([date, wea, lowtem, hightem, wind, level])
    #return return_list

def print_res(return_list):
    tplt = '{0:<10}\t{1:^10}\t{2:^10}\t{3:{6}^10}\t{4:{6}^10}\t{5:{6}^5}'
    print(tplt.format('日期', '天气', '最低温', '最高温', '风向', '风力',chr(12288)))
    for i in return_list:
        print(tplt.format(i[0], i[1],i[2],i[3] + '℃',i[4],i[5],chr(12288)))

def main():
    url = 'http://www.weather.com.cn/weather/101280601.shtml'
    html = get_page(url)
    wea_list = []
    parse_page(html, wea_list)
    print_res(wea_list)

if __name__ == '__main__':
    main()
