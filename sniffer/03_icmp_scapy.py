from scapy.all import * # pip install scapy

def packet_callback(packet):
    if packet.haslayer(ICMP):
        print(packet.show())

if __name__ == "__main__":
    sniff(prn=packet_callback, filter="icmp", store=0)

