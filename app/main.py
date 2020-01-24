#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import paho.mqtt.client as mqtt
# import json
# from prime_number import getPrimeNumber

# # BROKER_HOST = 'timber_mqtt_1'
# BROKER_HOST = 'localhost'
# MQTT_TOPIC = '/t/primenumber'

# client = mqtt.Client("P1")
# client.connect(BROKER_HOST)
# post = {
#     'start': 3,
#     'end': 10,
#     'primeNumbers': [
#         4, 5, 6
#     ]
# }

# client.publish(MQTT_TOPIC, payload=json.dumps(post))

import sys
import getopt


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print ('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print ('Input file is "', inputfile)
    print ('Output file is "', outputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
