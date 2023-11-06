import pandas as pd
import last

txts = pd.read_table('Exception.txt', header=None, names=['地址', 'url'], sep=' url-> ', encoding='utf-8', engine='python')

i = 0
for address in txts['地址']:
    if last.eary == str(address.replace('"', '')):
        print(address, True)
        print(txts['url'][i].replace('place', 'sight'))
    i += 1