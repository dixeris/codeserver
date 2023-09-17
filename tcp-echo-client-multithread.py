import socket
import threading

HOST = '127.0.0.1'
PORT = 65456

def recvHandler(clientSocket):
    while True:
        recvData = clientSocket.recv(1024)
        print('> received:', recvData.decode('utf-8'))
        if recvData.decode('utf-8') == 'quit':
            break


        
def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as clientSocket:
        try:
            if clientSocket.connect((HOST,PORT)) == -1:
                print('connect() failed and program terminated')
                clientSocket.close()
                return
        except Exception as exceptionObj:
            #Exception handling in case of binding function has error 
            print('connect() failed by eception:', exceptionObj)
            clientSocket.close()
            return
        clientThread = threading.Thread(target=recvHandler, args=(clientSocket,))
        clientThread.daemon = True
        clientThread.start()

        while True:
            sendmsg = input("> ")
            clientSocket.sendall(bytes(sendmsg,'utf-8'))         
            if sendmsg == 'quit':
                break


if __name__ == "__main__":
    print('> activated')
    main()
    print('> deactivated')

