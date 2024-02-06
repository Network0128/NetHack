#change_mac 함수는 이 정보를 사용하여 실제로 MAC 주소를 변경합니다. 
#이를 위해 subprocess.run 함수를 사용하여 네 가지 주요 명령을 실행합니다.
#인터페이스를 비활성화(down), MAC 주소를 변경(hw ether), 인터페이스를 다시 활성화(up), 그리고 변경된 인터페이스 설정을 확인합니다.


import subprocess  # subprocess 모듈을 임포트하여 외부 명령 실행 기능을 사용할 수 있게 함
import argparse  # argparse 모듈을 임포트하여 명령줄 인자 파싱 기능을 사용할 수 있게 함

def change_mac(interface, new_mac):  # MAC 주소를 변경하는 함수 정의, interface와 new_mac 두 개의 인자를 받음
    print(f"[+] Changing MAC address for {interface} to {new_mac}")  # 변경할 인터페이스와 새 MAC 주소를 출력

    commands = [  # 실행할 명령어들을 리스트의 리스트 형태로 저장
        ["ifconfig", interface, "down"],  # 네트워크 인터페이스를 비활성화하는 명령어
        ["ifconfig", interface, "hw", "ether", new_mac],  # MAC 주소를 변경하는 명령어
        ["ifconfig", interface, "up"],  # 네트워크 인터페이스를 활성화하는 명령어
        ["ifconfig", interface]  # 변경된 설정을 확인하기 위해 인터페이스 정보를 출력하는 명령어
    ]

    for command in commands:  # commands 리스트에 저장된 명령어들을 순회하며
        subprocess.run(command)  # 각 명령어를 실행

parser = argparse.ArgumentParser(description='Change the MAC address of a network interface')  # 명령줄 인자를 파싱하기 위한 ArgumentParser 객체 생성
parser.add_argument("-i", "--interface", dest="interface", help="interface to change its MAC address", required=True)  # '-i' 또는 '--interface' 옵션 추가
parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address", required=True)  # '-m' 또는 '--mac' 옵션 추가

args = parser.parse_args()  # 명령줄 인자를 파싱하여 args에 저장

# interface = args.interface  # 사용자가 입력한 인터페이스 이름을 변수에 저장 (이 코드는 주석 처리됨)
# new_mac = args.new_mac  # 사용자가 입력한 새 MAC 주소를 변수에 저장 (이 코드는 주석 처리됨)
change_mac(args.interface, args.new_mac)  # change_mac 함수를 호출하여 MAC 주소 변경 작업을 실행
