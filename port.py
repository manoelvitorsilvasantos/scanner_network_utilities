#!/usr/bin/env python3

from sys import argv
import socket

#criar um soquete
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#função para escamento de porta
def scanner_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (host, port)
    result = sock.connect_ex(dest)
    if result == 0:
        print('%d | is OPEN' %(port))
    else:
        print('%d | is CLOSED' %(port))

host = argv[1] #argumento pega o host
port = int(argv[3]) #argumento pega a porta

if host == None and port == None:
    print('python3 ./port [target] -p [port]\n')
else:
    scanner_port(host, port)
    sock.close()


    
