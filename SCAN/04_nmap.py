apt install nmap

pip install python-nmap # root 사용자에서 설치가 안될 경우, 일반 사용자에서 설치 -> ubuntu@ubuntu:~$ pip install python-nmap
pip show python-nmap
======================================
import nmap

# PortScanner 객체 생성
nm = nmap.PortScanner()

# 로컬호스트에서 포트 22, 80, 443 스캔
nm.scan('127.0.0.1', '22,80,443', '-sV')

# 결과 출력
host = '127.0.0.1'
print(f"Host: {host}")
print(f"Status: {nm[host].state()}")
for port in nm[host]['tcp']:
    state = nm[host]['tcp'][port]['state']
    service = nm[host]['tcp'][port]['name']
    print(f"Port {port}: {state} ({service})")

# 결과
Host: 127.0.0.1
Status: up
Port 22: closed (ssh)
Port 80: closed (http)
Port 443: closed (https)

# 연습 포인트
포트 변경: '22,80,443'을 다른 포트(예: '21,25,110')로 바꿔 실행해보세요.
IP 변경: 127.0.0.1을 다른 로컬 IP(예: 192.168.1.1)로 수정해 테스트.
결과 확인: nm[host]['tcp'] 딕셔너리를 print(nm[host]['tcp'])로 출력해 구조 확인.

----------------------------------------------------

import nmap  # nmap 모듈을 가져옴 (네트워크 스캔을 위한 라이브러리)

# PortScanner 객체 생성
nm = nmap.PortScanner()  # nmap의 PortScanner 클래스를 사용해 객체 생성

# 사용자로부터 IP 주소 입력받기
host = input("스캔할 IP 주소를 입력하세요: ")  # 스캔할 대상 IP 주소를 사용자로부터 입력받음

# 포트 스캔
nm.scan(host, '1-1000', '-sV')  # 입력받은 IP 주소에서 포트 1-1000 범위를 스캔 (-sV 옵션은 서비스 버전 탐지)

# 결과 출력
print(f"Host: {host}")  # 스캔 대상 호스트(IP 주소)를 출력
print(f"Status: {nm[host].state()}")  # 호스트의 상태를 출력 (예: up, down)

# 스캔된 TCP 포트 정보 반복 처리
for port, details in nm[host]['tcp'].items():  # 스캔된 TCP 포트와 해당 정보 반복
    state = details['state']  # 포트의 상태를 가져옴 (예: open, closed)
    service = details['name']  # 포트에서 실행 중인 서비스 이름을 가져옴
    print(f"Port {port}: {state} ({service})")  # 포트 번호, 상태, 서비스 이름을 출력

----------------------------------------------------
---> tcp port가 없을 경우 오류 발생함, 따라서 아래와 같이 if, else 문 추가 
if 'tcp' in nm[host]:
    for port, details in nm[host]['tcp'].items():  
        state = details['state']  
        service = details['name']  
        print(f"Port {port}: {state} ({service})") 
else:
    print("No TCP ports found.")  # TCP 포트가 없는 경우 출력  
---------------------------------------------------------------

ㅁ 여러 호스트를 대상으로 동시에 처리할 경우 ㅁ

주요 추가 사항
1. IP 범위 또는 네트워크 주소 입력:
사용자가 IP 범위(192.168.1.1-192.168.1.10) 또는 네트워크 주소(192.168.1.0/24)를 입력할 수 있도록 수정했습니다.
2. all_hosts() 사용:
nm.all_hosts()를 사용해 스캔된 모든 호스트를 가져옵니다. 이는 입력된 범위 또는 네트워크에서 스캔된 호스트를 순회하기 위해 필요합니다.
3. TCP 포트 확인:
스캔된 호스트에 TCP 포트 정보가 있는지 확인한 후 처리합니다. TCP 포트 정보가 없으면 "No TCP ports found."를 출력합니다.

import nmap  
nm = nmap.PortScanner()  
hosts = input("스캔할 IP 주소 범위를 입력(30.1.1.1-100 또는 30.1.1.0/24): ")  
nm.scan(hosts, arguments='-F -T4')  
for host in nm.all_hosts():
    print(f"Host: {host}") 
    print(f"Status: {nm[host].state()}") 
    if 'tcp' in nm[host]:
        for port, details in nm[host]['tcp'].items(): 
            state = details['state']  
            service = details['name'] 
            print(f"Port {port}: {state} ({service})") 
    else:
        print("No TCP Port")

----아래 코드는 사용 안 함 -- # UDP 포트 정보가 있는 경우 (실제 사용 시 옵션에 -sU 필요함, 그리고 결과까지 너무 오래 걸림) ----
    if 'udp' in nm[host]:
        for port, details in nm[host]['udp'].items(): 
            state = details['state']  
            service = details['name'] 
            print(f"Port {port}: {state} ({service})") 
    else:
        print("No UDP Port")


