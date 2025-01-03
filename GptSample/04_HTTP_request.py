HTTP 요청 보내기
특정 웹 서버로 간단한 HTTP GET 요청을 보내는 예제.

-------------------------------------------------------
from scapy.all import *

# HTTP 요청 생성 (대상 서버 IP 설정)
ip = IP(dst="93.184.216.34")  # example.com
tcp = TCP(dport=80, flags="S")  # TCP 연결 시작
http_packet = ip / tcp

# 패킷 전송 및 응답 확인
response = sr1(http_packet, timeout=2)

# 응답 결과 출력
if response:
    print(f"응답 받음! 서버: {response[IP].src}")
else:
    print("서버 응답 없음")

-------------------------------------------------------
IP(dst="93.184.216.34"): 대상 웹 서버 IP (example.com).
TCP(dport=80, flags="S"): TCP 핸드셰이크 시작(SYN 플래그 사용).
서버가 응답하면 연결 가능 상태를 확인.
