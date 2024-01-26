# # import csv
# # f = open('./public_data/subwayfee.csv', encoding = 'utf-8-sig')
# # data = csv.reader(f)
# # header = next(data)
# # rate = 0
# #
# # for row in data:
# #     for i in range(4,8):
# #         row[i] = int(row[i])
# #     rate = row[4] / (row[4] +row[6])
# #     if row[6] ==0:
# #         print(row)
# # f.close()
# #
# #
# # import csv
# # f = open('subwayfee.csv', encoding='utf-8-sig')
# # data = csv.reader(f)
# # header = next(data)
# # rate = 0
# # for row in data:
# #     for i in range(4, 8):
# #         row[i] = int(row[i]) # 4, 5, 6, 7 컬럼 값을 정수로 변환
# #     rate = row[4] / (row[4] + row[6])
# #     if row[6] == 0: # 무임승차 인원[6]이 없는 역 출력
# #         print(row)
# # f.close()
#
# # import csv
# # f = open('./public_data/subwayfee.csv', encoding='utf-8-sig')
# # data = csv.reader(f)
# # header = next(data)
# # max_rate = 0
# # for row in data:
# #     for i in range(4, 8):
# #         row[i] = int(row[i]) # 4, 5, 6, 7 컬럼 값을 정수로 변환
# #     if row[6] != 0: # 무임승차 인원[6]이 없는 역 출력
# #         rate = (row[6]*100) / (row[4] + row[6])
# #         if rate > max_rate:
# #             max_rate = rate
# #             print(row ,round(rate,2), '%')
# # f.close()
#
# #
# # import csv
# # f = open('./public_data/subwayfee.csv', encoding='utf-8-sig')
# # data = csv.reader(f)
# # header = next(data)
# #
# # max_rate = 0
# # max_row = []
# # max_total_num = 0
# #
# # for row in data:
# #     for i in range(4, 8):
# #         row[i] = int(row[i]) # 4, 5, 6, 7 컬럼 값을 정수로 변환
# #     total_count = row[4] +row[6]
# #     if row[6] != 0 and (total_count >10000): # 무임승차 인원[6]이 없는 역 출력
# #         rate = (row[4]) / total_count
# #         if rate > max_rate:
# #             max_rate = rate
# #             max_row = row
# #             max_total_num = total_count
# #             print(f"호선명:{max_row[1]}, 역이름 : {max_row[3]}, 전체 인원 : {max_total_num:,}명, "
# #                   f"유임승차인원: {max_row[4]:,}명, 유임승차 비율 : {round(max_rate*100, 2):,}%")
# #
# # print()
# # print(f"호선명:{max_row[1]}, 역이름 : {max_row[3]}, 전체 인원 : {max_total_num:,}명, "
# #       f"유임승차인원: {max_row[4]:,}명, 유임승차 비율 : {round(max_rate*100, 2):,}%")
# #
# # f.close()
# #
# # import csv
# # import matplotlib.pyplot as plt
# # # import platform
# # import koreanize_matplotlib
# #
# # f = open('./public_data/subwayfee.csv', encoding='utf-8-sig')
# # data = csv.reader(f)
# # header = next(data)
# # print(header)
# #
# # min_rate = 100
# # min_row = []
# # min_total_num = 0
# #
# # for row in data:
# #     for i in [4,6]:
# #         row[i] = int(row[i]) # 4, 5, 6, 7 컬럼 값을 정수로 변환
# #     print(type(row[4]), type(row[6]))
# #     total_count = row[4] +row[6]
# #     if row[6] != 0 and (total_count >10000): # 무임승차 인원[6]이 없는 역 출력
# #         rate = (row[4]) / total_count
# #         if rate <= 0.5:
# #             print(row, round(rate,2))
# #             if rate < min_rate:
# #                 min_rate = rate
# #                 min_row = row
# #                 min_total_num = total_count
# #
# # f.close()
# #
# #
# # print()
# # print(f"유임 승차 비율이 가장 낮은 역: {min_row[3]}")
# # print(f"전체 인원:{min_total_num:,}명, "
# #       f"유임승차인원:{min_row[4]:,}명, "
# #       f"유임승차비율:{round(min_rate*100, 1)}%")
# #
# # plt.title(min_row[3] + "역 유,무임 승차 비율")
# # label = ['유임승차', '무임승차']
# # values = [min_row[4], min_row[6]]
# # plt.pie(values, labels=label, autopct='%.1f%%')
# # plt.legend(loc=2)
# # plt.show()
#
# import csv
# max= [0] * 4
# max_station = [''] * 4
# label = ['유임승차', '유임하차', '무임승차', '무임하차']
#
# with open('./public_data/subwayfee.csv', encoding='utf-8-sig') as f:
#     data = csv.reader(f)
#     next(data)
#
#     for row in data:
#         for i in range(4, 8):
#             row[i] = int(row[i])
#             if row[i] > max[i-4]:
#                 max[i-4] = row[i]
#                 max_station[i-4] = row[3] + ' ' + row[1]
#
# for i in range(4):
#     print(f'{label[i]}: {max_station[i]} {max[i]:,}명')
#
# import csv
# max = [0] * 4 # [0]: 최대 유임승차,[1]: 최대 유임하차, [2]: 최대 무임승차, [3]: 최대 무임하차
# max_station = [''] * 4
# label = ['유임승차', '유임하차', '무임승차', '무임하차']
# # with 구문: 자동으로 파일을 close()시킴
# with open('./public_data/subwayfee.csv', encoding='utf-8-sig') as f:
#     data = csv.reader(f)
#     next(data)
#     for row in data:
#         for i in range(4, 8):
#             row[i] = int(row[i])
#             if row[i] > max[i-4]: # 원본데이터의 컬럼 (인덱스-4) -> max리스트의 인덱스
#                 max[i-4] = row[i]
#                 max_station[i-4] = row[3] + ' ' + row[1] # '역이름 지하철노선' 추가
# for i in range(4):
#     print(f'{label[i]}: {max_station[i]} {max[i]:,}명')
#

import csv
import matplotlib.pyplot as plt
# import platform
import koreanize_matplotlib

label = ['유임승차', '유임하차', '무임승차', '무임하차'] # 파이 차트 컬러 값
color_list = ['#ff9999', '#ffc000', '#8fd9b6', '#d395b0']
pic_count = 0
with open('./public_data/subwayfee.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)

    for row in data:
        for i in range(4,8):
            row[i] = int(row[i])
        print(row)
        plt.figure(dpi=100) # 저장할 그림파일의 dpi 설정
        plt.title(row[3] + ' ' + row[1])
        plt.pie(row[4:8], labels=label, colors=color_list, autopct = '%.1f%%', shadow=True)
        plt.savefig('img/' + row[3] + ' ' + row[1] + '.png')
        plt.close() # 파일 닫기. 매번 그린 후에 해당 plt를 닫아야함

        pic_count += 1
        if pic_count >=10:
            break