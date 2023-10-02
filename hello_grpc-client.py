import grpc
import hello_grpc_pb2
import hello_grpc_pb2_grpc


channel = grpc.insecure_channel("localhost:50051")

stub = hello_grpc_pb2_grpc.MyServiceStub(channel)

request = hello_grpc_pb2.MyNumber(value=4)

response = stub.MyFunction(request)

print("gRPC response:", response.value)
