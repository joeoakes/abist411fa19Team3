#Project: App4 - Project Diamond
#Purpose Details: To send a JSON payload through a message broker
#Course: IST 411
#Author: Team 3
#Date Developed: 11/18/2019
#Last Date Changed: 11/18/2019


import Pyro4

uri = input("What is the Pyro uri of the greeting object?").strip()
name = input("What is your name?").strip()

greeting_maker = Pyro4.Proxy(uri)
print(greeting_maker.get_fortune(name))




