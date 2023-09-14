import socket

HOST = '127.0.0.1'
PORT = 65456
print('> echo-server is activated')

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as clientsocket:
    clientsocket.connect((HOST,PORT))
    while True:
            sendmsg = input("> ")
            clientsocket.sendall(bytes(sendmsg,'utf-8'))
            Recvdata = clientsocket.recv(1024)
            print('> echoed: ', Recvdata.decode('utf-8'))
            if sendmsg == 'quit':
                break

print('>echo-client is de-activated')

