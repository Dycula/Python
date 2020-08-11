from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re


class MyMiddleware(MiddlewareMixin):
    count = 0  # 此变量用来记录整个网站的访问记录

    def process_request(self, request):
        self.__class__.count += 1
        print("count=%d", self.__class__.count)
        if self.__class__.count <= 5:
            return None
        else:
            return HttpResponse("此网站方位次数已达上限")


class VisitLimit(MiddlewareMixin):
    visit_times = {}

    def process_request(self, request):
        if request.method != "POST":
            return
        ip_address = request.META['REMOTE_ADDR']
        if not re.match('^/test', request.path_info):
            return
        times = self.visit_times.get(ip_address, 0)
        self.visit_times[ip_address]=times+1
        print(self.visit_times)
        if times>1:
            return HttpResponse("你被拒绝注册")
