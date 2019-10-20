import socket
import ssl
import json
import logging

# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# logging('App2 has begun')

def getLoggingForApp2(): 
  try:
    print("create an INET, STREAMing socket using SSL")
    diamondSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(diamondSock,
                               server_side=True,
                               certfile="server.crt",
                               keyfile="server.key")
    print("bind the socket to a public host, and a well-known port 8080")
    ssl_sock.bind(('localhost', 8080))
    ssl_sock.listen(5)
    print("ciphers: " + str(ssl_sock.cipher()))
    while True:
        print("accept connections from outside")
        (clientsocket, address) = ssl_sock.accept()

        message = clientsocket.recv(1024)
        print("Message received")
        print(message)

        logging.info('Message has been recieved by app2')
        strJson = message.decode("utf-8")
        print(strJson)

except Exception as e:
    print(e)
    ssl_sock.close()

# logging.info('App2 has ended')
