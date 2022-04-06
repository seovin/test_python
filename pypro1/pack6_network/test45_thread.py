# Thread
# process는 실행가능한 파일을 말한다. 프로세스는 현재 실행 중인 프로그램을 의미하면 tesk 라고도 부른다.
# prosess의 작은 실행단위를 thread 라고 한다. thread 기법을 이용하면 여러개의 thread를 통해 여러개의 작업을 할 수 있다.
# multi thread에 의한 muti tasking 이 가능함.

import threading, time

def run(id):
    for i in range(1, 11):
        print('id:{}-->{}'.format(id, i))
        time.sleep(0.5)
        
# 1) thread를 사용하지 않은 경우
# run('일')
# run('이')

# 2) thread를 사용한 경우
th1 = threading.Thread(target = run, args = ('일',))
th2 = threading.Thread(target = run, args = ('이',))
th1.start()
th2.start()

th1.join()
th2.join()
print('프로그램 종료')