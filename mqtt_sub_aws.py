# Read the Data from RPi Publisher (mqtt_pub.py) and pushes the data to MongoDB Server
# Run this program on AWS Machine only

import paho.mqtt.client as mqtt
from pymongo import MongoClient

# create a client to connect with MongoDB Server
mc=MongoClient('localhost',27017)

# Connect with databse
db=mc['iotnitw']

# Connect with collection
c=db['sensorValues']

broker='172.31.29.90' # my private broker (change it to your private ip)
port=1883
topic='nitw/iot'

# create a client object
client=mqtt.Client()

# connect with broker
client.connect(broker,port)
print('Broker Connected')
id=1000

# Subscribe
client.subscribe(topic)

# notification
def mom(client,userdata,msg): # msg - {key:value} - {payload: your_msg}
  global id
  t=(msg.payload) # msg - object (rocket), payload - key holding a value (data)
  t=t.decode('utf-8')
  print(t)
  id+=1
  k={'_id':id,'moisture_sensor':t}
  c.insert_one(k)
  print('Document Inserted')

# configure the notification
client.on_message=mom

# execute this subscribe on an infinte loop
client.loop_forever()
