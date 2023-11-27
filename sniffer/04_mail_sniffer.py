#성공
from scapy.all import sniff

def packet_callback(packet): #콜백함수 정의
    print(packet.show()) #패킷의 내용과 프로토콜의 정보를 추출해 화면에 출력

def main():
    sniff(prn=packet_callback, count=1) #도청작업 진행

if __name__ == '__main__':
    main()