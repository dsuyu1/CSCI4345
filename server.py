from socket import *

myIp = '127.0.0.1'
myPort = 8888
myAddr = (myIp, myPort)

# create a socket to listen
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind this socket to a port
serverSocket.bind(myAddr)

print(serverSocket)

# receive some message
received = serverSocket.recvfrom(2048)

# display the message we received
print(received)