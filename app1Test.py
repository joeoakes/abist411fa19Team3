# Project: App1 Test - Project Diamond
# Purpose Details: Testing if App 1 complies and runs.
# Course: IST 411
# Author: Cieara Parker
# Date Developed: 11/18/2019
# Last Date Changed: 11/20/2019

import socket

import ssl
import time
import unittest


class TestApp1(unittest.TestCase):


    def test_sample(self):

        print("Client connecting on port 8080 using SSL")
        diamondSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c_ssl = ssl.wrap_socket(diamondSock,
                                ca_certs="server.crt",
                                cert_reqs=ssl.CERT_REQUIRED)
        c_ssl.connect(('localhost', 8080))
        c_ssl.send(JsonPayload)
        logging.info('Object sent to Application 2')



if __name__ == '__main__':
    unittest.main(TestApp1)

