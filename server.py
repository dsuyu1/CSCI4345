from socket import *

myIp = '192.168.1.2'
myPort = 5050
myAddr = (myIp, myPort)
returnmsg = "Your message has been received!"

# create a socket to listen
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind this socket to a port
serverSocket.bind(myAddr)

# clientList

clientList = set() # empty to start


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

    # add the client address to the list if it's not already there
    if clientAddr not in clientList:
        clientList.add(clientAddr)
        print("New client added: ", clientAddr)
        print("Current clients: ", clientList)
    

    for client in clientList: # broadcasting to everybody
        if client != clientAddr: # don't send it back to the sender
            serverSocket.sendto(decoded.encode(), client) # send the received message to all other clients

    
    # if the server receives "exit", then break the loop
    if decoded == 'exit':
        break
