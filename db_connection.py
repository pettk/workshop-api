import pymongo

url = 'mongodb+srv://admin:Jl782kfJPZhB3RQS@cluster0.sfvpjku.mongodb.net/'
client = pymongo.MongoClient(url)

db = client['WorkshopDatabase']