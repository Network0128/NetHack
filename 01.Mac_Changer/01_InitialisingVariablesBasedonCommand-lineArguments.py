#사용자가 지정한 주소로 네트워크 인터페이스의 MAC 주소를 변경하는 스크립트입니다. 
#사용자는 명령줄 인자를 통해 인터페이스 이름과 새로운 MAC 주소를 지정할 수 있습니다. 
#subprocess 모듈을 사용하여 시스템 명령어(ifconfig)를 실행하며, argparse 모듈로 명령줄 인자를 처리합니다.
#스크립트는 먼저 argparse를 사용하여 사용자로부터 인터페이스 이름과 새 MAC 주소를 입력받습니다. 
#이 정보는 명령줄 인자 -i 또는 --interface와 -m 또는 --mac을 통해 제공됩니다. 이러한 인자들은 스크립트에 필수적으로 필요하기 때문에 required=True로 설정되어 있습니다.
#-----------------------------------------------------------------------------
#"파싱(parsing)"은 자연어, 컴퓨터 언어 또는 데이터 구조의 텍스트를 분석하여 의미와 구조를 이해하기 위해 의미있는 구성 요소로 분해하는 과정을 의미합니다.
#프로그래밍에서는 주로 입력된 데이터나 파일, 커맨드라인 인자 등을 읽고 그 구조를 이해하여 프로그램이 사용할 수 있는 형태로 변환하는 작업을 가리킵니다. 
#예를 들어, 파이썬에서 argparse 모듈을 사용하여 커맨드라인 인자를 파싱할 때, 사용자가 입력한 인자들은 각각 식별되고, 각 인자의 특정 값을 프로그램 내에서 사용할 수 있도록 변환됩니다. 
#이를 통해 프로그램은 다양한 입력에 대응하여 적절한 동작을 수행할 수 있습니다.

import subprocess  # subprocess 모듈을 임포트합니다.
import argparse  # argparse 모듈을 임포트합니다.

parser = argparse.ArgumentParser(description='Change the MAC address of a network interface')  # 인자 파서 객체를 생성합니다.

parser.add_argument("-i", "--interface", dest="interface", help="interface to change its MAC address", required=True)  # 인터페이스 인자를 추가합니다.
parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address", required=True)  # MAC 주소 인자를 추가합니다.

args = parser.parse_args()  # 커맨드라인 인자를 파싱합니다.

interface = args.interface  # 파싱된 인터페이스 값을 변수에 할당합니다.
new_mac = args.new_mac  # 파싱된 MAC 주소 값을 변수에 할당합니다.

print(f"Changing MAC address for {interface} to {new_mac}")  # MAC 주소 변경 작업 시작을 알립니다.

commands = [
    ["ifconfig", interface, "down"],  # 인터페이스를 비활성화하는 커맨드입니다.
    ["ifconfig", interface, "hw", "ether", new_mac],  # MAC 주소를 변경하는 커맨드입니다.
    ["ifconfig", interface, "up"],  # 인터페이스를 활성화하는 커맨드입니다.
    ["ifconfig", interface]  # 인터페이스 설정을 확인하는 커맨드입니다.
]

for command in commands:  # 모든 커맨드를 반복 실행합니다.
    subprocess.run(command)  # 각 커맨드를 실행합니다.


