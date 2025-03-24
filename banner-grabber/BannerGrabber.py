#!/usr/bin/python3

import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(str(s.recv(1024)).strip('b'))

def main():
    ip = input("Enter IP address: ")
    port = str(input("Enter port: "))
    banner(ip, port)
