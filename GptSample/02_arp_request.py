ARP 요청 스푸핑 (네트워크 내 장치 MAC 주소 확인)
네트워크에 연결된 장치의 IP와 MAC 주소를 확인하는 ARP 요청을 생성한다.
-----------------------------------------------
from scapy.all import *

# ARP 요청 생성 (IP 범위를 변경 가능)
arp_request = ARP(pdst="192.168.1.1/24")
broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
arp_request_broadcast = broadcast / arp_request

# ARP 요청 전송 및 응답 수집
answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

# 응답 결과 출력
print("IP 주소\t\tMAC 주소")
print("-" * 30)
for sent, received in answered_list:
    print(f"{received.psrc}\t{received.hwsrc}")
---------------------------------------------------------

ARP(pdst="192.168.1.1/24"): 특정 서브넷(예: 192.168.1.0/24)에 대한 ARP 요청.
Ether(dst="ff:ff:ff:ff:ff:ff"): 모든 장치에 브로드캐스트 전송.
IP와 MAC 주소 매핑 정보를 수집할 수 있음.
