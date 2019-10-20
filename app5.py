import logging
from logging.config import fileConfig
from pymongo import MongoClient
import sys
import pdb 



logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


logMessages = logging.config.listen()


pdb.set_trace()


try:  
 client = MongoClient('localhost', 27017)   
 print("Connected to MongoDB")   

 db = client.dbTeam3   
 print("Got the Database module4_dbTeam3")   

 collection = db.logMessages 
 print("Got the Collection payloadLogMessages")   
 
 print("Created the Document object")   
 response= logMessages 

 post_id = collection.insert(response)
 print (post_id)
except:   
 e = sys.exc_info()[0]   
 print("error: %s" % e)

