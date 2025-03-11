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
