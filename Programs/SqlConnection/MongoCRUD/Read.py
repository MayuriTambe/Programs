import pymongo
from pymongo import MongoClient

myclient= pymongo.MongoClient('mongodb://localhost:27017/')
database=myclient["codes"]
collection=database["subjects"]

data=([{"Maths":77,"English":79,"Computer":65,"Biology":87}])
result=collection.insert(data)
findvalue=collection.find()
print(result)
print(findvalue)