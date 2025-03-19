포트 반복문
지정한 포트 범위(start_portstart\_portstart_port부터 end_portend\_portend_port)를 반복하여 각 포트에 대해 TCP 소켓을 생성하고, connect_ex를 사용해 연결을 시도합니다. 
연결 결과가 0이면(Open) 해당 포트가 열려있음을, 그렇지 않으면(Closed) 닫혀 있음을 출력합니다.

with 구문 사용
with 구문을 사용하여 소켓 객체를 생성하면, 스캔 후 자동으로 소켓이 닫히므로 코드가 간결해집니다.

이 코드는 TCP 포트 스캔에 한정되어 있으므로 UDP 포트를 스캔하려면 별도의 방법이 필요합니다. 
이와 같은 포트 스캐너는 기초 네트워크 프로그래밍 및 보안 검사 시 유용하게 활용할 수 있습니다


import socket

# 사용자로부터 대상 IP와 포트 범위 입력 받기
target_ip = input("Target IP (ex: 192.168.1.10): ")
start_port = int(input("Start Port number (ex: 1): "))
end_port = int(input("End Port number (ex: 1024): "))

print(f"{target_ip}의 포트 {start_port} ~ {end_port} 스캔 시작")
for port in range(start_port, end_port + 1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            status = "OPEN"
        else:
            status = "CLOSED"
    print(f"{target_ip}:{port} - {status}")

print("스캔 완료")

