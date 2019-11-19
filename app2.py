# Project: App2 - Project Diamond
# Purpose Details: Receive a JSON payload from App 1 through TLS, hashes the
#payload and append it to a message to then send through SFTP.
# Course: IST 411
# Author: Team 3
# Date Developed: 11/18/2019
# Last Date Changed: 11/18/2019

import socket
import ssl
import pysftp
import hashlib
import sys
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


# logging('App2 has begun')

# Description: Receives the payload through TLS from App1.
# Param: None
# Returns: None
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
            message = c_ssl.recv(157778)

            print("Message received: ", message)

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
        from app1 import jsonList
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
            print("Sending jsonPayload.json file")
            sftp.put('jsonPayload.json')

    except Exception as e:
        print(e)
        print("Log exception 1:", sys.exc_info()[0])


try:
    payloadFromApp1()
    sftpSender()
    hmacHasher()


except Exception as e:
    print(e)

# logging ('App2 has ended')

