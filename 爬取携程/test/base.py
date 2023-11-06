# -*- coding: utf-8 -*-
import time

import requests
from lxml import etree
import json

class CanSha(object):
    def __init__(self, num, region):
        self.region = region
        self.url = "https://you.ctrip.com/countrysightlist/china110000/p{}.html".format(num)
        self.headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/107.0.0.0 Safari/537.36"}

    # 发送请求并获取源代码
    def get_data_index(self):
        resp = requests.get(self.url, headers=self.headers)
        if resp.status_code == 200:
            return resp.text
        else:
            return None

    # 数据解析
    def parse_data_index(self, resp):
        # 创建对象
        html = etree.HTML(resp)
        list_data = []

        for j in range(1, 11):
            xpaths = '//*[@id="content"]/div[4]/div/div[2]/div/div[2]/div[{}]/div/span/text()'.format(j)
            title = html.xpath(xpaths)
            # list_data.append(title)
            originurl = "https://you.ctrip.com" + html.xpath('//*[@id="content"]/div[4]/div/div[2]/div/div[2]/div[{}]/div/a/@href'
                                                              .format(j))[0]
            # print(title, originurl)

            yield title, originurl
        time.sleep(1)

    def write_data(self, data1, data2):
        with open("Exception.txt", "a", encoding="utf-8") as f:
            f.write(json.dumps(data1, ensure_ascii=False) + ' url-> ' + json.dumps(data2, ensure_ascii=False) + "\n")
    def run(self):
        resp = self.get_data_index()
        for data in self.parse_data_index(resp):
            # print(data[0][0], data[1])
            self.write_data(data[0][0], data[1])

if __name__ == '__main__':
    eary = input("请输入你要爬取的区域:")
    try:
        for num in range(1, 3):
            ErShoFang = CanSha(num, eary)
            ErShoFang.run()
    except Exception as e:
        print(e)