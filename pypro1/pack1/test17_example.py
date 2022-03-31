'''
연습문제) 키보드를 통해 직원 자료를 입력받아 가공 후 출력하기

함수를 두 개 작성

1.
datas = inputfunc() : 키보드로 값을 입력 받아 datas 변수에 담는 역할
while True: 문으로 무한루핑하며, 계속입력할까요?n이 될 때까지 자료를 입력받는다.

2.
processfunc(datas) : datas에 기억된 내용을 출력한다.

처리 조건 :
급여액은 기본급 + 근속수당 
수령액은 급여액 – 공제액

 
근무년수에 대한 수당표

근무년수     근속수당
0~3년      150000
4~8년      450000
9년 이상    1000000

급여 상한액에 대한 공제세율표

급여액        공제세율
300만원 이상    0.5
200만원 이상    0.3
200만원 미만    0.15

현재 년도 구하기
import time
print(time.localtime())
'''

import time
today= time.localtime()

count = 0
    
def inputfunc():
    list = []
    while True:
        data = input('사번, 이름, 기본급, 입사년도 입력 :').split(',')
        global count
        count += 1
        list.append(data)
        re = input('계속하시겠습니까? y/n')
        if re == 'n': 
            break
        else:
            continue
    return list

def processfunc(datas):
    for i in range(count):
        newlist = []
        
        newlist.insert(0,datas[i][0])
        newlist.insert(1,datas[i][1])
        newlist.insert(2,datas[i][2])

        time = today.tm_year-int(datas[i][3]) #근무년수
        newlist.insert(3,time)  #근무년수
        
        #급여액 처리
        if time < 4:
            salary = int(datas[i][2])+int(datas[i][3]) + 150000
            newlist.insert(4,int(datas[i][3]) + 150000) #근속수당
        elif 3 < time < 8:
            salary = int(datas[i][2])+int(datas[i][3]) + 450000
            newlist.insert(4,int(datas[i][3]) + 450000) #근속수당
        elif time > 9:
            salary = int(datas[i][2])+int(datas[i][3]) + 1000000
            newlist.insert(4,int(datas[i][3]) + 1000000) #근속수당
    
        #수령액 처리
        if salary >= 3000000:
            receive = salary - salary * 0.5
            newlist.insert(5,salary * 0.5) #공제액
        elif 3000000 > salary >= 2000000:
            receive = salary - salary * 0.3
            newlist.insert(5,salary * 0.3) #공제액
        else:
            receive = salary - salary * 0.15
            newlist.insert(5,salary * 0.15) #공제액
        

        newlist.insert(6,receive) #수령액
        print(newlist)


datas = inputfunc() 
print('사번\t이름\t기본급\t근무년수\t근속수당\t공제액\t수령액')
processfunc(datas)

print('처리건수 : ' + str(count)+'건')    