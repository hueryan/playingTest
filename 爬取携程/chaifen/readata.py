import pandas as pd
import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/107.0.0.0 Safari/537.36"}

txts = pd.read_table('Exception.txt', header=None, names=['地址', 'url'], sep=' url-> ', encoding='utf-8',
                     engine='python')

region = input("请输入要爬取的地区：")

i = 0
url = ''
for address in txts['地址']:
    if region == str(address.replace('"', '')):
        print(address, True)
        url = txts['url'][i].replace('place', 'sight')
        break
    i += 1

old_url = url.replace('"', '')

for j in range(1, 51):
    url = old_url
    url = url.replace('.html', '/s0-p{}.html#sightname'.format(j))
    print(url)

    url = requests.get(url, headers=headers)
    html = etree.HTML(url.text)

    for i in range(1, 12):
        if i == 6:
            continue
        sight = html.xpath('//*[@id="content"]/div[4]/div/div[2]/div/div[3]/div[{}]/div[2]/dl/dt/a[1]/text()'.format(i))
        dizhi = html.xpath('//*[@id="content"]/div[4]/div/div[2]/div/div[3]/div[{}]/div[2]/dl/dd[1]/text()'.format(i))
        print("景点名称：" + sight[0], "--> 地址：" + dizhi[0].replace('\r\n', ''))
        with open('city/{}sight.txt'.format(region), 'a', encoding='utf-8') as f:
            f.write("景点名称：" + sight[0] + "--> 地址：" + dizhi[0].replace('\r\n', '') + '\n')
