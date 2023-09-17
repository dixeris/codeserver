import socketserver
import threading

group_queue = []

class MyUDPHandler(socketserver.BaseRequestHandler):
    #self.request consists of a pair of data and client socket

    def handle(self):
        RecvData = self.request[0].strip()
        RecvSocket = self.request[1]

        RecvCmd = RecvData.decode('utf-8')
        #{CHAT} cmd line protocol to client registration and deregis 
        if RecvCmd[0] == "#" or RecvCmd == "quit":
            if RecvCmd == "#REG":
                print("> client resgistered", self.client_address)                               
                group_queue.append(self.client_address)
            elif RecvCmd == "#DEREG" or RecvCmd == "quit":
                if group_queue.__contains__(self.client_address) == True:
                    print("> client de-registered", self.client_address)
                    group_queue.remove(self.client_address)
        else:
            #{CHAT} prohibit an un-registered client mesage
            if len(group_queue) == 0:
                print("no clients to echo")
            elif group_queue.__contains__(self.client_address) == False:
                print('> ignores a message from un-registerd client')
            else:
                #{CHAT} FOrward a client mesage to whole clients 
                print ('> received (', RecvData.decode('utf-8'), ') and echoed to', len(group_queue), 'clients')
                for clientConn in group_queue:
                    RecvSocket.sendto(RecvData, clientConn)
            
if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65456
    print('> echo server activated')
    with socketserver.UDPServer((HOST,PORT), MyUDPHandler) as server:
        server.serve_forever()
    print('> ehco-server is de-activated')

    


        
            
