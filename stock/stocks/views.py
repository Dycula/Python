from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime,timedelta
from .stockdata import GetStockData

import json

# Create your views here.
def GetKlinesView(request):
    # 获取前端股票代码
    # 获取时间
    # 调用方法获取k线图数据
    # 返回结果
    ts_code = request.GET.get('ts_code','000001.SZ')
    start = '20190101'
    end = '20190603'
    klines_data = GetStockData().getKdata(ts_code, start, end)
    # reverse sort
    return HttpResponse(json.dumps({"result":True,"data":klines_data,"error":""}))


def GetAllListView(request):
    stock_list = GetStockData().getAlldata()[0:10]
    return HttpResponse(json.dumps({"result":True,"data":stock_list,"error":""}))


def GetIndustryView(request):

    stock_data = GetStockData().getAlldata()
    industry_data = {}
    for item in stock_data:
        if item["industry"] not in industry_data:
            industry_data[item["industry"]] = 1
        else:
            industry_data[item["industry"]] = industry_data[item["industry"]]+1
    data = {}
    data['result'] = []
    data['title'] = []
    m=0
    for it in industry_data:
        titem = {}
        if it == None:
            titem['name'] = "其他"
        else:
            titem['name'] = it
        titem['value'] = industry_data[it]
        if m<20:
            data['title'].append(titem['name'])
            data['result'].append(titem)
        m=m+1
    print(data)
    return HttpResponse(json.dumps({"result":True,"data":data,"error":""}))


def GetARBRView(request):
    code = '000004.SZ'
    t = datetime.now()
    t0 = t - timedelta(250)
    start = t0.strftime('%Y%m%d')
    end = t.strftime('%Y%m%d')
    data = GetStockData().getARBRdata(code, start, end)
    return HttpResponse(json.dumps({"result": True, "data": data, "error": ""}))

