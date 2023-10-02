import zmq
from random import randrange

print("Publishing weather updates")

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    zipcode = randrange(1,100000)
    temperature = randrange(-80,135)
    relhubidity = randrange(10,60)


    socket.send_string(f"{zipcode} {temperature} {relhubidity}")

