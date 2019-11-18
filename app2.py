import socket
import ssl
import logging
import pysftp
import hashlib
import sys

# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# logging('App2 has begun')

# Description: Receives the payload through TLS from App1.
# Param: None
# Returns: None
from app1 import jsonList


def payloadFromApp1():
    try:
        print("create an INET, STREAMing socket using SSL")
        diamondSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(diamondSock,
                                   server_side=True,
                                   ssl_version=ssl.PROTOCOL_TLSv1,
                                   certfile="server.crt",
                                   keyfile="server.key")
        print("bind the socket to a public host, and a well-known port 8080")
        ssl_sock.bind(('localhost', 8080))
        ssl_sock.listen(5)
        print("ciphers: " + str(ssl_sock.cipher()))
        while True:
            print("accept connections from outside")
            (c_ssl, address) = ssl_sock.accept()
            message = c_ssl.recv(1024)

            print("Message received")
            print(message)

            logging.info('Message has been received by app2')

            strJson = message.decode("utf-8")
            print(strJson)

    except Exception as e:
        print(e)
        ssl_sock.close()


# Description: Takes the payload and hashes it, appending it to a message.
# Param: None
# Returns: None

def hmacHasher():
    try:
        data = jsonList
        checksum = hashlib.sha256(data.encode()).hexdigest()
        print("Message has been hashed")
    except Exception as e:
        print(e)
        print("Log exception: ", sys.exc_info()[0])


# Description: Sends the payload to a server through SFTP for App3 to receive. 
# Param: None
# Returns: None

def sftpSender():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    cinfo = {'cnopts': cnopts, 'host': 'oz-ist-linux-oakes', 'username': 'ftpuser', 'password': 'test1234', 'port': 100}

    try:
        with pysftp.Connection(**cinfo) as sftp:
            print("Connection made")
            try:
                print("Sending jsonPayload.json file")
                sftp.put('jsonPayload.json')
            except Exception as e:
                print(e)
                print("Log exception 1:", sys.exc_info()[0])
    except Exception as e:
        print(e)
        print("Log exception 2:", sys.exc_info()[0])


try:

    payloadFromApp1()
    hmacHasher()
    sftpSender()

except Exception as e:
    print(e)

# logging ('App2 has ended')

