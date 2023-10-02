import grpc

import clientstreaming_pb2
import clientstreaming_pb2_grpc

from concurrent import futures

class ClientStreamServicer(clientstreaming_pb2_grpc.ClientStreamServicer):
    def GetServerResponse(self, request_iterator, context):
        print ('server processing gRPC client-streaming')
        count = 0
        for message in request_iterator:
            count += 1
        return clientstreaming_pb2.Number(value=count)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    clientstreaming_pb2_grpc.add_ClientStreamServicer_to_server(ClientStreamServicer(), server)
    print('Starting server')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
