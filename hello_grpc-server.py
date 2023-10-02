import grpc
from concurrent import futures 
#gRPC는 기본적으로 비동기식이므로 기계적으로 futures 를 import 한다. 
import hello_grpc_pb2
import hello_grpc_pb2_grpc

import hello_grpc

class MyServiceServicer(hello_grpc_pb2_grpc.MyServiceServicer):
    def MyFunction(self, request, context):
        response = hello_grpc_pb2.MyNumber()
        response.value = hello_grpc.my_func(request.value)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

hello_grpc_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(),server)
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# (9) grpc.server가 유지되도록 프로그램 실행을 유지함
try:
    server.wait_for_termination()
except KeyboardInterrupt:
    server.stop(0)

    

