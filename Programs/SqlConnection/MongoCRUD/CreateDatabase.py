import pymongo
from pymongo import MongoClient

myclient= pymongo.MongoClient('mongodb://localhost:27017/')
database=myclient["codes"]
collection=database["subjects"]
print(database)
print(collection)