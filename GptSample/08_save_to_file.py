패킷 생성 후 파일로 저장하기
Scapy로 만든 패킷을 파일로 저장하고 나중에 분석할 수 있게 한다.
-----------------------------------
from scapy.all import *

# 간단한 패킷 생성 (ICMP Ping 요청)
packet = IP(dst="8.8.8.8") / ICMP()

# 패킷을 파일로 저장
wrpcap("ping_packet.pcap", packet)

print("패킷이 'ping_packet.pcap' 파일에 저장되었다.")
-----------------------------------

IP(dst="8.8.8.8") / ICMP(): ICMP Ping 요청 패킷 생성.
wrpcap("파일명", 패킷): 패킷을 PCAP 파일로 저장.
저장한 파일은 Wireshark 같은 도구로 분석 가능.
