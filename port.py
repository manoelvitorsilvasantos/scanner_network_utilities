import socket
import time
import sys


def scanner_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (host, port)
    result = sock.connect_ex(dest)
    if result == 0:
        print('%d OPEN ' %(port))
    else:
        print('%d CLOSED ' %(port))
    sock.close()
def full_scanner_port(host, port_start, port_end):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = port_start
    while port < port_end:
        dest = (host, port)
        result = sock.connect_ex(dest)
        if result == 0:
            print('%d OPEN ' %(port))
        else:
            print('%d CLOSED ' %(port))
        port += 1


    
