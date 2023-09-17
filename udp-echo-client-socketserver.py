import socket
import threading

HOST = '127.0.0.1'
PORT = 65456

def recvHandler(clientSocket):
    while True:
        recvData = clientSocket.recv(1024)
        print('> recevied:', recvData.decode('utf-8'))
        if recvData.decode('utf-8') == "quit":
            break 

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as clientSocket:
        clientThread = threading.Thread(target=recvHandler, args=(clientSocket,))
        clientThread.daemon = True
        clientThread.start()

        while True:
            sendmsg = input('> ')
            clientSocket.sendto(bytes(sendmsg, 'utf-8'), (HOST, PORT))
            if sendmsg == "quit":
                break 

if __name__ == "__main__":
    print('> echo-client activated')
    main()
    print('> echo-server deactivated')
