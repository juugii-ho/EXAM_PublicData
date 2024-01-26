# import csv
# f = open('./public_data/daegu.csv', 'r', encoding='utf-8')
# data = csv.reader(f, delimiter=',')
# count=0
# for row in data:
#     if count > 5:
#         break
#     else:
#         print(row)
#     count += 1
# f.close()

# import csv
#
# # encoding='utf-8-sig'로 '\ufeff' 제거
# fin = open('./public_data/daegu.csv', 'r', encoding='utf-8-sig')
# data = csv.reader(fin, delimiter=',')
# # newline='': 한 라인씩 건너 뛰며 저장되는 현상 없앰
# fout = open('daegu-utf8_2.csv', 'w', newline='', encoding='utf-8-sig')
# wr = csv.writer(fout)
# for row in data:
#     for i in range(len(row)):
#         row[i] = row[i].replace('\t', '')
#         if row[0]=='1958-08-15':
#             print(row)
#     wr.writerow(row) # writerow(row): 한 행씩 파일로 저장
# fin.close()
# fout.close()
# print('파일 저장 완료')


# import csv
# f = open('daegu-utf8.csv', encoding='utf-8-sig')
# data = csv.reader(f, delimiter=',')
# header = next(data)
# print(header)
# i = 1
# for row in data:
#     print(row)
#     if i >= 5:
#         break # 5개의 데이터를 출력하면 break
#     i += 1
# f.close()


# import csv
#
# def get_minmax_temp(data):
#
#     header = next(data)
#     min_temp = 100
#     min_date = ''
#
#     max_temp = -999
#     min_date=''
#
#     for row in data:
#         if row[3] == '':
#             row[3] = 100
#         row[3] = float(row[3])
#
#         if row[4] =='':
#             row[4] = -999
#         row[4] = float(row[4])
#
#         if row[3] < min_temp:
#             min_temp = row[3]
#             min_date = row[0]
#         if row[4] > max_temp:
#             max_temp = row[4]
#             max_date = row[0]
#     print('-' * 50)
#     print(f'대구 최저 기온 날짜: {min_date}, 온도: {min_temp}')
#     print(f'대구 최고 기온 날짜: {max_date}, 온도: {max_temp}')
# def main():
#     f = open('daegu-utf8.csv', encoding='utf-8-sig')
#     data = csv.reader(f)
#     get_minmax_temp(data)
#     f.close()
# main()


# import csv
# import matplotlib.pyplot as plt
#
# f = open('daegu-utf8.csv', encoding='utf-8-sig')
# data = csv.reader(f)
#
# header = next(data)
# result = []
#
# for row in data:
#     if row[4] != '':
#         result.append(float(row[4]))
#
# print(len(result))
# f.close()
# plt.figure(figsize=(10,2))
# plt.plot(result, 'r')
# plt.show()




# import csv
# import matplotlib.pyplot as plt
# f = open('daegu-utf8.csv', encoding='utf-8-sig') # utf-8-sig 생략 가능
# data = csv.reader(f)
# header = next(data)
# result = []
# for row in data:
#     if row[4] != '': # 최고 기온 데이터 값이 있으면, 리스트에 저장
#         result.append(float(row[4]))
# print(len(result))
# f.close()
# plt.figure(figsize=(10, 2)) # 그래프 크기 조절(가로 10인치, 세로 2인치)
# plt.plot(result, 'r') # result 리스트에 저장된 값을 빨간색 그래프로 그리기
# plt.show() # 그래프 그리기



#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
# f = open('daegu-utf8.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# next(data)
# result = []
#
# for row in data :
#     if row[-1] != '':
#         result.append(float(row[-1]))
# f.close()
#
# plt.figure(figsize=(10,2))
# plt.hist(result, bins=500, color='blue')
# plt.rc('font', family= 'Malgun Gothic')
#
# plt.rcParams['axes.unicode_minus']  =False
# plt.title("1907년 부터 2023년까지 대구 기온 히스토그램")
# plt.show()



#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
# f = open('daegu-utf8.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# next(data)
# result = []
#
# for row in data :
#     if row[-1] != '' : # 최고 기온을 리스트에 저장
#         result.append(float(row[-1]))
# f.close()
# plt.figure(figsize=(10, 2))
# plt.hist(result, bins=500, color='blue') # result에 저장된 값을 히스토그램으로 그림
# plt.rc('font', family='Malgun Gothic')
# plt.rcParams['axes.unicode_minus'] = False # 레이블에 마이너스('-')기호 깨지는 현상 해결
# plt.title("1907년 부터 2023년까지 대구 기온 히스토그램")
# plt.show()
#
#
#

