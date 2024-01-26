# 2022.5 버전

# 1. 과거 10년 동안의 대구 날씨 데이터에서 1년 중 일교차가 가장 큰 달은 각각 몇 월인지 그래프로 표시
# n 기간: 최근 10년 (2014년 ~ 2023년)
# - 각 달의 일교차(최고기온 – 최저기온)를 비교하여 각 년도별 일교차가 가장 큰
# 달을 bar 그래프로 표시
# - Pandas 또는 Python 코딩

import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_two_plots(title, x_data, ilgyo):
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(12, 4))
    plt.bar(x_data, ilgyo)
    plt.xlabel('Year/Month')
    plt.ylabel('일교차')
    plt.title(title)
    plt.show()



def main():
    start_year = 2014
    end_year = 2023

    weather_df = pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
    weather_df['날짜']  = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')

    ilgyo = [0] * 10

    max_temp_list = [0] * (12)
    min_temp_list = [0] * (12)
    x_data = [0] * 10

    for j in range(10):
        for i in range(1,13):
            max_temp_years_df = weather_df[(weather_df['날짜'].dt.year == start_year + j) & (weather_df['날짜'].dt.month == i)]
            max_temp_list[j] = max_temp_years_df['최고기온'].mean()
            min_temp_years_df = weather_df[(weather_df['날짜'].dt.year == start_year + j) & (weather_df['날짜'].dt.month == i)]
            min_temp_list[j] = min_temp_years_df['최저기온'].mean()
            ilgyoMm = max_temp_list[j] - min_temp_list[j]
            if ilgyoMm > ilgyo[j]:
                ilgyo[j] = ilgyoMm
                x_data[j] = str(2014+j) +'.'+ str(i)
                # print(x_data)

    # print(ilgyo, max(ilgyo))
    # print('')
    draw_two_plots('지난 10년간 대구의 일교차가 가장 큰 달', x_data, ilgyo)


main()



# # ------------------------
# 2022.4 버전



# # 1. 과거 10년 동안의 대구 날씨 데이터에서 1년 중 일교차가 가장 큰 달은 각각 몇 월인지 그래프로 표시
# # n 기간: 최근 10년 (2014년 ~ 2023년)
# # - 각 달의 일교차(최고기온 – 최저기온)를 비교하여 각 년도별 일교차가 가장 큰
# # 달을 bar 그래프로 표시
# # - Pandas 또는 Python 코딩
#
# import pandas as pd
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
# def draw_two_plots(title, x_data, ilgyo):
#     plt.rcParams['axes.unicode_minus'] = False
#     plt.figure(figsize=(12, 4))
#     plt.bar(x_data, ilgyo)
#     plt.xlabel('Year/Month')
#     plt.ylabel('일교차')
#     plt.title(title)
#     plt.show()
#
#
#
# def main():
#     start_year = 2014
#     end_year = 2023
#
#     weather_df = pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
#     weather_df['날짜']  = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
#
#     ilgyo = [0] * 10
#
#     max_temp_list = [0] * (12)
#     min_temp_list = [0] * (12)
#     x_data = [0] * 10
#
#     for j in range(10):
#         for i in range(1,13):
#             max_temp_years_df = weather_df[(weather_df['날짜'].dt.year == start_year + j) & (weather_df['날짜'].dt.month == i)]
#             max_temp_list[j] = round(max_temp_years_df['최고기온'].mean(), 1)
#             min_temp_years_df = weather_df[(weather_df['날짜'].dt.year == start_year + j) & (weather_df['날짜'].dt.month == i)]
#             min_temp_list[j] = round(min_temp_years_df['최저기온'].mean(),1)
#             ilgyoMm = max_temp_list[j] - min_temp_list[j]
#             if ilgyoMm > ilgyo[j]:
#                 ilgyo[j] = ilgyoMm
#                 x_data[j] = str(2014+j) +'.'+ str(i)
#                 # print(x_data)
#
#     # print(ilgyo, max(ilgyo))
#     # print('')
#     draw_two_plots('지난 10년간 대구의 일교차가 가장 큰 달', x_data, ilgyo)
#
#
# main()