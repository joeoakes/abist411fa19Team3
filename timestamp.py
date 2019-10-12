import calendar
import json
import time


def getTimeAsTuple():
    timeTuple = time.gmtime()
    return timeTuple


def getJsonPayload():
    jsonString = """{"name": "Dylan","lastName": "Palaia","age": 25,"graduated": true, "balance": null}"""
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


# Create a Python Json Object
jsonObject = json.loads(getJsonPayload())

# This calls my comparetimes method to show both the start and finish times in seconds.
# calculates the difference in seconds, returns the difference.
print("Time Difference", comparetimes(gettimeinSeconds()))

# add the time stamp in seconds
jsonObject['date'] = gettimeinSeconds()
# Print the Json with time stamp in seconds
print(jsonObject)

# add the time stamp in pretty format
jsonObject['date'] = formattimetoHuman()
# Print the Json with time stamp in pretty format
print(jsonObject)

