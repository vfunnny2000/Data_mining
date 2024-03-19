import json
import time
from pymongo import MongoClient

NAME = 'books'

start_time = time.time()
uri = "mongodb+srv://olgaduganova:F1Dye6s0YmTBZPNk@cluster0.na76xic.mongodb.net/"
client = MongoClient(uri)
db = client['library']
collection = db[NAME]

count = collection.count_documents({})
print(f'Число записей в базе {NAME}: {count}')


cheapest = collection.aggregate([
    {"$group": {"_id": "$name", "min_price": {"$min": "$price"}}},
    {"$sort": {"min_price": 1}}
])
cheapest = list(cheapest)[0]
print(f'Самая дешевая книга: {cheapest["_id"]} стоит £{cheapest["min_price"]:.2f}')


most_expensive = collection.aggregate([
    {"$group": {"_id": "$name", "max_price": {"$max": "$price"}}},
    {"$sort": {"max_price": -1}}
])
most_expensive = list(most_expensive)[0]
print(f'Самая дорогая книга: {most_expensive["_id"]} стоит £{most_expensive["max_price"]:.2f}')


most_available = collection.aggregate([
    {"$group": {"_id": "$name", "count": {"$max": "$available"}}},
    {"$sort": {"count": -1}}
])
most_available = list(most_available)[0]
print(f'Больше всего книг в наличие: {most_available["_id"]} их {most_available["count"]} шт.')