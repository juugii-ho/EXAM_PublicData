# date_string1 = '2024 01 01'
# print(date_string1.split())
# date_string2 = '2023-12-31'
# split_date_string = date_string2.split('-')
# print(split_date_string)
#
# year = split_date_string[0]
# month = split_date_string[1]
# day = split_date_string[2]
#
# print(f'연도:{year}, 월:{month}, 일:{day}')
#


# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
# f = open('daegu-utf8.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# next(data)
# aug = []
#
# for row in data :
#     month = row[0].split('-')[1]
#     # date_list = row[0].split('-')
#     # month = date_list[1]          이 두 줄을 한 줄로 만든 것
#     if row[-1] != '':
#         if month == '08':
#             aug.append(float(row[-1]))
# f.close()
#
# plt.hist(aug, bins = 100, color = 'tomato')
# plt.title('대구 8월의 최고 기온 히스토그램')
# plt.xlabel("Temperature") # x축 레이블
# plt.ylabel("Counts") # y축 레이블
# plt.show()

#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
# f = open('daegu-utf8.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# next(data)
# aug = []
# for row in data :
#     month = row[0].split('-')[1]
#     # date_list = row[0].split('-')
#     # month = date_list[1]          이 두 줄을 한 줄로 만든 것
#     if row[-1] != '' :
#         if month == '08':
#             aug.append(float(row[-1]))
# f.close()
# plt.hist(aug, bins = 100, color = 'tomato')
# plt.title('대구 8월의 최고 기온 히스토그램')
# plt.xlabel("Temperature") # x축 레이블
# plt.ylabel("Counts") # y축 레이블
# plt.show()

#
#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
# f = open('daegu-utf8.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# next(data)
# aug = []
# jan = []
#
# for row in data :
#     month = row[0].split('-')[1]
#     # date_list = row[0].split('-')
#     # month = date_list[1]          이 두 줄을 한 줄로 만든 것
#     if row[-1] != '':
#         if month == '08':
#             aug.append(float(row[-1]))
#         if month == '01':
#             jan.append(float(row[-1]))
# f.close()
#
# plt.hist(aug, bins = 100, color = 'tomato', label = 'Aug')
# plt.hist(jan, bins = 100, color = 'b', label='Jan')
# # plt.title('대구 8월의 최고 기온 히스토그램')
# plt.xlabel("Temperature") # x축 레이블
# # plt.ylabel("Counts") # y축 레이블
# plt.rc('axes', unicode_minus = False)
# plt.legend()
# plt.show()



# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
# def draw_graph_on_date(month, day):
#     f = open('daegu-utf8.csv', encoding='utf-8-sig')
#     data = csv.reader(f)
#     next(data)
#     result = []
#
#     for row in data:
#         if row[-1] != '':
#             date_string = row[0].split('-')
#             if date_string[1] == month and date_string[2] ==day:
#                 result.append(float(row[-1]))
#     f.close()
#     plt.figure(figsize=(15,2))
#     plt.plot(result, 'royalblue')
#     plt.rc('axes', unicode_minus=False)
#     plt.title(f'매년 {month}월 {day}일 최고 기온 변화')
#     plt.show()
#
# month, date = input('날짜(월 일)를 입력하세요: ').split()
# draw_graph_on_date(month, date)



import csv
import matplotlib.pyplot as plt
# import platform
import koreanize_matplotlib

def draw_graph_on_date(start_year, month, day):
    f = open('daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)
    high_temp = []
    low_temp = []
    x_year = []

    for row in data:
        if row[-1] != '':
            date_string = row[0].split('-')
            if int(date_string[0]) >= start_year:
                if int(date_string[1]) == month and int(date_string[2]) ==day:
                    high_temp.append(float(row[-1]))
                    low_temp.append(float(row[-2]))
                    x_year.append(date_string[0])
    f.close()
    plt.figure(figsize=(20,4))
    plt.plot(x_year, high_temp, 'hotpink', marker='o', label='최고기온')
    plt.plot(x_year, low_temp, 'royalblue', marker='s', label='최저기온')

    plt.rc('axes', unicode_minus=False)
    plt.title(f'{start_year}년 이후 {month}월 {day}일의 온도 변화 그래프, size=16')
    plt.legend(loc=2)
    plt.xlabel('year')
    plt.ylabel('temparature')
    plt.show()

draw_graph_on_date(2000, 12, 24)

