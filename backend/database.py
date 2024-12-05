'''
script: database.py
action: Connects to the database and maintains the CRUD methods
author: Dylan McCallum
date: 27NOV24
reference: FARMSTACK Tutorial by @bekbrace
'''

# Declare required modules

# MongoDB driver
from motor.motor_asyncio import AsyncIOMotorClient
from model import Todo
import os
#from bson import ObjectId


client = AsyncIOMotorClient(os.getenv('DB_SHORT'))

database = client.TodoList
collection = database.todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

# async def create_todo(todo):
#     document = todo
#     result = await collection.insert_one(document)
#     return result

async def update_todo(title, desc):
    await collection.update_one({"title": title}, {"$set":{"description": desc}})
    document = await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True

async def todo_create(todo: Todo):
    
    result = await collection.insert_one(todo.model_dump())
    created_item = await collection.find_one({"_id": result.inserted_id})
    
    if created_item:
        created_item["id"] = str(created_item["_id"])
        del created_item["_id"]
        return created_item
    
    return None

