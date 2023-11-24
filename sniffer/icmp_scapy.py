# pip install scapy

from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(ICMP):
        print(packet.show())

if __name__ == "__main__":
    sniff(prn=packet_callback, filter="icmp", store=0)

