import socket

HOST = '127.0.0.1'
PORT = 65456

def main():

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as clientsocket:
        try:
            if clientsocket.connect((HOST,PORT)) == -1:
                print('connect() failed and program terminated')
                clientsocket.close()
                return
        except Exception as exceptionObj:
            #Exception handling in case of binding function has error 
            print('connect() failed by eception:', exceptionObj)
            clientsocket.close()
            return
  
        while True:
            sendmsg = input("> ")
            clientsocket.sendall(bytes(sendmsg,'utf-8'))
            Recvdata = clientsocket.recv(1024)
            print('> echoed: ', Recvdata.decode('utf-8'))
            if sendmsg == 'quit':
                break

if __name__ == "__main__":
    print('> echo client is activated')
    main()
    print('> echo-client is deactivated')

