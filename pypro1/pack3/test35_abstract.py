# 추상 클래스 : 추상 메소드를 하나라도 가지고 있는 경우 대체적으로 추상 클래스 라고 한다.

from abc import *

class AbstractClass(metaclass = ABCMeta): #추상클래스
    @abstractmethod
    def abcMethod(self): # 추상 메소드
        pass
    
    def nomalMethod(self): # 일반 메소드
        print('추상 클래스 내의 일반 메소드')
        
# aa = AbstractClass() # TypeError: Can't instantiate abstract class AbstractClass with abstract method abcMethod

class Child1(AbstractClass):
    name = '난 Child1'
    
    def abcMethod(self): # 추상 클래스의 파생 클래스는 반드시 추상 메소드를 정의 . 강제
        print('추상메소드를 오버라이딩')
        
c1= Child1()
print(c1.name)
c1.abcMethod()
c1.nomalMethod()

print()
class Child2(AbstractClass):
    def abcMethod(self): # 오버라이딩을 강요함
        a = 10
        b = 20
        # ...
        print('추상메소드를 오버라이딩 해서 마법에서 풀림 ㅎㅎ')

    def nomalMethod(self): #오버라이딩이 선택적
        print('부모 클래스의 메소드를 다시 정의함')
        
c2 = Child2()
c2.abcMethod()
c2.nomalMethod()

print('다형성 ----')
mbc = c1
mbc.abcMethod()
print()
mbc = c2
mbc.abcMethod()