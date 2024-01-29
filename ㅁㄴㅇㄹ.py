import pandas as pd
import numpy as np
data = pd.read_csv('공공보건의료기관현황.csv', index_col=0, encoding='utf-8-sig')
print(data.columns)
print(data.head())

print(data['주소'].head())

addr = pd.DataFrame(data['주소'])
addr = addr['주소'].apply(lambda v : v.split()[:2])
addr = pd.DataFrame(addr.tolist(), columns=('시도', '군구'))
print(addr.head())

print(addr['시도'].unique())

addr[addr['시도'] == '창원시']

addr.iloc[27] = ['경상남도', '창원시']
addr.iloc[31] = ['경상남도', '창원시']

print(addr.iloc[27])
print(addr.iloc[31])

addr[addr['시도'] == '경산시']
addr.iloc[47] = ['경상북도', '경산시']
addr.iloc[47]

addr[addr['시도'] == '천안시']
addr.iloc[209] = ['충청남도', '천안시']
addr.iloc[210] = ['충청남도', '천안시']

print(addr['시도'].unique())