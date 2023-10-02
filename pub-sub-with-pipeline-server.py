import zmq
def main():
    ctx = zmq.Context()
    publisher = ctx.socket(zmq.PUB)
    publisher.bind("tcp://*:5557")
    collector = ctx.socket(zmq.PULL)
    collector.bind("tcp://*:5558")
    
    while True:
        msg = collector.recv()
        print("server: publishing updates >> ", msg)
        publisher.send(msg)


if __name__ == '__main__':
    main()


    