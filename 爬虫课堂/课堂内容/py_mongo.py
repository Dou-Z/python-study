from pymongo import MongoClient

clien = MongoClient('127.0.0.1',27017)
db = clien['mon']['pytjon']

db.insert_one({'name':'赵云'})
# data = db.find()
# # # # collection.insert({'name':'chenxi','age':18})
# #
# for i in data:
#     print(i)

