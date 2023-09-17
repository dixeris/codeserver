import socket

HOST = '127.0.0.1'
PORT = 65456

def main():

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as serversocket:
        try:
            if serversocket.bind((HOST,PORT)) == -1:
                print('bind() failed and program terminated')
                serversocket.close()
                return
        except Exception as exceptionObj:
            #Exception handling in case of binding function has error 
            print('bind() failed by eception:', exceptionObj)
            serversocket.close()
            return
        
        if serversocket.listen() == -1:
            print('> listen() has error')
            return
                
        clientSocket, clientAddress = serversocket.accept()

    with clientSocket:
        print('> client connected b IP address {0} with port {1}'.format(clientAddress[0],clientAddress[1]))
        while True:
            RecvData = clientSocket.recv(1024)
            print('echoed:', RecvData.decode('utf-8'))
            clientSocket.sendall(RecvData)
            if RecvData.decode('utf-8') == 'quit':
                break

if __name__ == "__main__":
    print('> echo server is activated')
    main()
    print('> echo-server is deactivated')

