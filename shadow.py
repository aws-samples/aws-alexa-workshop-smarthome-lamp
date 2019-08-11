#!/usr/bin/python

# Lab 1 - Setting up.
# Make sure your host and region are correct.

import sys
import ssl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import json
import time
import qrcode

iotEndpoint = "<xxx>-ats.iot.<region>.amazonaws.com"
thingName = "ratchet"
deviceBindingURL = "<your-device-bind-url>"

# Generate QR code for device binding
img = qrcode.make(deviceBindingURL + "?thingName=" + thingName)
img.save('./qrcode.png')

# Shadow JSON schema example
# {
# "state": {
#   "desired":{
#     "power":"ON" / "OFF"
#   }
# }
# }

# A programmatic shadow handler name prefix.
SHADOW_HANDLER = "ratchet"


# Function to encode a payload into JSON
def json_encode(string):
    return json.dumps(string)


# Function to print message
def on_message(message, response, token):
    print message


# Custom Shadow callback
def customShadowCallback_Delta(payload, responseStatus, token):
    # payload is a JSON string ready to be parsed using json.loads(...)
    # in both Py2.x and Py3.x
    print(responseStatus)
    payloadDict = json.loads(payload)
    print("++++++++DELTA++++++++++")
    print("property: " + str(payloadDict["state"]))
    print("power: " + str(payloadDict["state"]["power"]))
    print("version: " + str(payloadDict["version"]))
    print("+++++++++++++++++++++++\n\n")
    shadowMessage = {"state": {"reported": {"power": str(payloadDict["state"]["power"])}}}
    shadowMessage = json.dumps(shadowMessage)
    deviceShadowHandler.on_message = on_message
    deviceShadowHandler.json_encode = json_encode
    deviceShadowHandler.shadowUpdate(shadowMessage, on_message, 5)
    print "Shadow Update Sent"


# Create a deviceShadow with persistent subscription
shadow = AWSIoTMQTTShadowClient(thingName)

# Setup our MQTT client and security certificates
# Make sure your certificate names match what you downloaded from AWS IoT

# Use the endpoint from the settings page in the IoT console
shadow.configureEndpoint(iotEndpoint, 8883)

# rootCA.pem is the same for all devices
# private.key is device-name.private.key from the ZIP file
# cert.pem is device-name.cert.pem from the ZIP file
shadow.configureCredentials("credentials/rootCA.pem", "credentials/private.key", "credentials/cert.pem")

# AWSIoTMQTTShadowClient configuration
shadow.configureAutoReconnectBackoffTime(1, 32, 20)
shadow.configureConnectDisconnectTimeout(10)  # 10 sec
shadow.configureMQTTOperationTimeout(5)  # 5 sec

# Connect to AWS IoT
shadow.connect()
print "Connect to IoT Core"

# Create a deviceShadow with persistent subscription
deviceShadowHandler = shadow.createShadowHandlerWithName(thingName, True)

# Listen on deltas
deviceShadowHandler.shadowRegisterDeltaCallback(customShadowCallback_Delta)

# Loop forever
while True:
    time.sleep(1)
