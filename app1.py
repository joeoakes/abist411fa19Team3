# Project: Project Diamond
# Purpose Details: Application one,
# Pulls JSON from a URL, Saves to a text file,
# Appends a timestamp, Sends to App 2,
# Compares timestamps, Logs all Activity
# Course: IST 411
# Author: Dylan Palaia
# Date Developed: 10/11/2019
# Last Date Changed: 10/17/2019
# Rev: 3.3

import calendar
import socket
import ssl
import json
import urllib.request
import time
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


# Description: Method is used to save the JSON received by Curl to  a .txt file.
# Param: uses getJsonPayload() to get the Json to save. (May be changed to a parameter)
# Returns: None
def saveJsonTotxtFile():
    outfile = open('jsonPayload.txt', 'w')
    json.dump(getJsonPayload(), outfile)
    outfile.close()
    logging.info('DEBUG: JSON string saved to Text File')


# Description: This method uses SSL sockets to as a client to send the JSON to App2.
# Param: Accepts payload
# Returns: None
def sendJsontoApp2(JsonToSend):
    try:
        JsonToSend = JsonToSend
        print("DEBUG: Client connecting on port 8080 using SSL")
        diamondSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(diamondSock,
                                   ca_certs="server.crt",
                                   cert_reqs=ssl.CERT_REQUIRED)
        ssl_sock.connect(('localhost', 8080))
        ssl_sock.send(bytes(JsonToSend, "utf-8"))
        logging.info('DEBUG: Object sent to Application 2')
    except Exception as e:
        print(e)
        print(ssl_sock.cipher())
        logging.error('DEBUG: Exception has been thrown')
        ssl_sock.close()

    with open('jsonPayload.txt', 'r') as json_data:
        pyObj = json.loads(json_data)
        print(repr(pyObj))

    # Description: This method uses CURL to pull JSON payloads from a URL.
    # Param: None
    # Returns: Payload from CURL(Bulk or single at a time?)


def getJsonPayload():
    # jsonString = """{"name": "Dylan","lastName": "Palaia","age": 25,"graduated": true, "balance": null}"$

    url = 'https://jsonplaceholder.typicode.com'
    param = '/post/1/comments'

    try:
        print("DEBUG: Getting payload from CURL")
        print('DEBUG: Url: ', url + param)
        response = urllib.request.urlopen(url + param)
        JsonPayload = response.read()
        # print('Payload: ', JsonPayload)

    except Exception as e:
        print(e)
        print("DEBUG: error: %s" % e)
        print("Something went wrong with getting the curl payload")

    return JsonPayload


# ======================Below are several time related functions================


# Description: A tuple is similar to a list of values.
# Its needed here because a tuple is required to get the time stamp as seconds
# and to format it in human readable form.
# Param: None
# Returns: Tuple
def getTimeAsTuple():
    timeTuple = time.gmtime()
    return timeTuple


# Description: This method is just a skeleton. It will compare the round trip time,
# when its received by app 4.
# Param: Int
# Returns: double
def comparetimes(timeIntSeconds):
    a = timeIntSeconds
    b = calendar.timegm(getTimeAsTuple())
    print("Start Time: ", a, "Finish Time", b)
    c = a - b
    return c


# Description: Makes and returns timestamp in seconds
# Param: None
# Returns: Time in Seconds(Int)
def gettimeinSeconds():
    seconds = time.time()
    return seconds


# Create a formatted TimeStamp, returns Int of pretty formatted Date
# Description: Create a formatted TimeStamp, returns Int of pretty formatted Date
# Param: None
# Returns: Int?
def formatDateToHumanReadable():
    formattedTimeStamp = time.strftime("%Y-%m-%d %H:%M:%S", getTimeAsTuple())
    return formattedTimeStamp


# Description: Main Process, Below is a try catch block where all the methods are run.
# Param: None
# Returns: None


try:
    # Save the Payload to a file.
    # saveJsonTotxtFile()

    # Convert the string received by CURL to a Python Object
    jsonList = json.loads(getJsonPayload())
    # Add the time stamp in seconds to the JSON object.
    # TODO This is where we need to look through the payloads and append the timestamp individually.
    # Desciption: Loop adds a timestamp to each of the elements in the list
    # Author: CiearaParker
    # Param: None
    # Returns: None
    for i in jsonList:
        i['date'] = gettimeinSeconds()
        print(i)
    # jsonObject['date'] = gettimeinSeconds()
    # Print/Show the Json with time stamp in pretty format.
    # print(len(jsonList))
    # print(jsonList)



except Exception as e:
    print(e)
