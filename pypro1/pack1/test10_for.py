#반복문 for 와 range()
# range(초기치, 목적치, 증가치) : 수열 생성 함수

print(list(range(1, 6, 1)))
print(list(range(1,6)))
print(set(range(1,6)))
print(tuple(range(1,6)))
print(list(range(6)))
print(list(range(0,6)))
print(list(range(1, 11, 2)))
print(list(range(-10, -100, -20)))

print()
for i in range(6):
    print(i, end = ' ')
    
print()
for i in range(1, 10): # java : for(int i = 0; i < 10; i++){ }
    print('{0}*{1}={2}'.format(2, i, i * 2), end = ' ')
    
print()
tot = 0 
for i in range(1, 11):
    tot += i
    
print('합은 ' + str(tot))
print('합은 ' + str(sum(range(1, 11))))

print()
# 참고 : n-gram : 문자열에서 n개의 연속된 요소를 추출하기
# 문자 단위 2 -gram
text = 'hello'

for i in range(len(text)):
    print(text[i:i+2])
    #print(text[i:i+3])
    
print()
# 단어 단위
text = 'this is python program'
words = text.split()
print(words)

for i in range(len(words) - 1):
    print(words[i], words[i + 1])


