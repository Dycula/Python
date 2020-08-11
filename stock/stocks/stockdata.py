import tushare as ts
import talib as ta
from datetime import datetime, timedelta

class Test(object):
    def getTest(self):

        pro = ts.pro_api('b280312f2903dbec185c07535e9ab3f67df9bfe2220e08e46742b9b5')
        data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

        pass

class GetStockData(object):

    def getKdata(self,code, start, end):
        pro = ts.pro_api('b280312f2903dbec185c07535e9ab3f67df9bfe2220e08e46742b9b5')
        df = pro.daily(ts_code=code,start_date=start,end_date=end)
        result = []
        for index,idx in enumerate(df.index):
            re = []
            re.append(df.ix[idx]['trade_date'])
            re.append(df.ix[idx]['open'])
            re.append(df.ix[idx]['close'])
            re.append(df.ix[idx]['low'])
            re.append(df.ix[idx]['high'])
            result.append(re)
        return result

    def getAlldata(self):
        pro = ts.pro_api('b280312f2903dbec185c07535e9ab3f67df9bfe2220e08e46742b9b5')
        df = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
        result = []
        for index,idx in enumerate(df.index):
            item = {}
            item['ts_code'] = df.ix[idx]['ts_code']
            item['name'] = df.ix[idx]['name']
            item['area'] = df.ix[idx]['area']
            item['industry'] = df.ix[idx]['industry']
            item['list_date'] = df.ix[idx]['list_date']
            result.append(item)
        return result


    def getARBRdata(self, code, start, end):
        pro = ts.pro_api('b280312f2903dbec185c07535e9ab3f67df9bfe2220e08e46742b9b5')
        df = pro.daily(ts_code=code, start_date=start, end_date=end)
        df = df.sort_values(by='trade_date', axis=0)

        df['HO'] = df.high - df.open
        df['OL'] = df.open - df.low
        df['HYC'] = df.high - df.close.shift(1)
        df['YCL'] = df.close.shift(1) - df.low
        df['AR'] = ta.SUM(df.HO,timeperiod=26)/ta.SUM(df.OL,timeperiod=26)*100
        df['BR'] = ta.SUM(df.HYC,timeperiod=26)/ta.SUM(df.YCL,timeperiod=26)*100
        df_data = df[['trade_date','AR','BR']].dropna()
        result = {}
        result['trade_date']=[]
        result['AR']=[]
        result['BR']=[]
        for index,idx in enumerate(df_data.index):
            result['trade_date'].append(df_data.ix[idx]['trade_date'])
            result['AR'].append(df_data.ix[idx]['AR'])
            result['BR'].append(df_data.ix[idx]['BR'])
        return result





if __name__ == '__main__':
    t = datetime.now()
    t0 = t - timedelta(250)
    start = t0.strftime('%Y%m%d')
    end = t.strftime('%Y%m%d')
    GetStockData().getARBRdata('000001.SZ',start,end)
