while True:
    holsu = input('원하는 크기의 n x n 마방진의 n값을 홀수로 정해주세요: ')
    holsuList = ['3','5','7','9']
    if holsu in holsuList:
        print('마방진을 작성합니다.')
        holsu = int(holsu)
        mabangjin = [[0 for i in range(holsu)] for j in range(holsu)]

        # for i in range(holsu):
            # print(mabangjin[i])

        x_point = (holsu // 2) + 1
        y_point = holsu
        # i 는 1~holsu**2-1번 시행
        # print(x_point, ',', y_point)
        mabangjin[holsu - y_point][x_point - 1] = 1

        # print(mabangjin[5 - y_point][x_point - 1])

        # for i in range(holsu):
        #     print(mabangjin[i])

        # 좌표평면
        for i in range(2, pow(holsu, 2) + 1):
            if 0 < x_point <= holsu and 0 < y_point <= holsu:
                x_point = x_point + 1
                y_point = y_point + 1
                if y_point > holsu and x_point > holsu:
                    x_point -= 1
                    y_point -= 2
                if y_point > holsu:
                    y_point = 1
                if x_point > holsu:
                    x_point = 1
                if mabangjin[holsu - y_point][x_point - 1] != 0:
                    y_point -= 2
                    x_point -= 1
                # print(x_point, ',', y_point)

                mabangjin[holsu - y_point][x_point - 1] = i
            # for i in range(holsu):
                # print(mabangjin[i])

        for i in mabangjin:
            # print(i)
            for j in i:
                print(f'{j:2}', end=" ")
            print()


    else:
        print('다시 입력해주세요.')


# holsu = int(holsu)
# mabangjin = [[0 for i in range(holsu)] for j in range(holsu)]
#
# for i in range(holsu):
#     print(mabangjin[i])
#
#
# x_point = (holsu//2)+1
# y_point = holsu
# # i 는 1~holsu**2-1번 시행
# print(x_point, ',', y_point)
# mabangjin[5 - y_point][x_point - 1] = 1
#
# print(mabangjin[5 - y_point][x_point - 1])
#
#
# for i in range(holsu):
#     print(mabangjin[i])
#
# # 좌표평면
# for i in range(2,pow(holsu,2) +1 ):
#     if  0< x_point <=holsu and 0<y_point<=holsu:
#         x_point = x_point+1
#         y_point = y_point+1
#         if y_point > holsu and x_point > holsu:
#             x_point -= 1
#             y_point -= 2
#         if y_point > holsu:
#             y_point = 1
#         if x_point > holsu:
#             x_point = 1
#         if mabangjin[5-y_point][x_point-1] != 0:
#             y_point -= 2
#             x_point -= 1
#         print(x_point, ',', y_point)
#
#         mabangjin[5-y_point][x_point-1] = i
#     for i in range(holsu):
#         print(mabangjin[i])
#
# for i in mabangjin:
#     # print(i)
#     for j in i:
#         print(j, end=' ')
#     print()