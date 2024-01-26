import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('./public_data/subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    hosun = set()
    max_station = set()
    maxList = [0]*52
    minList = [0]*52
    max = [0]*52
    min = [100000000]*52



    for row in data:
        row[4:] = map(int, row[4:])
        hosun.add(row[1])
        hosunList = list(hosun)
        hosunList = sorted(hosunList, reverse=False)

        for j in range(0,7):
            if row[1] == hosunList[j]:
                for i in range(4,52):
                    if row[i] > max[i]:
                        max[i] = row[i]
                        if max[i] > maxList[i]:
                            maxList[i] = max[i]
                        max = [0] * 52

                    if row[i] < min[i]:
                        min[i] = row[i]
                        if min[i] < minList[i]:
                            minList[i] = min[i]
                        min = [100000000] * 52

    print(maxList)
    print(minList)
    print(hosunList)