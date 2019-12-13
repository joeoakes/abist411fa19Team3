






=======
# Project: App5 - Project Diamond
# Purpose Details: Gathers all the logging information and sends it to the MongoDB.
# Course: IST 411
# Author: Jinal Parmar
# Date Developed: 11/18/2019
# Last Date Changed: 11/18/2019
>>>>>>> 40b55d91cda51b00f57be01952e4a62582054271

import logging
from logging.config import fileConfig

from pymongo import MongoClient
import sys
import pdb
import socket
import logging.handlers
logging.basicConfig(level = logging.INFO, format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %$')
formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")



logInfo = ' '



logMessages = logging.config.listen()
logMessages.start()



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8080))
serversocket.listen(5)


 
#Root logger 
logger = logging.getLogger('app5') 

stream_handler = logging.StreamHandler() 
stream_handler.setLevel(logging.INFO)



logger.addHandler(stream_handler) 




try: 
	#logging.info('Test') 
	while True: 
			(clientsocket,address) = serversocket.accept()
			logInfo = clientsocket.recv(1024).decode()
			if logInfo != ' ':
				logging.info(logInfo) 
				logInfo = ' '
	
except Exception as e: 
		print(e) 
		logging.config.stopListening() 
