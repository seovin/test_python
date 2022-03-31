# 함수 : 실인수(매개변수)와가인수의 매핑
# 매개변수의 유형 : 위치 매개변수, 기본값 매개변수, 키워드 매개변수 ,가변 매개변수

def showGugu(start, end = 5):
    for dan in range(start, end + 1):
        print(str(dan) + '단 출력')
        
showGugu(2, 3)
print()
showGugu(3)
print()
showGugu(start = 2, end = 3)
print()
showGugu(end = 3, start = 2)
print()
showGugu(2, end = 3)
print()
# showGugu(start = 2, 3) #err
# showGugu(end = 3, 2) #err

def func1(*ar):
    print(ar)

func1('김밥')
func1('김밥', '비빔밥')
func1('김밥', '비빔밥', '볶음밥')

#def func2(*ar, a): err
def func2(a, *ar):
    print(a)
    for i in ar:
        print('배고프면', i)

func2('김밥')
func2('김밥', '비빔밥')
func2('김밥', '비빔밥', '볶음밥')

print()
def process(choice, *ar):
    if choice =='sum':
        res = 0
        for i in ar:
            res += i
    elif choice =='mul':
        res = 0
        for i in ar:
            res *= i
    return res
        
print(process('sum',1,2,3,4,5))
print(process('mul',1,2,3,4,5))
print(process('mul',1,2,3))

print()
def func3(w, h, **other):
    print('몸무게 : {}, 키 : {}'.format(w, h))
    print(other)
    
func3(66, 177)
print()
func3(66, 177, irum='지구인', age = 22)
func3(66, 177, irum='한국인')

print()
def func4(a, b, * v1, **v2):
    print(a, b)
    print(v1)
    print(v2)
    
func4(1, 2)
func4(1, 2, 3, 4, 5)
func4(1, 2, 3, 4, 5, m=6, n=7)
