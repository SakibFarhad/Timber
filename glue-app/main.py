#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime
import paho.mqtt.client as mqtt
import pymongo

mongoObj= object()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("/t/primenumber")
    


def on_message(client, userdata, msg):
    payload = msg.payload 
    print(msg.topic+" "+str(payload))
    jsonData = json.loads(payload)
    now = datetime.now()
    jsonData.update({'date': now.strftime("%d/%m/%Y %H:%M")}) 
    

    print ('Connecting to mongodb...')
    myclient = pymongo.MongoClient("mongodb://user:password@mongodb_container:27017/")
    mydb = myclient["primedb"]
    mycol = mydb["primecollection"]
    print ('Inserting Data..')
    print(mycol.insert_one(jsonData).inserted_id)
    


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt_container", 1883, 60)

client.loop_forever()
