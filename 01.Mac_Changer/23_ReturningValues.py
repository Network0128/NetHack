#get_arguments 함수는 사용자로부터 네트워크 인터페이스의 이름과 변경할 새로운 MAC 주소를 명령줄 인자로 받기 위해 argparse 모듈을 사용합니다. 
#명령줄 인터페이스를 설정하고, "-i" 또는 "--interface" 인자로 인터페이스 이름을, "-m" 또는 "--mac" 인자로 새 MAC 주소를 필수적으로 입력받도록 합니다. 
#입력된 인자들은 파싱 후 반환되어, MAC 주소 변경을 위해 사용됩니다.

import subprocess
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(description='Change the MAC address of a network interface')  # MAC 주소를 변경하기 위한 명령줄 인터페이스 설정
    parser.add_argument("-i", "--interface", dest="interface", help="interface to change its MAC address",required=True)  # 인터페이스 이름을 지정하는 필수 명령줄 인자 추가
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address", required=True)  # 새 MAC 주소를 지정하는 필수 명령줄 인자 추가
    return parser.parse_args()  # 파싱한 인자들을 반환


def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    commands = [
        ["ifconfig", interface, "down"],
        ["ifconfig", interface, "hw", "ether", new_mac],
        ["ifconfig", interface, "up"],
        ["ifconfig", interface]
    ]
    for command in commands:
        subprocess.run(command)


args = get_arguments()
change_mac(args.interface, args.new_mac)
