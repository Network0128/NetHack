apt install nmap

pip install python-nmap # root 사용자에서 설치가 안될 경우, 일반 사용자에서 설치 -> ubuntu@ubuntu:~$ pip install python-nmap
pip show python-nmap

---직전 파일을 nmap을 이용한 코드로 수정: 결과는 동일---
1. import nmap: socket 대신 nmap 모듈 사용.
2. 입력 처리:
    target_ip, start_port, end_port는 동일하게 입력받음.
    port_range = f"{start_port}-{end_port}": Nmap에 전달할 포트 범위 문자열 생성 (예: "1-1024").
3. scanner = nmap.PortScanner(): Nmap 스캐너 객체 생성.
4. scanner.scan(target_ip, port_range): 지정된 IP와 포트 범위를 스캔.
5. 결과 출력:
    scanner.all_hosts(): 스캔된 호스트를 순회.
    scanner[host]['tcp'][port]['state']: 각 포트의 상태 ("open", "closed" 등)를 가져옴.
    state.upper(): 상태를 대문자("OPEN", "CLOSED")로 변환해 출력.
--------------------------------------------------------------------------
import nmap

# 사용자로부터 대상 IP와 포트 범위 입력 받기
target_ip = input("Target IP (ex: 192.168.1.10): ")
start_port = int(input("Start Port number (ex: 1): "))
end_port = int(input("End Port number (ex: 1024): "))

# Nmap 스캐너 객체 생성
scanner = nmap.PortScanner()

# 포트 범위 문자열 생성
port_range = f"{start_port}-{end_port}"

# 스캔 및 출력
print(f"Scanning {target_ip} ports {start_port} ~ {end_port}")
scanner.scan(target_ip, port_range)

# 결과 출력
for host in scanner.all_hosts():
    if 'tcp' in scanner[host]:
        for port in scanner[host]['tcp'].keys():
            state = scanner[host]['tcp'][port]['state']
            print(f"{target_ip}:{port} is {state.upper()}")
