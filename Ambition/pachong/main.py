import itchat
from itchat.content import *

import jieba.analyse
import requests
import json

itchat.auto_login(hotReload=False)

# 调用图灵机器人的api，采用爬虫的原理，根据聊天消息返回回复内容
def tuling(info):
    appkey = "b98734fac27a4022b8c4acde4362d57b"
    body={'key':appkey,'info':info.encode('utf-8')}
    url = "http://www.tuling123.com/openapi/api"
    req = requests.post(url,data=body)
    if req:
        data = json.loads(req.text)
    else:
        return None
    print('data:', data)
    answer = data['text']
    return answer


#程序主要功能
MAIN_FUNCTION={'天气':1}

def text_handle(words):

    jieba.add_word('二狗', tag='nr')  # 添加二狗

    place = ''  # 地点
    first_keyword = ''  # 关键名词
    time = ''  # 时间
    # TF-IDF算法提取关键词，形成关键词列表，根据权重大小依次排序
    words_list = [i for i in jieba.analyse.extract_tags(words, withWeight=False)]
    print(words_list)

    # 获取词性标注
    word_attribute_dict = {key: value for key, value in jieba.posseg.cut(words)}
    print(word_attribute_dict)

    # 提取目标关键词
    for word in words_list:
        value = word_attribute_dict[word]  # 获取词性
        if value == 'ns':  # 地名
            place += word
        elif value == 'n' and not first_keyword:  # 名词
            first_keyword = word
        elif value == 't' and not time:  # 时间词
            time = word
        elif value == 'nr':  # 人名
            pass
        elif value == 'i':  # 成语
            pass

    list_keyword=[
        MAIN_FUNCTION.get(first_keyword,0),
        first_keyword,
        place,
        time,
    ]
    print(list_keyword)
    return  list_keyword


# 对于群聊信息，定义获取想要针对某个群进行机器人回复的群ID函数
def group_id(name):
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']

@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']:
    item = group_id(u'冲出宇宙战舰')  # 根据自己的需求设置

    if msg['FromUserName'] == item and (msg['isAt'] or '二狗' in msg['Text']):

        # 关键词提取
        text_handle_relust = text_handle(msg['Text'])
        if text_handle_relust[0]:#指定功能

            content='后台正在查询'
            '''
            用于后台接口
            coding中
            '''
        else:#普通聊天
            content=tuling(msg['Text'])

        itchat.send(u'%s' % content, item)

# 注册文本消息，绑定到text_reply处理函数
# text_reply msg_files可以处理好友之间的聊天回复
@itchat.msg_register([TEXT])
def text_reply(msg):

    # 关键词提取
    text_handle_relust = text_handle(msg['Text'])
    if text_handle_relust[0]:  # 指定功能

        content = '后台正在查询哦'
        #xxxx(text_handle_relust[0],text_handle_relust[1:])
    else:  # 普通聊天
        content = tuling(msg['Text'])

    itchat.send(u'%s' % content, msg['FromUserName'])

itchat.run()
