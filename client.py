from socket import *

# Pre-requisites
    # we need some info
serverIP = '192.168.1.2'
serverPort = 5050
serverAddr = (serverIP, serverPort)

# my own information (not required)
# myIP = '127.0.0.1'
# myPort = 7777


# 1. Take in a message to send
msg = input('Please enter a message to send: ')

# 2. Encode the message (prepare the message for transfer)
encoded = msg.encode()

# 3. Send it to someone
    # Create a socket to enable sending/receiving
mySocket = socket(AF_INET, SOCK_DGRAM)

mySocket.sendto(encoded, serverAddr)

# receive a response from the server
    # hint: you need the recvfrom() method
returnmsg, serverAddress = mySocket.recvfrom(2048)

# print the response from the server back to the console
print("The server says: ", returnmsg.decode())