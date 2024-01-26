import pandas as pd

df = pd.read_csv('./public_data/subwaytime.csv', header=[0,1] )
# print(df.head())
# print(df.columns)
# print(df)
hosun1 = []
# print(df.loc[2])
# print(df.index)

hosun_name = ['1호선', '2호선', '3호선', '4호선', '5호선', '6호선', '7호선']

for j in hosun_name:
    for i in range(621):
        if df.loc[i][1] == j:
            hosun1.append(df.loc[2])
    hosun_df = pd.DataFrame(hosun1)

print(hosun_df)