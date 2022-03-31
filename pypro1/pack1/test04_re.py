#정규표현식 : 대량의 문자열에 대해 일정한 패턴을 부여해 원하는 문자열만 취할 수 있다.

import re

ss = "1234abc가나다abcABCfun_123555_6Python if fun"
print(ss)
print(re.findall('123', ss))
aa = re.findall(r'123', ss)
print(aa[0])
print(re.findall('가나', ss))
print(re.findall('[12]', ss))
print(re.findall('[0-9]', ss))
print(re.findall('\d\d', ss)) # \d 한글자 \d\d 두글자 \D \s \S \w \W
print(re.findall('[0-9]+', ss)) # 1회 이상
print(re.findall('[0-9]?', ss)) # 0 or 1회 이상
print(re.findall('[0-9]*', ss))  # 0회 이상
print(re.findall('[0-9]{2}', ss))
print(re.findall('[0-9]{2,3}', ss))
print(re.findall('[a-z]', ss))
print(re.findall('[a-zA-Z]', ss))
print(re.findall('[가-힣]', ss))
print(re.findall('[^가-힣]', ss)) #부정
print(re.findall('.bc', ss)) # .자리에 아무거나
print(re.findall('a..', ss)) 
print(re.findall('^123', ss)) # 123으로 시작하는 .. 
print(re.findall('fun$', ss)) # 으로 끝나는 .. 
print(re.findall('12|34', ss))
print(re.findall('(ab)+(c)', ss)) # 그룹화

p = re.compile('abc') #패턴을 객체로 만듦
print(re.findall(p, ss))

p = re.compile('the', re.IGNORECASE)
print(re.findall(p, ss))