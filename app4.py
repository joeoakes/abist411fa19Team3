#Project: App4 - Project Diamond
#Purpose Details: To send a JSON payload through a message broker
#Course: IST 411
#Author: Team 3
#Date Developed: 11/18/2019
<<<<<<< HEAD
#Last Date Changed: 12/13/2019
from  Crypto.Cipher import AES 
import Pyro4
import zlib
import sys 



=======
#Last Date Changed: 11/18/2019

import Pyro4
import pika

try:
    uri = input("What is the Pyro uri of the greeting object?").strip()
    name = input("What is the name of the .json file?").strip()

    greeting_maker = Pyro4.Proxy(uri)
    print(greeting_maker.get_fortune(name))

    print("Connecting to Localhoast Queue")
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    print("Channel Connected")
    channel.queue_declare(queue='ist411')
    channel.basic_publish(exchange='', routing_key='ist411', body='jsonPayload.json')
    print(" [x] Sent 'jsonPayload.json'")
    connection.close()

except Exception as e:
    print(e)

class AES: 
	def encryptAES(self, payload) 
	try: 

		pad = b ' '
		obj = AES.new('This is a key', AES.MOD_CBC, 'This is an IV456')
		length = 16 -(len(payload)%16) 
		payload += length *pad 
		ciphertext = object.encrypt(payload)
		return ciphertext
	except Exception as e: 
		print (e) 
