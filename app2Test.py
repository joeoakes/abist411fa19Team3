# Project: App2 Test - Project Diamond
# Purpose Details: Testing if App 2 complies and runs.
# Course: IST 411
# Author: Cieara Parker
# Date Developed: 11/18/2019
# Last Date Changed: 11/20/2019

import socket
import ssl
import pysftp
import hashlib
import hmac
import sys
import logging
import unittest




class TestApp2(unittest.TestCase):

    def test_sample(self):
        
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
            ssl_sock.close()

  
     def test2_sample(self):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        cinfo = {'cnopts': cnopts, 'host': 'oz-ist-linux-oakes', 'username': 'ftpuser', 'password': 'test1234',
                 'port': 100}

            with pysftp.Connection(**cinfo) as sftp:
                print("Connection made")
                print("Sending jsonPayload.json file")
                sftp.put('jsonPayload.json')
  

 


if __name__ == '__main__':
    unittest.main(TestApp2)

