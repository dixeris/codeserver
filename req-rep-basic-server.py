import time 
import zmq 

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    msg = socket.recv()
    print("recevied request: %s" % msg)
    time.sleep(1)
    socket.send(b"World")
