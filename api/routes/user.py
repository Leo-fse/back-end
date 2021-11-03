from bson import ObjectId
from fastapi import APIRouter, HTTPException

from api.database.config import mongo_client
from api.database.serialize import serializeDict, serializeList

from api.models.user import User

user =  APIRouter()
database = mongo_client["test"]
collection = database['user']

@user.get("/")
async def find_all_users():
    res = collection.find()
    return serializeList(res)

@user.get("/{id}")
async def find_one_user(id):
    res = collection.find_one({"_id": ObjectId(id)})
    if res:
        return serializeDict(res)
    raise HTTPException(404, f"There is no user with this id({id})")

@user.post("/")
async def create_user(user: User):
    collection.insert_one(dict(user))
    return serializeList(collection.find())

@user.put("/{id}")
async def update_user(id, user: User):
    res = collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    if res:
        return serializeDict(collection.find_one({"_id": ObjectId(id)}))
    raise HTTPException(404, f"there is no user with this id({id})")

@user.delete("/{id}")
async def delete_user(id, user: User):
    res = collection.find_one_and_delete({"_id": ObjectId(id)})
    if res:
        return "Succesfully deleted todo item !"
    raise HTTPException(404, f"there is no user with this if({id})")
    