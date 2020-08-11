#urls.py
#用于提供用户能够访问的路由(请求)
from views import *
urls=[("/time",show_time),("/hello",hello),("/bye",bye)]