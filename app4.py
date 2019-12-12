#Project: App4 - Project Diamond
#Purpose Details: To send a JSON payload through a message broker
#Course: IST 411
#Author: Team 3
#Date Developed: 11/18/2019
#Last Date Changed: 11/18/2019

import Pyro4
import pika

try:
    uri = input("What is the Pyro uri of the greeting object?").strip()
    name = input("What is your name?").strip()

    greeting_maker = Pyro4.Proxy(uri)
    print(greeting_maker.get_fortune(name))

    print("Connecting to Localhoast Queue")
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    print("Channel Connected")
    channel.queue_declare(queue='ist411')
    channel.basic_publish(exchange='', routing_key='ist411', body='payloadSendParker.json')
    print(" [x] Sent 'payloadSendParker.json'")
    connection.close()

except Exception as e:
    print(e)

