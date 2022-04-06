li = [1,2,2,2,3,4,5,5,5,2,2]  # 리스트 타입
im = set(li)
li = list(im)
print(li)

for i in {1, 2, 3, 4, 5, 5, 5, 5}:
  print(i, end = ' ')
  
a = 1; b = 2; c = 3;

def func1():
    a = 111
    b = 222
    def func2():
        global c
        nonlocal b
        print('func2 안에서 a:{}, b:{}, c:{}'.format(a, b, c))
        c = 333
        b = 444
    func2()
func1()

v1, *v2, v3 = [1, 2, 3, 4, 5]
print(v1)
print(v2)
print(v3) 


def Hap(m, n):
  return m + n

print(Hap(1, 2))
lambda x, y:x + y
print((lambda x, y:x + y)(1, 2))

print(list(range(1, 6, 2))) 


dan = 3    
while True:
    num = 1
    while True:
        print('{}*{}={}'.format(dan, num, dan*num), end=' ')
        num += 1
        if num == 10:
            break
    print()
    dan += 2
    if dan > 9:
        break
    
def func():
    sum = 0
    for i in range(100):
        if i % 5 == 0:
            sum += i
    return sum

print(func())



sum = 0
count = 0
for i in range(1,101):
    if i % 2 != 0:
        count += 1
        sum += i
print('홀수의 합 : {} 홀수의 갯수: {}'.format(sum,count))

def func9():
    sum = 0
    count = 0
    i = 0
    while True:
        i += 1
        if i % 2 == 0:
            count += 1
            sum += i
        if i == 100:
            break
    return sum , count 

sum, count = func9()
print('짝수의 합 : {} 홀수의 갯수: {}'.format(sum,count))

for i in range(1,3):
    for j in range(1,3):
        if (i + j) % 2 == 0:
            print(i,j)
            
datas = {'python', 'java', 'go'} 
a = 0
while a < 3:
    print(datas[a])
    a += 1