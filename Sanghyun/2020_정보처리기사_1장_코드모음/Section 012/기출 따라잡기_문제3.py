def prnt():
    global a, b, c  # 0,5,0 가 전역변수로 저장됨 따라서 함수를 실행할 때마다 a,b,c 의 값이 변경됨됨
    while a < b:  # 0<5 동안 반복
        a += 1  # a = 1 ,2, 3, 4, 5
        c += a  # c에 a를 누적 합산해서 15가 나옴
        print(a, b, c)
        prnt()  # print 함수를 재호출 함


a, b, c = 0, 5, 0
prnt()
print('a =', a, end=', ')
print('b =', b, end=', ')
print('c =', c)

# 따라서 답은, a = 5, b = 5, c = 15
# 1 5 1
# 2 5 3
# 3 5 6
# 4 5 10
# 5 5 15
