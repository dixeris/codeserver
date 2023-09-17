import socketserver
import threading 

#{CHAT} create a list to store socket informations

group_queue = []

class ThreadingTCPSocketHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('> client connected b IP address {0} with port {1}'.format(self.client_address[0],self.client_address[1]))
        
        #{CHAT} import the global variable and register a new client conn informtaion into a client DB        
        global group_queue
        group_queue.append(self.request)

        while True:
            RecvData = self.request.recv(1024)            
            #{CHAT} Unregister a disconnected client from a client DB
            if RecvData.decode('utf-8') == 'quit':
                group_queue.remove(self.request)
                break
            #{CHAT} Forward a client message to whole clients (broadcast)
            else:                
                print('> received (', RecvData.decode('utf-8'), ') and echoed to ', len(group_queue), 'clients')                
                group_queue_without_myself = list(group_queue)
                group_queue_without_myself.remove(self.request)
                for conn in group_queue_without_myself:
                    conn.sendall(RecvData)

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
        
    
