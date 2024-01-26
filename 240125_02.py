# (1)
#
# import csv
#
# result =[]
# total_number = 0
# with open('./public_data/subwaytime.csv', encoding='utf-8-sig') as f:
#     data = csv.reader(f)
#     next(data)
#     next(data)
#     for row in data:
#         row[4:] = map(int, row[4:])
#         total_number += row[4]
#         result.append(row[4])
#
# print(f'총 지하철 역의 수 : {len(result)}')
# print(f'새벽 4시 승차인원 : {total_number:,}')

# --------------------------------------------------------------------
# (2)
#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
#
# with open('./public_data/subwaytime.csv', encoding='utf-8-sig') as f:
#     data = csv.reader(f)
#     next(data) # 2줄의 헤더 정보 건너 뜀
#     next(data)
#     result = []
#     total_number = 0
#     max_num = -1
#     max_station = ''
#
#     for row in data:
#         row[4:] = map(int, row[4:])
#         total_number += row[4]
#         result.append(row[4])
#         if row[4] > max_num:
#             max_num = row[4]
#             max_station = row[3]
#
# print('새벽 4시 총 승차 인원수: {0:,}'.format(total_number))
# print('최대 승차역: {0}, 인원 수: {1:,}'.format(max_station, max_num))
# result.sort() # 오름차순으로 정렬 result.sort(reverse=True)
# plt.figure(dpi=100)
# plt.bar(range(len(result)), result)
# plt.title('새벽 4시 지하철 총 승차인원 현황')
# plt.show()


# --------------------------------------------------------------------

# # (3)
#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
#
# with open('./public_data/subwaytime.csv', encoding='utf-8-sig') as f:
#     data = csv.reader(f)
#     next(data) # 2줄의 헤더 정보 건너 뜀
#     next(data)
#     result = []
#     total_number = 0
#     max_num = -1
#     max_station = ''
#
#     for row in data:
#         row[4:] = map(int, row[4:])
#         total_number += row[4]
#         result.append(row[4])
#         if row[4] > max_num:
#             max_num = row[4]
#             max_station = row[3]
#
# print('새벽 4시 총 승차 인원수: {0:,}'.format(total_number))
# print('최대 승차역: {0}, 인원 수: {1:,}'.format(max_station, max_num))
# result.sort() # 오름차순으로 정렬 result.sort(reverse=True)
# plt.figure(dpi=100)
# plt.bar(range(len(result)), result)
# plt.title('새벽 4시 지하철 총 승차인원 현황')
# plt.show()


#--------------------------------------------------------------------
# # (4)
#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
#
# with open('./public_data/subwaytime.csv', encoding='utf-8-sig') as f:
#     data = csv.reader(f)
#     next(data) # 2줄의 헤더 정보 건너 뜀
#     next(data)
#     result = []
#     total_number = 0
#     max_num = -1
#     max_station = ''
#
#     for row in data:
#         row[4:] = map(int, row[4:])
#         row_sum = sum(row[10:15:2])
#         #row_sum = row[10] + row[12] + row[14]
#         result.append(row_sum)
#         if row_sum > max_num:
#             max_num = row_sum
#             max_station = row[3] + '(' + row[1] + ')'
#
# print(f'최대 승차 인원역: {max_station} {max_num:,}')
# result.sort(reverse=True)
#
# plt.figure(figsize=(10,4))
# ax1 = plt.subplot(1,2,1)
# plt.title('10개 역의 승차 인원 수', size=12)
# plt.bar(range(10), result[0:10])
# plt.ylabel('승차인원수')
#
# ax2 = plt.subplot(1, 2, 2, sharey = ax1)
# plt.title('전체 역의 승차 인원 수', size=12)
# plt.bar(range(len(result)), result)
#
# plt.suptitle('출근시간대 승차 인원 현황\n', size=20)
# plt.tight_layout()
# plt.show()

# --------------------------------------------------------------------
# # (5)
#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
#
# with open('./public_data/subwaytime.csv', encoding='utf-8-sig') as f:
#     data = csv.reader(f)
#     next(data) # 2줄의 헤더 정보 건너 뜀
#     next(data)
#     max = [0] * 23 # 새벽 3시는 지하철 운행 안함
#     max_station = [''] * 23
#     xtick_list = []
#
#     for i in range(4,27):
#         n = i % 24
#         xtick_list.append((str(n)))
#
#     for row in data:
#         row[4:] = map(int, row[4:])
#         for j in range(23):
#             a = row[j * 2 + 4] # j=0: data[0 * 2 + 4]의 값을 max[0]에 저장하기 위함
#             if a > max[j]:
#                 max[j] = a
#                 max_station[j] = xtick_list[j] + '시: ' + row[3] # 4시: 구로
#     for i in range(len(max)):
#         print(f'[{max_station[i]}]: {max[i]:,}')
#
#
# plt.figure(figsize=(10,10))
# plt.title('시간대별 최대 승차역 정보')
# plt.bar(range(23), max)
# plt.xticks(range(23), labels=max_station, rotation=80)
# plt.tight_layout()
# plt.show()
#
#

