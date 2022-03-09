import socket
host = input('target >> ')
inicio = int(input('port inicio >> '))
final = int(input('port final >> '))
port = inicio
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msg = 'send with sucess'
for i in range(inicio, final):
    dest = (host, i)
    try:
       tcp.connect(dest)
       tcp.send('teste')
    except ValueError:
        print('Port %d is closed'  %(i)) 

tcp.close()
