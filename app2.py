# Project: App2 - Project Diamond
# Purpose Details: Receive a JSON payload from App 1 through TLS, hashes the
#payload and append it to a message to then send through SFTP.
# Course: IST 411
# Author: Team 3
# Date Developed: 11/18/2019
# Last Date Changed: 11/18/2019

import hashlib
import hmac
import socket
import ssl
import pysftp
import sys
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


# Description: Receives the payload through TLS from App1, hashes the payload and then places it in a secure server through STFP for App 3 to recieve.
# Param: None
# Returns: None
def payloadFromApp1():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    cinfo = {'cnopts': cnopts, 'host': 'oz-ist-linux-oakes', 'username': 'ftpuser', 'password': 'test1234', 'port': 100}

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

            key = "5411"
            key = bytes(key, 'UTF-8')
            strJson = hmac.new(key, message, hashlib.sha256).hexdigest()
            print("Message has been hashed")
            logging.info('Message has been encoded')
            print(strJson)
            with pysftp.Connection(**cinfo) as sftp:
                print("Connection made")
                print("Sending jsonPayload.json file")
                sftp.put('jsonPayload.json')
                logging.info('Message has been sent to app3')

    except Exception as e:
        print(e)
        ssl_sock.close()
        print("Log exception: ", sys.exc_info()[0])
        logging.error('DEBUG: Exception has been thrown')


try:
    payloadFromApp1()

except Exception as e:
    print(e)
    logging.error('DEBUG: Exception has been thrown')

