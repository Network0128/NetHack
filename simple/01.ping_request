Ping 요청 보내기 (ICMP 패킷 생성 및 전송)
네트워크 연결 상태를 확인할 때 사용하는 ping 명령과 동일한 기능을 구현한다.
----------------------------------------
from scapy.all import *

# 대상 IP 주소 설정
target_ip = "8.8.8.8"

# ICMP Echo 요청 패킷 생성
packet = IP(dst=target_ip)/ICMP()

# 패킷 전송 및 응답 수신
response = sr1(packet, timeout=2)

# 응답 분석
if response:
    print(f"응답 수신: {response[IP].src}")
    response.show()
else:
    print("응답 없음")
----------------------------------------
sr1(): 패킷을 전송하고 첫 번째 응답을 기다림.
응답 여부로 네트워크 상태를 확인 가능.
