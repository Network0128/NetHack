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

import nmap

# PortScanner 객체 생성
nm = nmap.PortScanner()

# 특정 IP 주소에 대한 포트 스캔 수행
nm.scan('10.1.1.21', '22-443', '-sV')

#여러 호스트 지정: nm.scan('10.1.1.11-21', '22-443', '-sV')

# 스캔 결과 출력
for host in nm.all_hosts():
    print(f"호스트: {host} ({nm[host].hostname()})")
    print(f"상태: {nm[host].state()}")
    print(f"NMAP 명령어: {nm.command_line()}")
    for proto in nm[host].all_protocols():
        print(f"프로토콜: {proto}")
        for port in nm[host][proto]:
            print(f"포트: {port}, 상태: {nm[host][proto][port]['state']}, 서비스: {nm[host][proto][port]['name']}")
