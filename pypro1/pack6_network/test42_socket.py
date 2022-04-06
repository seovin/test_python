# 파이썬 네트워크
# 네트워크를 위한 통신 채널을 지원 : socket 모듈

import socket

print(socket.getservbyname('http','tcp')) #포트넘버 80
print(socket.getservbyname('telnet','tcp')) #포트넘버 23
print(socket.getservbyname('ftp','tcp')) #포트넘버 21
print(socket.getservbyname('smtp','tcp')) #포트넘버 25
print(socket.getservbyname('pop3','tcp')) #포트넘버 110

print(socket.getaddrinfo('www.naver.com', 80, proto = socket.SOL_TCP))

