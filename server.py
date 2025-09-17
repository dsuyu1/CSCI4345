from socket import *

myIp = '127.0.0.1'
myPort = 8888
myAddr = (myIp, myPort)
returnmsg = "Your message has been received!"

# create a socket to listen
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind this socket to a port
serverSocket.bind(myAddr)

# keep receiving 
while(True):
# receive some message
    received, clientAddr = serverSocket.recvfrom(2048)

# decode and display the message we received
    decoded = received.decode()
    print(decoded)

    # Return a message to the client
        # message and the client address
        # hint: use the sendto() method
    serverSocket.sendto(returnmsg.encode(), clientAddr) # sends the returnmsg encoded back to the client address

    # if the server receives "exit", then break the loop
    if decoded == 'exit':
        break
