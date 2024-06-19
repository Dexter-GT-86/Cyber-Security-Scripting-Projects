Cyber Security Scripting Projects

This project contains a series of cybersecurity scripts designed to demonstrate various network attack techniques using Python and the Scapy library. The scripts include tasks such as packet manipulation, session hijacking, Man-in-the-Middle (MITM) attacks, and DNS spoofing.

Project Structure

	•	q1.py: Script for sending a TCP reset packet.
	•	q3.py: Script for session hijacking by sending a packet to create a directory on the victim’s system.
	•	q4.py: Script for session hijacking by sending a packet to initiate a reverse shell connection.
	•	q5-reverse-shell.py: Script for session hijacking to execute a reverse shell.
	•	q5-session-hijacking.py: Script for session hijacking to execute a command on the victim’s system.
	•	q6-mitm.py: Script for performing a Man-in-the-Middle (MITM) attack.
	•	q6-spoof.py: Script for DNS spoofing.

Getting Started

Prerequisites

	•	Python 3.x
	•	Scapy library

Script Descriptions

q1.py

This script sends a TCP reset packet to terminate an existing TCP connection. It demonstrates basic packet crafting using Scapy.

q3.py

This script performs session hijacking by injecting a packet into an existing TCP session to create a directory on the victim’s system.

q4.py

This script performs session hijacking by injecting a packet to initiate a reverse shell connection from the victim’s system to the attacker’s system.

q5-reverse-shell.py

This script is similar to q4.py but focuses on executing a reverse shell on the victim’s system through session hijacking.

q5-session-hijacking.py

This script performs session hijacking by injecting a packet to execute a specific command on the victim’s system.

q6-mitm.py

This script sets up a Man-in-the-Middle (MITM) attack by poisoning the ARP cache of both the victim and the gateway, enabling the attacker to intercept and modify network traffic.

q6-spoof.py

This script performs DNS spoofing by intercepting DNS query packets and responding with a spoofed DNS response, redirecting the victim to a malicious IP address.

Disclaimer

These scripts are for educational purposes only. Unauthorized use of these scripts on networks or systems without permission is illegal and unethical. Use them responsibly and only on systems and networks you own or have explicit permission to test.

License

This project is licensed under the MIT License. See the LICENSE file for details.
