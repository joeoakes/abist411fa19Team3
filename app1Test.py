# Project: App1 Test - Project Diamond
# Purpose Details: Testing if App 2 complies and runs.
# Course: IST 411
# Author: Cieara Parker
# Date Developed: 11/18/2019
# Last Date Changed: 11/20/2019

import socket
import json
import urllib.request
import ssl
import time
import logging
import unittest


logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


class TestApp1(unittest.TestCase):

    def timeInSeconds():
        times = time.time()
        return times

    def formatDate(self, timeInTuple):
        formatted = time.strftime("%Y-%m-%d %H:%M:%S", timeInTuple())
        return formatted

    def timeInTuple():
        tuple = time.gmtime()
        return tuple

    url = 'https://jsonplaceholder.typicode.com'
    param = '/post/1/comments'

    try:
        print('Url: ', url + param)
        response = urllib.request.urlopen(url + param)
        JsonPayload = response.read()

        def timeLog(self, formatDate, timeInSeconds):
            post = {}
            post['date'] = timeInSeconds()
            post['date'] = formatDate()
            logging.insert(post)
            logging.info('Timestamp added to payload')

        print("Client connecting on port 8080 using SSL")
        diamondSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c_ssl = ssl.wrap_socket(diamondSock,
                                ca_certs="server.crt",
                                cert_reqs=ssl.CERT_REQUIRED)
        c_ssl.connect(('localhost', 8080))
        c_ssl.send(JsonPayload)
        logging.info('Object sent to Application 2')

    except Exception as e:
        print(e)
        print(c_ssl.cipher())
        logging.error('DEBUG: Exception has been thrown')
        c_ssl.close()

    with open('jsonPayload.json', 'w') as outFile:
        jsonObj = outFile.write(json.dumps(url))
        logging.info(' JSON string saved to Text File')

    with open('jsonPayload.json', 'r') as json_data:
        pyObj = json.load(json_data)
        print(repr(pyObj))


if __name__ == '__main__':
    unittest.main(TestApp1)

