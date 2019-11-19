
# Project: App3 - Project Diamond
# Purpose Details: Unit testing for sending email, compresspayload
# Course: IST 411
# Author: Jinal Parmar
# Date Developed: 11/18/2019
# Last Date Changed: 11/18/2019



import json
import unittest
import urllib
from unittest import TestCase
import smtplib
from mock import patch, call

from app3 import sendEmail
from app3 import compressPayload
import gzip

class TestSendEmail(TestCase):
    def test_sendEmail(self,address):
        with patch ("smtplib.SMTP") as mock_smtp:
            from_address = "fjp5090@psu.edu"
            to_address = "fjp5090@psu.edu"

            #setting up paylaod
        def setupPayload(self):
            with urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts/1') as payload:
                jsonPayload = json.loads(payload.read().decode('utf-8'))

            ''' Testing sendEmail method '''

            def testEmailisSent(self):
                email = sendEmail(jsonPayload,"Test email",from_address,to_address)
                self.assertTrue(email.sendEmail())



class TestCompressPayload(TestCase):
    def test_compressPayload(self):
        #setting up the payload
        def setupPayload(self):
           data = '{"value": "test"}'
           compressTestPayload = gzip.compress(data)


        #Testing compression method


        def payloadIsCompressed(self,data ):
            compress = compressPayload(data)
            testCheckSum = gzip.compress(data)
            self.assertTrue(self.compressTestPayload,testCheckSum)







class TestGreetingMaker(TestCase):
    def test_get_fortune(self):
        payload = open("jsonPayload.json", 'rb')
        data = payload.read()


if __name__ == 'main':
    test_classes_to_run = [TestCompressPayload,TestSendEmail,TestGreetingMaker]
    loader = unittest.TestLoader()
    
    runner = unittest.TextTestRunner()
    results = runner.run(test_classes_to_run)

