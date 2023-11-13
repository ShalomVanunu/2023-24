from scapy.all import *
from scapy.layers.inet import *


def show_IP(packet):
    print(packet[IP].dst)


def main():
    sniff(filter="ip", prn=show_IP)

if __name__ == "__main__":
    main()


