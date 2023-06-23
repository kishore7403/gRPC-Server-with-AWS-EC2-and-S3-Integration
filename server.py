import grpc
from concurrent import futures
import computeandstorage_pb2 
import computeandstorage_pb2_grpc 
import boto3

class EC2OperationsServicer(computeandstorage_pb2_grpc.EC2OperationsServicer):
    def StoreData(self, request, context):
        client = boto3.client('s3')
        bucket_name = 'b00934548-bucket'
        key= 'data_file.txt'
        content=request.data
        client.put_object(Body=content,Bucket=bucket_name,Key=key)
        # url = client.generate_presigned_url('get_object', Params={'Bucket':bucket_name, 'Key': key})
        url="https://"+bucket_name+".s3.amazonaws.com/"+key
        return computeandstorage_pb2.StoreReply(s3uri=url)

    def AppendData(self, request, context):
        client = boto3.client('s3')   
        bucket_name = 'b00934548-bucket' 
        key= 'data_file.txt'
        new_data = request.data
        response=client.get_object(Bucket=bucket_name,Key=key)
        old_data=response['Body'].read().decode('utf-8')
        write_data=old_data+new_data
        client.put_object(Body=write_data,Bucket=bucket_name,Key=key)
        return computeandstorage_pb2.AppendReply()
    
    def DeleteFile(self, request, context):
        client = boto3.client('s3')   
        s3uri=request.s3uri
        bucket_start = s3uri.index("://") + 3
        bucket_end = s3uri.index(".s3.amazonaws.com")
        bucket_name = s3uri[bucket_start:bucket_end]
        key_start = s3uri.rindex("/") + 1
        key = s3uri[key_start:]
        client.delete_object(Bucket=bucket_name,Key=key)
        return computeandstorage_pb2.DeleteReply()

def serve():
    port='50051'
    server = grpc.server(futures.ThreadPoolExecutor())
    computeandstorage_pb2_grpc.add_EC2OperationsServicer_to_server(EC2OperationsServicer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()