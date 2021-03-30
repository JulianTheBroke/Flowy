import time
import socket

print('RUN: main.py')

IP = "192.168.137.175"
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, 1234))
s.listen(5)
print('listening')

clientsocket = ""

while True:
    if not clientsocket:
        clientsocket, address = s.accept()
        print('connection established')
    try:
        msg = clientsocket.recv(1024)
        msg.decode('utf-8')
        print(msg)
    except Exception:
        clientsocket, address = s.accept()
        print('connection established')        
        msg = clientsocket.recv(1024)
        msg.decode('utf-8')
        print(msg)

    msgi = int(msg)
    if msgi <= 10:
        clientsocket.send(bytes('green', 'utf-8'))
    elif msgi <= 15:
        clientsocket.send(bytes('orange', 'utf-8'))
    elif msgi <= 20:
        clientsocket.send(bytes('red', 'utf-8'))

print('DONE??')