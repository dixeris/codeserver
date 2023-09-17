#!/bin/python3
import socket

HOST = '127.0.0.1'
PORT = 65456
print('> echo-server is activated')

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as serversocket:
    serversocket.bind((HOST,PORT))
    serversocket.listen()
    clientSocket, clientAddress = serversocket.accept()
    with clientSocket:
        print('> client connected b IP address {0} with port {1}'.format(clientAddress[0],clientAddress[1]))
        while True:
            RecvData = clientSocket.recv(1024)
            print('echoed:', RecvData.decode('utf-8'))
            clientSocket.sendall(RecvData)
            if RecvData.decode('utf-8') == 'quit':
                break

print('>echo-server is de-activated')

