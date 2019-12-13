#Project: App4 - Project Diamond
#Purpose Details: To send a JSON payload through a message broker
#Course: IST 411
#Author: Team 3
#Date Developed: 11/18/2019
#Last Date Changed: 11/18/2019


import Pyro4
import zlib
import sys 
uri = input("What is the Pyro uri of the greeting object?").strip()
name = input("What is your name?").strip()

greeting_maker = Pyro4.Proxy(uri)
print(greeting_maker.get_fortune(name))

class AES: 
	def encryptAES(self, payload) 
	try: 

		pad = b ' '
		obj = AES.new('This is a key', AES.MOD_CBC, 'This is App4')
		length = 16 -(len(payload)%16) 
		payload += length *pad 
		ciphertext = object.encrypt(payload)
		return ciphertext
	except Exception as e: 
		print (e) 

