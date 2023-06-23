# gRPC Server with AWS EC2 and S3 Integration

This project is a gRPC server that integrates with AWS EC2 and S3 services. It provides methods for storing, appending, and deleting files on S3 using AWS libraries. The server can be deployed on an EC2 instance and communicates with client applications over gRPC.

When finished the system will look and function like this:

![Annotation 2023-06-23 120407](https://github.com/kishore7403/gRPC-Server-with-AWS-EC2-and-S3-Integration/assets/48860055/e55c2cac-ee5a-48fd-9f61-7b50f68107bb)

## Installation

1. Clone the repository:


2. Change to the project directory:


3. Install the dependencies:

- Python:

  ```
  pip install -r requirements.txt
  ```

- Node.js:

  ```
  npm install
  ```

4. Configure AWS credentials:

Set up your AWS credentials by either providing the access key and secret access key directly or using the AWS CLI `aws configure` command.

5. Deploy the gRPC server on an EC2 instance:

- Launch an EC2 instance on AWS with the desired configuration.
- Obtain the IPv4 address of the EC2 instance.
- Update the gRPC server code with the EC2 instance's IP address and port.

6. Start the gRPC server:

- Python:

  ```
  python server.py
  ```

- Node.js:

  ```
  node server.js
  ```

7. Update the client code:

- Modify the client code to connect to the gRPC server using the EC2 instance's IP address and port.
- Run the client application to interact with the gRPC server.

## Usage

1. Run the client application to initiate the interaction with the gRPC server.
2. The client application sends requests to the gRPC server for storing data, appending data, or deleting files on AWS S3.
3. The gRPC server communicates with AWS EC2 and S3 services to perform the requested operations.
4. The client application receives responses from the gRPC server and performs necessary validations.
5. Test each step of the interaction process, including storing data, appending data, and deleting files.
6. Customize and extend the gRPC server and client code as per your requirements.

## API Reference

The gRPC server provides the following methods:

- `StoreData`: Stores the provided data in a file on AWS S3 and returns the publicly readable URL of the created file.

- `AppendData`: Appends the provided data to the existing file on AWS S3.

- `DeleteFile`: Deletes the specified file from AWS S3.

Refer to the `computeandstorage.proto` file for the request and response message formats for each method.

## Testing

To test the integration of your gRPC server with the provided client application, follow these steps:

1. Deploy the gRPC server on an EC2 instance, ensuring it is accessible from the internet.

2. Obtain the IPv4 address of the EC2 instance.

3. Update the client application's code to make requests to the gRPC server's methods using the appropriate IP address and port.

4. Start the client application and initiate the interaction with the gRPC server.

5. Verify that the client application successfully interacts with the gRPC server by checking the responses and performing necessary validations.

6. Test each step of the interaction process, including storing data, appending data, and deleting the file.

## Deployment

To deploy the gRPC server on an AWS EC2 instance:

1. Create an EC2 instance using the desired configuration, ensuring it has the necessary access to AWS S3.

2. Configure security groups and network settings to allow incoming connections to the gRPC
