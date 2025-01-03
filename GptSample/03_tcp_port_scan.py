TCP 포트 스캔 (열려 있는 포트 확인)
특정 대상의 열린 포트를 탐지하여 서비스 동작 여부를 확인한다.

-------------------------------------------
from scapy.all import *

# 스캔 대상과 포트 설정
target_ip = "192.168.1.1"
ports = [22, 80, 443]  # 스캔할 포트 리스트

# 포트 스캔
for port in ports:
    tcp_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
    response = sr1(tcp_packet, timeout=2, verbose=False)
    
    if response and response[TCP].flags == "SA":
        print(f"포트 {port} 열림")
    else:
        print(f"포트 {port} 닫힘")
--------------------------------------------
TCP(dport=port, flags="S"): SYN 플래그로 TCP 핸드셰이크 시작.
response[TCP].flags == "SA": SYN-ACK 응답은 포트가 열려 있음을 의미.
열려 있는 포트로 동작 중인 서비스를 확인 가능.
