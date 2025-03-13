전체 동작 요약
1. IP "10.1.1.2"와 포트 80에 대해 TCP 소켓을 생성하고 타임아웃을 1초로 설정합니다.
2. 연결을 시도하고:
   - 성공 시 "10.1.1.2:80 is open" 출력.
   - 실패 시 "10.1.1.2:80 is not responding" 출력.
   - 1초 내 응답이 없으면 "Timeout...." 출력.
3. 작업 후 소켓을 닫습니다.

---------------------------------------------------------------------------

import socket

target_ip,target_port="10.1.1.2",80 #포트 번호는 정수

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
