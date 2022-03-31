# 문1 ) 2 ~ 9 단 모두 출력

for i in range(2,10):
    for j in range(1,10):
        print('{0} * {1} = {2}'.format(i,j,i*j))

# 문2 ) 1 ~ 100 사이의 정수 중 3의 배수 이면서 5의 배수의 합 출력
sum = 0
for i in range (100):
    if i % 3 == 0 and i % 5 == 0:
        sum += i
print(sum)

# 문 3) 주사위를 두번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
# 예 ) 1 3 
# 예 ) 2 2

for i in range(1,7):
    for j in range(1,7):
        if (i + j) % 4 == 0:
            print(i,j)