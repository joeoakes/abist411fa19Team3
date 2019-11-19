# Project: App2 Test - Project Diamond
# Purpose Details: Testing to see if App 1 complies and runs.
# Course: IST 411
# Author: Cieara Parker
# Date Developed: 11/18/2019
# Last Date Changed: 11/18/2019

import calendar
import socket
import ssl
import json
import urllib.request
import time
import logging
import unittest

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


class TestApp1(unittest.Testcase):

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
    def sendJsontoApp2(jsonList):
        jsonList = jsonList
        try:
            print("DEBUG: Client connecting on port 8080 using SSL")
            diamondSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c_ssl = ssl.wrap_socket(diamondSock,
                                    ca_certs="server.crt",
                                    cert_reqs=ssl.CERT_REQUIRED)
            c_ssl.connect(('localhost', 8080))
            c_ssl.send(bytes(jsonList, 'utf - 8'))
            logging.info('DEBUG: Object sent to Application 2')
        except Exception as e:
            print(e)
            print(c_ssl.cipher())
            logging.error('DEBUG: Exception has been thrown')
            c_ssl.close()

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
        # Author: Cieara Parker
        # Param: None
        # Returns: None
        for i in jsonList:
            i['date'] = gettimeinSeconds()
            i['date'] = formatDateToHumanReadable()

        sendJsontoApp2()
        print(jsonList)

# jsonObject['date'] = gettimeinSeconds()
# Print/Show the Json with time stamp in pretty format.


    except Exception as e:
        print(e)

if __name__ == '__main__':
    unittest.main()
