3# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('172.26.58.207', port)) # 127.0.0.1 means that we are connecting to server running on same computer
#if want to connect to server running on different computer then use IP of the computer running server and PORT on which it is serving

# receive data from the server
print s.recv(1024)
# close the connection
s.close()
