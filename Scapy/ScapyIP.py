#https://youtu.be/WMmVheaE0xE
#https://github.com/shrestha-tripathi/offensive-python/blob/master/packet_sniffer.py


import scapy.all as scapy
from scapy.layers import http



def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)
        print(packet[http.HTTPRequest].Host.decode("utf-8"))
        #print("[+] Http Request >> " + packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path)


scapy.sniff(store=False, prn=process_packet)