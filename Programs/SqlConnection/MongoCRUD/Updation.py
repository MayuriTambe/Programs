import pymongo
from pymongo import MongoClient

myclient= pymongo.MongoClient('mongodb://localhost:27017/')
database=myclient["codes"]
collection=database["subjects"]

data=([{"Maths":77,"English":79,"Computer":65,"Biology":87}])
newvalues = { "$set": { "Maths": "98" } }

Updation=collection.update(data,newvalues)
print(Updation)
for x in collection.find():
  print(x)