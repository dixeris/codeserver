import sys
import threading
import time
import zmq
from random import randint, random

class ServerTask(threading.Thread):
    def __init__(self,num_server):
        threading.Thread.__init__(self)
        self.num_server = num_server


    def run(self):
        context = zmq.Context()
        
        frontend = context.socket(zmq.ROUTER)
        frontend.bind("tcp://*:5570")

        backend = context.socket(zmq.DEALER)
        backend.bind("inproc://backend")

        workers = []
        for i in range(self.num_server):
            worker = ServerWorker(context, i)
            worker.start()
            workers.append(worker)

        zmq.proxy(frontend,backend)
        
        frontend.close()
        backend.close()
        context.term()


class ServerWorker(threading.Thread):
    def __init__(self,context,id):
        threading.Thread.__init__(self)
        self.context = context
        self.id = id

    def run(self):
        worker = self.context.socket(zmq.DEALER)
        worker.connect("inproc://backend")
        print("Worker#{0} started".format(self.id))

        while True:
            ident, msg = worker.recv_multipart()
            print("Worker#{0} received {1} from {2}".format(self.id,msg,ident))
            worker.send_multipart([ident,msg])

        worker.close()

def main(argv):
    server = ServerTask(int(argv[1]))
    server.start()
    server.join()

if __name__== "__main__":
    main(sys.argv)


