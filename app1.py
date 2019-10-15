# Project: Application One gets a Payload from CURL, saves to a text file and appends a time stamp to the payload. 
# Purpose Details:
# Course: IST 411
# Author: Dylan Palaia
# Date Developed: 10/11/2019
# Last Date Changed: 10/11/2019
# Rev: 3.0

import calendar
import socket
import ssl
import json
import curl
import urllib.parse
import urllib.request
import time
import logging 




def saveJsonTotxtFile():
    outfile = open('jsonPayload.json', 'w')
    json.dump(getJsonPayload(), outfile)
    outfile.close()
    logging.info('JSON Object is converted to Text File') 


def sendJsontoApp2(JsonToSend):
    try:
        JsonToSend = JsonToSend
        print("Client connecting on port 8080 using SSL")
        diamondSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(diamondSock,
                                   ca_certs="server.crt",
                                   cert_reqs=ssl.CERT_REQUIRED)
        ssl_sock.connect(('localhost', 8080))

        ssl_sock.send(bytes(JsonToSend, "utf-8"))
	logging.info('Object sent to Application 2') 
    except Exception as e:
        print(e)
        print(ssl_sock.cipher())
	logging.error('Exception has been thrown')
    ssl_sock.close()
   


# Time Stamp Methods
def getTimeAsTuple():
    timeTuple = time.gmtime()
    return timeTuple


def getJsonPayload():
    jsonString = """{"name": "Dylan","lastName": "Palaia","age": 25,"graduated": true, "balance": null}"""
   
    print('https://jsonplaceholder.typicode.com/posts/1')
    url='https://jsonplaceholder.typicode.com'
    param='/posts/1'	

    try:
    	from io import BytesIO

    	print('Url: ', url + param)
   	response = urllib.request.urlopen(url + param)
    	JsonPayload = response.read()
    	print('Payload: ', JsonPayload)

   except ImportError:
    	from StringIO import StringIO as BytesIO
    	e = sys.exc_info()[0]
    	print("error: %s" % e)
	
   return jsonString


def comparetimes(timeIntSeconds):
    A = timeIntSeconds
    B = calendar.timegm(getTimeAsTuple())
    print("Start Time: ", A, "Finish Time", B)
    C = A - B
    return C


# makes and returns timestamp in seconds
def gettimeinSeconds():
    seconds = time.time()
    return seconds


# Create a formatted TimeStamp, returns Int of pretty formatted Date
def formattimetoHuman():
    formattedTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S", getTimeAsTuple())
    return formattedTimeStamp


# Main Process
try:
    saveJsonTotxtFile()

    jsonObject = json.loads(getJsonPayload())

    # add the time stamp in seconds
    jsonObject['date'] = gettimeinSeconds()

    # Turns json to string for sending to app 2
    json.dumps(jsonObject)
    # Sends json to app 2
    sendJsontoApp2(json.dumps(jsonObject))

    # add the time stamp in pretty format
    jsonObject['date'] = formattimetoHuman()
    # Print the Json with time stamp in pretty format
    print(jsonObject)

except Exception as e:
    print(e)

