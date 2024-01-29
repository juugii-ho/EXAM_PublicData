# #(1)
#
# import csv
# f = open('./public_data/age.csv', encoding='utf-8-sig')
# data = csv.reader(f)
#
# header = next(data)
# print(header)
# # row[0]: 행정기관
#
# for row in data:
#     if '산격3동' in row[0]:
#         print(row)
# f.close

# -------------------------------------------------------

# #(2)
#
# import csv
# f = open('./public_data/age.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# header = next(data)
#
# result = []
# for row in data:
#     if '산격3동' in row[0]:
#         for data in row[3:]:        # '산격3동'이 포함된 자료만 출력
#             result.append(data)     # 0세~100세 이상까지 자료를 리스트에 추가
# print(result)
# f.close

# -------------------------------------------------------

# #(3)
#
# import csv
# import matplotlib.pyplot as plt
# import platform
# import koreanize_matplotlib
#
# f = open('./public_data/age.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# result = []
# city = ''
#
# for row in data:
#     if '신암' in row[0]:
#         city = row[0]
#         for data in row[3:]: # 0세부터 100세 이상까지 데이터
#             if ',' in data:
#                 data = data.replace(',','')
#             result.append(int(data))
# f.close
# print(result)
#
# plt.title(f'{city} 인구현황')
# plt.xlabel('나이')
# plt.ylabel('인구수')
# plt.plot(result)
# plt.show()


# -------------------------------------------------------
# #(4)
#
# import csv
# import matplotlib.pyplot as plt
# import platform
# import koreanize_matplotlib
#
# f = open('./public_data/age.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# result = []
# city = ''
#
# def print_population(population):
#     '''
#     특정 지역의 인구 현황을 화면에 출력함
#     '''
#
#     for i in range(len(population)):
#         print(f'{i:3d}세: {population[i]:6d}명', end=' ')
#         if (i +1) % 10 ==0:
#             print()
#
# def drow_population(distict_name, popuation_list):
#     '''
#     특정 지역에 대한 인구 분포를 그래프로 나타냄(plot)
#     - district_name: 지역 이름
#     - population_list: 0~100세 이상까지 인구수 리스트
#     '''
#     # 그래프 출력
#     plt.style.use('ggplot')
#     plt.title('{} 인구 현황'.format(distict_name))
#     plt.xlabel('나이')
#     plt.ylabel('인구 수')
#
#     plt.bar(range(101), popuation_list)
#     plt.xticks(range(0, 101, 10))
#
#     plt.plot(popuation_list)
#     plt.show()
#
# def get_poputlation(city):
#     f = open('./public_data/age.csv', encoding='utf-8-sig')
#     data = csv.reader(f)
#     next(data)
#
#     population_list = []
#     district_name = ''
#
#     for row in data:
#         if city in row[0]:
#             district_name = row[0]
#             for data in row[3:]: # 0세부터 100세 이상까지 데이터
#                 if ',' in data:
#                     data = data.replace(',','')
#                 population_list.append(int(data))
#             break
#     f.close
#
#     print_population(population_list)
#     drow_population(district_name, population_list)
#
# city = input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요:')
# get_poputlation(city)

# -------------------------------------------------------
# #(5)
#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
# def draw_piechart(city_name, city_population, voting_population):
#     non_voting_population = city_population - voting_population
#     population = [non_voting_population, voting_population]
#
#     color = ['tomato', 'royalblue']
#     plt.pie(population, labels=['18세 미만', '투표가능인구'], autopct='%.1f%%', colors=color, startangle=90)
#
#     plt.legend(loc=1)
#     plt.title(city_name + " 투표 가능 인구 비율")
#     plt.show()
#
#
#
# def get_voting_population(city):
#     f = open('./public_data/age.csv', encoding='utf-8-sig')
#     data = csv.reader(f)
#     header = next(data)
#
#     voting_number_list = []
#     city_name = ''
#     city_population = 0
#     voting_population = 0
#     for row in data:
#         if city in row[0]:
#             city_population = row[1]
#             if ',' in city_population:
#                 city_population = city_population.replace(',', '')
#             city_population = int(city_population)
#             city_name = row[0]
#             for data in row[21:]:
#                 if ',' in data:
#                     data = data.replace(',', '')
#                 voting_num = int(data)
#                 voting_number_list.append(voting_num)
#                 voting_population += voting_num
#             break
#     f.close
#     print(f'{city_name}전체 인구 수:{city_population:,}명, 투표 가능 인구 수 : {voting_population:,}명')
#
#     draw_piechart(city_name, city_population, voting_population)
#
# city = input('투표 가능 인구수를 확인할 도시이름을 입력하세요: ')
# get_voting_population(city)




# -------------------------------------------------------
# #(6)
#
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
#
# def draw_piechart(city, population_list, label_list):
#     plt.pie(population_list, labels=label_list, autopct='%.1f%%', startangle=90)
#
#     plt.legend(loc=1)
#     plt.title(city + "학령인구 비율")
#     plt.show()
#
#
#
# def get_population(row, start, end):
#     population = 0
#     for num in row[start:end+1]:
#         if ',' in num:
#             num = num.replace(',', '')
#         num = int(num)
#         population += num
#     return population
#
# def school_age_population(city):
#     city_population = 0
#     non_school_pop = 0
#     school_age_pop = 0
#
#     label_list = ['초등학생', '중학생', '고등학생', '대학생', '비학령인구']
#     population_list = []
#
#     f = open('./public_data/age.csv', encoding='utf-8-sig')
#     data = csv.reader(f)
#     header = next(data)
#
#     for row in data:
#         if city in row[0]:
#             city_population = row[1]
#             if ',' in city_population:
#                 city_population = city_population.replace(',', '')
#             city_population = int(city_population)
#
#             elementary_pop = get_population(row, 9, 14)
#             population_list.append(elementary_pop)
#
#             middleschool_pop = get_population(row, 15, 17)
#             population_list.append(middleschool_pop)
#
#             highschool_pop = get_population(row, 18, 20)
#             population_list.append(highschool_pop)
#
#             university_pop = get_population(row, 21, 24)
#             population_list.append(university_pop)
#
#             school_age_pop = (elementary_pop + middleschool_pop + highschool_pop + university_pop)
#             non_school_pop = city_population - school_age_pop
#             population_list.append(non_school_pop)
#             break
#
#
#     print(f'전체 인구 수 {city_population} 학령인구 비율 : {round((school_age_pop*100)/city_population, 1)}%')
#
#     draw_piechart(city, population_list, label_list)
#
# city = input('학령 인구를 분석할 도시 이름: ')
# school_age_population(city)
#

