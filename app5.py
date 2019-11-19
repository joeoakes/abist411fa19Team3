import logging
from logging.config import fileConfig
from pymongo import MongoClient
import sys
import pdb 


#Sets the type of
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


logMessages = logging.config.listen()
logMessages.start()



pdb.set_trace()
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def connecting_to_database():
    try:
        client = MongoClient('localhost', 27017)
        print("Connected to MongoDB")

        db = client.dbTeam3
        print("Got the Database module4_dbTeam3")

        stream_handler = logging.streamHandler()
        stream_handler.setLevel(logging.info())


 #print("create an INET, STREAMing socket using SSL")


    except:
        e = sys.exc_info()[0]
        print("error: %s" % e)


try:
   connecting_to_database()

except Exception as e:
    print(e)
