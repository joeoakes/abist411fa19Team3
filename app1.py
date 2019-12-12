# Project: App1 - Project Diamond
# Purpose Details: Pulls JSON from a URL, saves to a text file, appends a timestamp
# and sends to App 2. It then compares timestamps and logs all activity
# Course: IST 411
# Author: Cieara Parker
# Date Developed: 11/18/2019
# Last Date Changed: 11/18/2019


# Project: App2 Test - Project Diamond
# Purpose Details: Testing if App 2 complies and runs.
# Course: IST 411
# Author: Cieara Parker
# Date Developed: 11/18/2019
# Last Date Changed: 11/18/2019

import socket
import ssl
import sys
import json
import urllib.request
import time
import pika
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


# Description: Makes and returns timestamp in seconds
# Param: None
# Returns: Time in Seconds(Int)
def timeInSeconds():
    times = time.time()
    return times


# Description: Create a formatted timestamp, returns string for a formatted date (month, day, year).
# Param: None
# Returns: Sring
def formatDate():
    formatted = time.strftime("%Y-%m-%d %H:%M:%S", timeInTuple())
    return formatted


# Description: A tuple is required to get the time stamp as seconds and to format it in human readable form.
# Param: None
# Returns: Tuple
def timeInTuple():
    tuple = time.gmtime()
    return tuple


url = 'https://jsonplaceholder.typicode.com'
param = '/post/1/comments'

try:
    print('Url: ', url + param)
    response = urllib.request.urlopen(url + param)
    JsonPayload = response.read()


    # Description: creates a post to add to the log for each logging event occurred
    # Param: None
    # Returns: None
    def timeLog():
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

    print("Connection to localhost")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    print("Queue ist411 created")
    channel.queue_declare(queue='ist411')
    logging.info('ist411 queue created')


    # Description: callback function that will receive the message
    # Param: None
    # Returns: None
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        logging.info('Message received')


    channel.basic_consume(queue='ist411', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()



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

