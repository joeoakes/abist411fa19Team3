import sys, datetime 
from pymongo imort MongoClient 

def connectToDB():
	client = MongoClient('localhost',27017)
	db= client.dbTeam3
	collection = db.logMessages
	



def mongoInstance(typer,text) :
	try:
	
		post = {"type" :typer, 
			"text" :text,
			"date" :datetime.datetime.utcnow()}
		post_id = self.collection.insert_one(post)
	
