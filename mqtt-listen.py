import paho.mqtt.client as mqttClient
import time
import datetime
from iso8601 import parse_date
import json
import mqtt_creds_config
user=mqtt_creds_config.user
broker_address=mqtt_creds_config.broker_address
password=mqtt_creds_config.password
port=mqtt_creds_config.port

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")

def on_message(client, userdata, message):
    decoded_message=str(message.payload.decode("utf-8"))
    msg=json.loads(decoded_message)
    my_datetime = parse_date(msg['received_at']).strftime('%d-%m-%Y %H:%M:%S %Z') # reformatting time 
    decoded=msg['uplink_message']['decoded_payload']
    timestamp=decoded['decodedData']['Timestamp']
    temp=decoded['decodedData']['Temp']
    humid=decoded['decodedData']['Humidity']
    print(my_datetime + ": Timestamp: " + timestamp + ": Temperature: " + temp + "C, Humidity: " + humid + "%") # all strings, so we can concatenate them

Connected = False   # global variable for the state of the connection
client = mqttClient.Client("Python")               # create new instance
client.username_pw_set(user, password=password)    # set username and password
client.on_connect= on_connect                      # attach function to callback
client.on_message= on_message                      # attach function to callback
client.connect(broker_address, port=port)          # connect to broker

client.loop_start()                                # start the loop
while Connected != True:                           # Wait for connection
    time.sleep(0.1)
client.subscribe("v3/+/devices/+/up")		   # subscribe to 'up' topic
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()

