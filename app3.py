# Project: App3 - Project Diamond
# Purpose Details: Receive a hashed JSON payload through SFTP,
# Verify the hash of the payload, send an email to all
# group members with the payload and compress the messgae. Finally,
# Pyro to pass the payload message to app 4.
# Course: IST 411
# Author: Cieara Parker
# Date Developed: 11/18/2019
# Last Date Changed: 11/18/2019


import base64
import gzip
import hashlib
import hmac
import logging
import smtplib
import sys
from email.mime.text import MIMEText

import Pyro4
import pysftp

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts': cnopts, 'host': 'oz-ist-linux-oakes', 'username': 'ftpuser', 'password': 'test1234', 'port': 100}

fromAddress = 'czp5346@psu.edu'
subject = 'JSON Payload'
toAddress = ['czp5346@psu.edu', 'fjp5090@psu.edu']


@Pyro4.expose
class GreetingMaker(object):
    # Description: Reads back the written payload file created in App1.
    # Param: name
    # Returns: data
    def get_fortune(self, name):
        payload = open("jsonPayload.json", 'rb')
        data = payload.read()
        return data


try:
    with pysftp.Connection(**cinfo) as sftp:
        print("Connection made")
        print("getting jsonPayload.json file")
        sftp.get('/home/ftpuser/jsonPayload.json')
        sftp.remove('/home/ftpuser/jsonPayload.json')
        print("Reading the payload file")
        logging.info('payload file retrieved and read')
        payload = open('jsonPayload.json', 'rb')
        data = payload.read()
        payload.close()
        setKey = "5411"
        setKey = bytes(setKey, 'UTF-8')
        signature = hmac.new(setKey, data, hashlib.sha256).hexdigest()
        print("Signature 1 (sha256): ", signature)
        sig1 = signature.encode('utf8')
        signature_ = base64.encodestring(sig1)
        print("Signature 2 (sha256): ", signature)
        print()
        sig3 = input("Signature from App2: ")
        signature4 = sig3.encode('utf-8')
        signature5 = base64.encodestring(signature4)
        print(signature5)
        compare = hmac.compare_digest(signature_, signature_)
        print(compare)
        jsonPayload = data.decode('utf-8')
        logging.info('Hash value compared')


        # Description: Compresses the payload through gzip.
        # Param: None
        # Returns: payloadComp
        def compressPayload(data):
            payloadComp = gzip.compress(data)
            return payloadComp


        compressPayload(data)
        print("JSON payload is compressed")
        logging.info('Payload compressed')


        # Description: Sends the payload in an email to all of the group memebers.
        # Param: None
        # Returns: None
        def sendEmail(payload, subject, fromAddress, toAddress):
            email_msg = payload
            msg = MIMEText(email_msg)
            msg['Subject'] = subject
            msg['From'] = fromAddress
            msg['To'] = ", ".join(toAddress)
            print("Sending the email")
            logging.info('Email sent')
            s = smtplib.SMTP_SSL('authsmtp.psu.edu', 465)
            s.sendmail(fromAddress, toAddress, msg.as_string())


        sendEmail(jsonPayload, subject, fromAddress, toAddress)
        daemon = Pyro4.Daemon()
        uri = daemon.register(GreetingMaker)
        print("Ready. Object uri = ", uri)
        daemon.requestLoop()
        logging.info('Pyro connected')
except Exception as e:
    print(e)
    print("Log exception 2:", sys.exc_info()[0])
    logging.error('DEBUG: Exception has been thrown')

