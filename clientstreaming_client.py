import grpc
import clientstreaming_pb2
import clientstreaming_pb2_grpc

def make_message(message):
    return clientstreaming_pb2.Message ( message = message ) 
    
    
def generate_message():
    messages = [
        make_message("message #1"),
        make_message("message #2"),
        make_message("message #3"),
        make_message("message #4"),
        make_message("message #5")
    ]
    for a in messages:
        print('[client to server] %s' % a.message)
        yield a
    

def send_message(stub):
    response = stub.GetServerResponse(generate_message())
    print('[server to client] %d' % response.value)

    

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = clientstreaming_pb2_grpc.ClientStreamStub(channel)
        send_message(stub)


if __name__ == "__main__":
    run()