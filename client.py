from socket import *

# Pre-requisites
    # we need some info
serverIP = '127.0.0.1'
serverPort = 8888
serverAddr = (serverIP, serverPort)

# my own information (not required)
# myIP = '127.0.0.1'
# myPort = 7777


# 1. Take in a message to send
msg = input('Please enter a message to send: ')

# 2. Encode the message (prepare the message for transfer)
encoded = msg.encode()

print(encoded)

# 3. Send it to someone
    # Create a socket to enable sending/receiving
mySocket = socket(AF_INET, SOCK_DGRAM)

mySocket.sendto(encoded, serverAddr)

# receive a response from the server
    # hint: you need the recvfrom() method

