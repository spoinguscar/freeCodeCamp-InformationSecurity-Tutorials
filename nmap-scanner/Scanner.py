#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool.")
print("-----------------------------------------------")

ip_addr = input('Please enter the IP address you want to scan: ')
print(f"The IP you entered is {ip_addr}")
type(ip_addr)

resp = input("""
Please enter the type of scan you want to run
1) SYN ACK Scan
2) UDP Scan
3) Comprehensive Scan
""")

print(f"You have selected option {resp}")

print(f"Nmap Version: {scanner.nmap_version()}")

if resp == "1":
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print(f"IP Status: {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open Ports: {scanner[ip_addr]['tcp'].keys()}")
elif resp == "2":
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print(f"IP Status: {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open Ports: {scanner[ip_addr]['udp'].keys()}")
elif resp == "3":
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print(f"IP Status: {scanner[ip_addr].state()}")
    print(scanner[ip_addr].all_protocols())
    print(f"Open Ports: {scanner[ip_addr]['tcp'].keys()}")
else:
    print("Invalid option")