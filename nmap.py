"""
nmap -p 1-200 192.168.33.15
Scans ports from 1 to 200 on the target IP address to check for open ports.

nmap -p 80 192.168.33.15
Scans only port 80 (HTTP) on the target IP address.

nmap -F 192.168.33.15
Performs a fast scan on the target IP by scanning fewer ports (default list of common ports).

nmap -p - 192.168.33.15
Scans all 65,535 ports on the target IP.

nmap -sT 192.168.33.15
Performs a TCP connect scan on the target IP to detect open TCP ports.

nmap -sU 192.168.33.15
Performs a UDP scan on the target IP to detect open UDP ports.

nmap -A 192.168.33.15
Enables OS detection, version detection, script scanning, and traceroute on the target.

For subnet scan
nmap  192.168.1.100/24
Scans all devices within the given subnet (e.g., 192.168.1.0/24 scans IPs 192.168.1.1 to 192.168.1.255).

"""