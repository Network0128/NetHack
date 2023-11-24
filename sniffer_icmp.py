#icmp 패킷을 수신하는 코드
import socket

HOST = '10.1.1.2'  # 상대방이 아닌 본인의 IP주소

def main():
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sniffer.bind((HOST, 8080))
    #ICMP는 포트번호를 사용하지 않으므로 상관없음

    print(sniffer.recvfrom(65565))

if __name__ == '__main__':
    main()

