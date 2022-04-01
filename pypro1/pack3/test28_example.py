# 커피 자판기 프로그램

class Machine:
    def __init__(self):
        self.coinin = CoinIn()  #클래스의 포함
    def showData(self):
        print("커피 "+ str(self.coinin.cupCount)+'잔과 잔돈 '+ str(self.coinin.culc())+'원')
        
            
class CoinIn:
    def __init__(self):
        self.coin = int(input('동전을 입력하세요 :')) 
        self.cupCount = int(input('몇잔을 원하세요 :'))
    def culc(self):
        change = self.coin - self.cupCount * 200 
        return change
        
if __name__ == '__main__':
    Machine().showData()
    
    