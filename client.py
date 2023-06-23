import grpc
from computeandstorage_pb2 import StoreRequest, AppendRequest, DeleteRequest
import computeandstorage_pb2_grpc

def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = computeandstorage_pb2_grpc.EC2OperationsStub(channel)

    value=1
    while value==1:
        n=int(input())
        if n==1:
            data = b"new"
            request = StoreRequest(data=data)
            response = stub.StoreData(request)
        if n==2:
            data = b"append"
            request = AppendRequest(data=data)
            response= stub.AppendData(request)
        if n==3:
            s3uri= b"https://b00934548.s3.amazonaws.com/data_file.txt"
            request = DeleteRequest(s3uri=s3uri)
            response= stub.DeleteFile(request)

if __name__ == '__main__':
    run_client()