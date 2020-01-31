#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json, sys
from prime_number import getPrimeNumber

BROKER_HOST = 'mqtt_container'
# BROKER_HOST = 'localhost'
MQTT_TOPIC = '/t/primenumber'

def publishData(startPoint, endPoint):
    client = mqtt.Client("P1")
    client.connect(BROKER_HOST)
    post = {
        'start': startPoint,
        'end': endPoint,
        'primeNumbers': getPrimeNumber(startPoint, endPoint)
    }
    print (post)
    client.publish(MQTT_TOPIC, payload=json.dumps(post))



def main(argv):
    if len(argv) == 2: 
        publishData(int(argv[0]), int(argv[1]))
    else:
        print ("""
        Useage: python3 main.py <start point> <end point>
        example: python3 main.py 5 20
        """)

if __name__ == "__main__":
    main(sys.argv[1:])