# -------------------------------------------------------
# #(7)
#
# import csv
# import matplotlib.pyplot as plt
# import platform
# import koreanize_matplotlib
# def print_population(population):
#
#     '''
#     특정 지역의 인구 현황을 화면에 출력함
#     '''
#     for i in range(len(population)):
#         print(f'{i:3d}tp: {population[i]:4d}명', end=" ")
#         if (i+1) % 10 == 0:
#             print()
#     print()
#
# def draw_gender_population(title, male_num_list, female_num_list):
#
#     plt.barh(range(len(male_num_list)), male_num_list, label = '남성')
#     plt.barh(range(len(female_num_list)), female_num_list, label = '여성')
#     plt.rcParams['axes.unicode_minus']=False
#     plt.title(title + ' 성별 인구 비율')
#     plt.legend()
#     plt.show()
#
# def calculate_population():
#     f = open('./public_data/gender.csv', encoding='utf-8-sig')
#     data = csv.reader(f)
#     male_num_list = []
#     female_num_list = []
#
#     district = input('시군구 이름을 입력하세요: ')
#     for row in data:
#         if district in row[0]:
#             for male in row[106:207]:
#                 if ',' in male:
#                     male = male.replace(',', '')
#                 male_num_list.append(-int(male))
#             for female in row[209:310]:
#                 if ',' in female:
#                     female = female.replace(',','')
#                 female_num_list.append(int(female))
#             break
#     f.close()
#
#     print(f'남성 총 인구수:{sum(male_num_list):,}')
#     print_population((male_num_list))
#     print('-----------------------------------')
#     print(f'여성 총 인구수:{sum(female_num_list):,}')
#     print_population(female_num_list)
#     draw_gender_population(district, male_num_list, female_num_list)
#
# calculate_population()
# -------------------------------------------------------
# #(8)
# import csv
# import matplotlib.pyplot as plt
# import koreanize_matplotlib
# f = open('./public_data/gender.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# population=[] # Pie
# city = input('찾고 싶은 지역의 이름을 입력하세요: ')
# male_count = 0
# female_count = 0
#
# for row in data:
#     if city in row[0]:
#         male_count = int(row[104].replace(',',''))
#         female_count = int(row[207].replace(',', ''))
#         break
#
# print(f'{city} 남자 인구 수 : {male_count:,}명, 여자 인구 수 : {female_count:,}명')
#
# population = [male_count, female_count]
# color = ['cornflowerblue', 'tomato']
# plt.pie(population, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90)
# plt.title(city + " 남녀 성별 비율")
# plt.show()

# -------------------------------------------------------
# # (9)
# import csv
# import matplotlib.pyplot as plt
# import platform
# import koreanize_matplotlib
# f = open('./public_data/gender.csv', encoding='utf-8-sig')
# data = csv.reader(f)
# city_list = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시']
# for city in city_list:
#     male_list = []
#     female_list = []
#     for row in data:
#         if city in row[0]:
#             for i in range(106,207):
#                 male_list.append(int(row[i].replace(',','')))
#                 female_list.append(int(row[i+103].replace(',','')))
#             break
#     color = ['cornflowerblue', 'tomato']
#     plt.plot(male_list, label = '남성', color = color[0])
#     plt.plot(female_list, label='여성', color = color[1])
#     plt.title(city + " 남녀 인구 수 비교")
#     plt.xlabel('나이')
#     plt.ylabel('인구 수')
#     plt.legend
#     plt.savefig('img/' + city + '.png', dpi=100)
#     plt.close()

# -------------------------------------------------------
#(10)
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import math

def draw_scatter(city, male_list, female_list, bubble_size_list):
    plt.figure(figsize=(8,4), dpi=100)
    plt.scatter(male_list, female_list, s=bubble_size_list, c=range(101), alpha=0.5, cmap='jet')
    plt.colorbar()
    plt.plot(range(max(male_list)), range(max(male_list)), 'g--')

    plt.title(city + ' 지역의 남녀 인구 수 비교')
    plt.xlabel('남성 인구 수')
    plt.ylabel('여성 인구 수')
    plt.show()

def calculate_population():
    f = open('./public_data/gender.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    male_list = []
    female_list = []
    bubble_size_list = []
    city = input('찾고 싶은 지역의 이름을 입력하세요: ')
    for row in data:
        if city in row[0]:
            for i in range(106,207):
                male_num = int(row[i].replace(',',''))
                female_num = int(row[i+103].replace(',',''))
                bubble_size_list.append(math.pow(male_num+female_num,0.7))
                male_list.append(male_num)
                female_list.append(female_num)
            break

    f.close()
    print(f'[여성 인구] : {female_list}')
    print(f'[남성 인구] : {male_list}')
    draw_scatter(city, male_list, female_list, bubble_size_list)
calculate_population()
# -------------------------------------------------------
