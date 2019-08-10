#!/usr/bin/python

# Lab 1 - Setting up.
# Make sure your host and region are correct.

import sys
import ssl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import json
import time
import qrcode

#Setup our MQTT client and security certificates
#Make sure your certificate names match what you downloaded from AWS IoT

mqttc = AWSIoTMQTTClient("1234")

#Use the endpoint from the settings page in the IoT console

#	Most company's internet block 8883 port. 
#	If you are using an internal network, you will meet the error "connection refused"
#	Please use a guest network 
mqttc.configureEndpoint("xxxxxx.ats.iot.cn-north-1.amazonaws.com.cn",8883)


#	rootCA.pem is the same for all devices
#	privateKey.pem is device-name.private.key from the ZIP file
#	certificate.pem is device-name.cert.pem from the ZIP file
mqttc.configureCredentials("credentials/rootCA.pem","credentials/privateKey.pem","credentials/certificate.pem")

#Function to encode a payload into JSON
def json_encode(string):
        return json.dumps(string)

mqttc.json_encode=json_encode

#Declaring our variables
message ={
  'val1': "Value 1",
  'val2': "Value 2",
  'val3': "Value 3",
  'message': "Test Message"
}

#Encoding into JSON
message = mqttc.json_encode(message)

#This sends our test message to the iot topic
def send():
    mqttc.publish("iot", message, 0)
    print "Message Published"


#Connect to the gateway
mqttc.connect()
print "Connected"

#Loop until terminated

while True:
    send()
    time.sleep(5)


#To check and see if your message was published to the message broker go to the MQTT Client and subscribe to the iot topic and you should see your JSON Payload



mqttc.disconnect()




