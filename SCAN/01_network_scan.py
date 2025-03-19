전체 동작 요약
1. IP "10.1.1.2"와 포트 80에 대해 TCP 소켓을 생성하고 타임아웃을 1초로 설정합니다.
2. 연결을 시도하고:
   - 성공 시 "10.1.1.2:80 is open" 출력.
   - 실패 시 "10.1.1.2:80 is not responding" 출력.
   - 1초 내 응답이 없으면 "Timeout...." 출력.
3. 작업 후 소켓을 닫습니다.

import socket #파이썬 표준 라이브러리로 바로 사용 가능

#target_ip,target_port="10.1.1.21",80 #포트 번호는 정수
target_ip = input("스캔할 IP를 입력하세요 (예: 10.1.1.21): ")
target_port = int(input("스캔할 포트 번호를 입력하세요 (예: 80): "))

ipscan_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP소켓 생성

result=ipscan_sock.connect_ex((target_ip,target_port)) #연결 시도
if result==0:
    print(f"{target_ip}:{target_port} is open")
else:
    print(f"{target_ip}:{target_port} is not responding")

ipscan_sock.close() #소켓닫기

----------------------try, except, finally ----------------------------------

import socket 
target_ip,target_port="10.1.1.2",80

ipscan_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP소켓 생성
ipscan_sock.settimeout(1)  # 1초 내에 응답이 없으면 timeout 예외 발생

try:
    result=ipscan_sock.connect_ex((target_ip,target_port)) #연결 시도
    if result==0:
        print(f"{target_ip}:{target_port} is open")
    else:
        print(f"{target_ip}:{target_port} is not responding")
except socket.timeout:
    print("Timeout....")
finally:    
    ipscan_sock.close() #소켓닫기

----------------------간단히 with 문으로 구현하기 -------------------------
import socket

target_ip, target_port = "10.1.1.2", 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(1)
    result = sock.connect_ex((target_ip, target_port))
    print(f"{target_ip}:{target_port} - {'OPEN' if result == 0 else 'CLOSED'}")

-----------try, except 구문 추가 -------------------------
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(1)
    try:
        result = sock.connect_ex((target_ip, target_port))
        print(f"{target_ip}:{target_port} - {'OPEN' if result == 0 else 'CLOSED'}")
    except socket.timeout:
        print(f"{target_ip}:{target_port} - TIMEOUT")
