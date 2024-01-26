# 2. 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고 특정 월의 최고 기온 및 최저
# 기온의 평균값을 구하고 그래프로 표현
# n daegu-utf8.csv 또는 daegu-utf8-df.csv 파일 이용
# n 데이터 구조
# ['날짜', '지점', '평균기온', '최저기온', '최고기온’]
# [0] [1] [2] [3] [4]
# n 화면에서 측정할 달을 입력 받아서 진행
# n 해당 기간 동안 최고기온 평균값 및 최저기온 평균값 계산
# - 최고기온 및 최저기온 데이터를 이용하여 입력된 달의 각각 평균값을 구함
# - 문자열 형태의 ‘날짜’ 열의 데이터는 datetime 으로 변경함:
# n 하나의 그래프 안에 2개의 꺾은선 그래프로 결과를 출력
# - 마이너스 기호 출력 깨짐 방지
# - 입력된 월을 이용하여 그래프의 타이틀 내용 변경
# - 최고 온도는 빨간색, 최저 온도는 파란색으로 표시하고 각각 마커 및 legend를 표시


import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def draw_two_plots(title, x_data, max_temp_list1, label_y1, max_temp_list2, label_y2):
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(12, 4))
    plt.plot(x_data, max_temp_list2, marker='s', markersize=6, color='b', label=label_y2)
    plt.plot(x_data, max_temp_list1, marker='s', markersize=6, color='r', label=label_y1)
    plt.xticks(x_data) # 모든 xtick값을 출력함
    #plt.ylim(10, 40)
    plt.title(title)
    plt.legend()
    plt.show()

def main():
    start_year = int(input("시작 연도를 입력하세요: "))
    end_year = int(input("마지막 연도를 입력하세요: "))
    search_month = int(input("기온 변화를 측정할 달을 입력하세요: "))

    weather_df = pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
    weather_df['날짜']  = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')

    e_s = end_year - start_year + 1
    max_temp_list = [0] * (e_s)
    min_temp_list = [0] * (e_s)

    for i in range(e_s):
        max_temp_years_df = weather_df[(weather_df['날짜'].dt.year == start_year + i) & (weather_df['날짜'].dt.month ==search_month)]
        max_temp_list[i] = round(max_temp_years_df['최고기온'].mean(), 1)
        # print(max_temp_list)
        min_temp_years_df = weather_df[(weather_df['날짜'].dt.year == start_year + i) & (weather_df['날짜'].dt.month ==search_month)]
        min_temp_list[i] = round(min_temp_years_df['최저기온'].mean(), 1)
        # print(min_temp_list)

    # print(f'{start_year}년부터 {end_year}년까지 최고 기온 평균 : {max_temp_list}도')
    # print(f'{start_year}년부터 {end_year}년까지 최저 기온 평균 : {min_temp_list}도')

    e_s_max_temp_mean = round(sum(max_temp_list)/len(max_temp_list), 1)
    e_s_min_temp_mean = round(sum(min_temp_list)/len(min_temp_list), 1)

    # print(f'{start_year}년부터 {end_year}년까지 전체 최저 기온 평균 : {e_s_min_temp_mean}도')
    # print(f'{start_year}년부터 {end_year}년까지 전체 최고 기온 평균 : {e_s_max_temp_mean}도')

    print(f'''{start_year} 년부터 {end_year} 년까지 {search_month} 월의 기온 변화
{search_month} 월 최저기온 평균 :''')
    print(', '.join(map(str, min_temp_list)))

    print(f'{search_month} 월 최고기온 평균 :')
    print(', '.join(map(str, max_temp_list)))


    x_data = [i for i in range(start_year, end_year+1)]
    draw_two_plots(f'{start_year}년부터 {end_year}년까지 {search_month}월의 기온 변화', x_data,
                   max_temp_list, '최고 기온',
                   min_temp_list, '최저 기온')

main()
