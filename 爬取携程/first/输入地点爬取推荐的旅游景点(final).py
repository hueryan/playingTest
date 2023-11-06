# -*- coding:utf-8 -*-
import requests
import json


class Xie_cheng(object):
    def __init__(self, loc, page):
        self.url = "https://m.ctrip.com/restapi/soa2/20591/getGsOnlineResult?"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
        self.data = {'auth': "",
                     'cid': "09031037315935202308",
                     'ctok': "",
                     'cver': "1.0",
                     'extension': '[]',
                     'lang': "01",
                     'sid': "8888",
                     'syscode': "09",
                     'xsid': "",
                     'keyword': loc,
                     'pageIndex': page,
                     'pageSize': '12',
                     'profile': 'false',
                     'sourceFrom': "",
                     'tab': "sight"}

    # 获取源代码并解析数据
    def post_data(self):
        resp = requests.post(self.url, headers=self.headers, data=self.data).text
        dict_data = json.loads(resp)
        for list_data in dict_data['items']:
            print(list_data['word'])


if __name__ == '__main__':
    loc = input("请输入地点，我们给您爬取出推荐的旅游景点:")
    try:
        for cir_num in range(1, 100):
            XC = Xie_cheng(loc, cir_num)
            XC.post_data()
    except:
        pass
