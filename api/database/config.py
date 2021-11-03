# MongoDB driver
import motor.motor_asyncio
import pymongo
# mongo_client = motor.motor_asyncio.AsyncIOMotorClient(
#     'mongodb://localhost:27017'
# )
mongo_client = pymongo.MongoClient('mongodb://localhost:27017')