# --------------------------------------------------------------------
# # (6)
#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
#
# with open('./public_data/subwaytime.csv', encoding='utf-8-sig') as f:
#     data = csv.reader(f)
#     next(data) # 2줄의 헤더 정보 건너 뜀
#     next(data)
#     subway_in = [0] *24     # 승차 인원 저장 리스트
#     subway_out = [0] * 24   # 하차 인원 저장 리스트
#
#     for row in data:
#         row[4:] = map(int, row[4:])
#         for i in range(24):
#             subway_in[i] += row[4+i*2]
#             subway_out[i] += row[5+i*2]
#
# xtick_list = []
# for i in range(4,28):
#     n = i % 24
#     xtick_list.append(str(n))
#
# plt.figure(dpi=100)
# plt.title('지하철 시간대별 승하차 인원 추이', size=16)
# plt.grid(linestyle=':') # 그리드 라인 표시
# plt.plot(subway_in, label='승차')
# plt.plot(subway_out, label='하차')
# plt.legend()
#
# plt.xticks(range(24), labels=xtick_list)
# plt.xlabel('시간')
# plt.ylabel('인원 (천만명)')
# plt.show()
#
#
#
#

# --------------------------------------------------------------------
# # (7)
# import operator
#
# names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
#
# # Key를 기준으로 정렬 (기본: 오름차순)
# print("[lambda] dict 정렬: key 기준 오름차순")
# res = sorted(names.items(), key=(lambda x:x[0]))
# print(res)
# print()
#
# # Value를 기준으로 정렬, 내림차순: reverse=True
# print("[lambda] dict정렬: value 기준, 내림차순")
# res = sorted(names.items(), key=(lambda x: x[1]), reverse=True)
# print(res)
#


# --------------------------------------------------------------------
# # (8)
# import operator
#
# names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}
#
# # key를 기준으로 정렬 (오름차순)
# sorted_x = sorted(names.items(), key=operator.itemgetter(0))
# print("[operator] dict정렬: key 기준, 오름차순")
# print(sorted_x)
#
# print()
# # value를 기준으로 정렬 (내림차순)
# sorted_x = sorted(names.items(), key=operator.itemgetter(1), reverse=True)
# print("[operator] dict정렬: value 기준, 내림차순")
# print(sorted_x)
#

# --------------------------------------------------------------------
import pandas as pd

df = pd.read_excel('./public_data/subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0,1] )
print(df.head())
print(df.columns)
print(df[('호선명', 'Unnamed: 1_level_1')])
print(df[('지하철역', 'Unnamed: 3_level_1')])
commute_time_df = df.iloc[:, [1,3,10,12,14]]
print(commute_time_df)

print(commute_time_df.dtypes)

commute_time_df[('07:00:00~07:59:59', '승차')] = commute_time_df[('07:00:00~07:59:59', '승차')].apply(lambda x : x.replace(',',''))
commute_time_df[('08:00:00~08:59:59', '승차')] = commute_time_df[('08:00:00~08:59:59', '승차')].apply(lambda x : x.replace(',',''))
commute_time_df[('09:00:00~09:59:59', '승차')] = commute_time_df[('09:00:00~09:59:59', '승차')].apply(lambda x : x.replace(',',''))
print(commute_time_df)

commute_time_df = commute_time_df.astype({('07:00:00~07:59:59', '승차'):'int64'})
commute_time_df = commute_time_df.astype({('08:00:00~08:59:59', '승차'):'int64'})
commute_time_df = commute_time_df.astype({('09:00:00~09:59:59', '승차'):'int64'})
print(commute_time_df.dtypes)

row_sum_df = commute_time_df.sum(axis=1, numeric_only=True)
passenger_number_list = row_sum_df.to_list()
print(row_sum_df)

max_number = row_sum_df.max(axis=0) # 해당 열에서 최대값 찾기
print(max_number)

max_index = row_sum_df.idxmax()
max_line, max_station = df.iloc[max_index, [1, 3]] #최대값의 [1]: 호선,[3]: 지하철역명
print('출근 시간대 최대 승차 인원역: {0} {1} {2:,}명'.format(max_line, max_station, max_number))

import matplotlib.pyplot as plt

passenger_number_list.sort(reverse=True)
plt.figure(dpi=100)
plt.bar(range(len(passenger_number_list)), passenger_number_list)
plt.show()

# --------------------------------------------------------------------


# print(hosunList)

# print(hosunList)

# for j in hosunList:
#     for row in data:
#         print(row[1])
#         print(hosunList[j])
#         if row[1] = hosun:
#             print('y')
#
# for row in data:
#     # if row[11] > max:
#     #     max = row[11]
#     print(row[11])
# maxList.append(max)

# print(maxList)


# # print(hosun)
# hosunList = list(hosun)
# hosunList = sorted(hosunList, reverse=False)
# # print(hosunList)
#
#
# # for i in hosunList:
#     for j in


#         if row[1] > max[i]:
#             max[i] = row[1]
# print(max)
# for row in data:
#     row[12:] = map(int, row[12:])
#


# --------------------------------------------------------------------
# --------------------------------------------------------------------
