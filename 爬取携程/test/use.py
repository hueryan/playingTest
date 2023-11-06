import pandas as pd
import base

class readTxt(object):
    def __init__(self, region):
        self.region = region


    def eee(self):
        txts = pd.read_table('Exception.txt', header=None, names=['地址', 'url'], sep=' url-> ', encoding='utf-8', engine='python')
        return txts


    def run(self):
        i = 0
        text = self.eee()
        for address in text['地址']:
            if self.region == str(address.replace('"', '')):
                print(address, True)
                print(text['url'][i].replace('place', 'sight'))
            i += 1

if __name__ == '__main__':
    region = input("请输入你要查询的区域:")
    for i in range(213):
        base.CanSha(i, region).run()
    # base.CanSha(213, region).run()
    readTxt(region).run()