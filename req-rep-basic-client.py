import zmq 

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")

for request in range(10):
    print("sending request %s" % request)
    socket.send(b"hello")

    message = socket.recv()
    print("Recevied reply %s [ %s ]" % (request, message))