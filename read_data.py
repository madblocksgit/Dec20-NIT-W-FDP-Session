# Import the pymongo library
from pymongo import MongoClient

# Connect with Server
mc=MongoClient('localhost',27017)

# Connect with database
db=mc['iotnitw']
print('Database Connected')

# Connect with Collection
c=db['sensorValues']
print('Collection Connected')

for i in c.find():
        print (i)

