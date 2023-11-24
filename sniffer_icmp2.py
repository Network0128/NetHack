import socket
def main():
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sniffer.bind(('10.1.1.3', 8080))

    print("icmp 패킷 수신 대기중...")

    try:
        while True:
            print(sniffer.recvfrom(65565))
    except KeyboardInterrupt:
        print("프로그램이 종료되었습니다.")

if __name__ == '__main__':
    main()
