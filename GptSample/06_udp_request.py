UDP 패킷 전송 (DNS 요청처럼 사용)
UDP 패킷을 전송해 대상 서버가 응답하는지 확인하는 예제.
---------------------------------
from scapy.all import *

# UDP 요청 생성 (대상 서버 설정)
ip = IP(dst="8.8.8.8")  # Google DNS
udp = UDP(dport=53)  # DNS 기본 포트(53)
dns_request = ip / udp / "Test"

# 패킷 전송 및 응답 확인
response = sr1(dns_request, timeout=2)

# 응답 결과 출력
if response:
    print(f"응답 받음! 서버: {response[IP].src}")
else:
    print("서버 응답 없음")
---------------------------------

UDP(dport=53): UDP의 53번 포트로 패킷 전송.
sr1(): 패킷을 전송하고 응답을 기다림.
DNS처럼 UDP 기반 프로토콜 테스트 가능.
