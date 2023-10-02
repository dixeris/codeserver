# Bidirectional streaming gRPC server
# Reference: https://velotio.medium.com/implementing-grpc-in-python-a-step-by-step-guide-e9733871acb0

import grpc
from concurrent import futures

import serverstreaming_pb2
import serverstreaming_pb2_grpc

def make_message(message):
    return serverstreaming_pb2.Message(
        message=message
    )

class ServerStreamingService(serverstreaming_pb2_grpc.ServerStreamingServicer):

    def GetServerResponse(self, request, context):
        messages = []
        for i in range(1,request.value+1):            
            messages.append(make_message("message #%d" % i))        
        print('Server processing gRPC server-streaming {%d}.' % request.value)
        for message in messages:
            yield message

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    serverstreaming_pb2_grpc.add_ServerStreamingServicer_to_server(ServerStreamingService(), server)
    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()