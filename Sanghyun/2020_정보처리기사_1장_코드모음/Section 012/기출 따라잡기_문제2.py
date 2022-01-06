a = [50, 30, 70, 10, 90]
max = a[0]
min = a[0]

for i in range(1, 5):

    if a[i] > max:
        max = a[i]

    if a[i] < min:
        min = a[i]

print(max, min, sep='\n')


# 30 > 50 False
# 30 < 50  True
# a[0]=50 보다 리스트에 있는 a[1]~a[5]의 값을 비교해서 작은 것은 큰건 Max 값, 작은 건 min 값에 저장되도록 함
# # len(a) 을 활용하면 range 함수에서 5를 대체하여 사용이 가능함
