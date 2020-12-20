# Run on Raspberry Pi only

# Read Data from Arduino
# Arduino USB is connected to USB Port of RPi
# Arduino Uno - Italy - ttyACM0

import serial
import paho.mqtt.client as mqtt
import time

broker='204.236.212.224' # public-ip
port=1883
topic='nitw/iot'

ser=serial.Serial('/dev/ttyACM0',9600,timeout=0.5)


# create a client object
client=mqtt.Client()

# connect with broker
client.connect(broker,port)
print('Broker Connected')

while True:
        # check whether data is available or not
        if(ser.inWaiting()>0):
                t=ser.readline()
                t=t.decode('utf-8')
                t=t.split('#')[1]
                t=t[:-3] # last 3 chars will be removed from t
                print(t)
                client.publish(topic,str(t))
                print('Published')
                time.sleep(3) # 3 seconds of delay


