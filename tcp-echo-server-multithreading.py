import socketserver
import threading 

class ThreadingTCPSocketHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('> client connected b IP address {0} with port {1}'.format(self.client_address[0],self.client_address[1]))
        while True:
            RecvData = self.request.recv(1024)
            cur_thread = threading.current_thread()
            print('echoed:', RecvData.decode('utf-8'), "by", cur_thread.name)
            self.request.sendall(RecvData)
            if RecvData.decode('utf-8') == 'quit':
                break



class ThreadingTCPServer(socketserver.ThreadingMixIn,socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65456
    print('> echo client is activated')
    server = ThreadingTCPServer((HOST,PORT), ThreadingTCPSocketHandler)
    with server:
        ip, port = server.server_address

        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        print("> server loop running in thread(main thread):", server_thread.name)

        baseThreadNumber = threading.active_count()
        while True:
            msg = input('> ')
            if msg == 'quit':
                if baseThreadNumber == threading.active_count():
                    print("> stop procedure started")
                    break
                else:
                    print("active threads are remained:", threading.active_count() - baseThreadNumber,"threads")

        print('> echo-client is deactivated')
        server.shutdown()
        
    
