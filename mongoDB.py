# Project: MongoDB - Project Diamond
# Purpose Details: Stores all logging information of application runs.
# Course: IST 411
# Author: Jinal Parmar
# Date Developed: 11/18/2019
# Last Date Changed: 11/18/2019


import sys, datetime 
from pymongo import MongoClient 

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
	
