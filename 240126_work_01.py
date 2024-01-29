import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

def pieplot(dgmf, g, i ):
    color = ['cornflowerblue', 'tomato']
    plt.subplot(3,3, i )
    plt.pie(dgmf, labels=['남', '여'], autopct='%.1f%%', colors=color, startangle=90)
    plt.title(gu)
    plt.suptitle('대구광역시 구별 남녀 인구 비율')


f = open('./public_data/gender.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
daegu_male = []
daegu_female = []
daegu_gu = []
dgmf= []

for row in data:
    if '대구광역시' in row[0]:
        daegu_gu.append(row[0])
        daegu_male.append(int(row[104].replace(',','')))
        daegu_female.append(int(row[207].replace(',','')))

for i in range(9):
    dgmf.append(daegu_male[i])
    dgmf.append(daegu_female[i])
    gu = daegu_gu[i]
    print(dgmf, gu)
    pieplot(dgmf, gu, i+1)
    dgmf=[]


plt.show()