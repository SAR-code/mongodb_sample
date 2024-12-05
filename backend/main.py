'''
script: main.py
action: contains basic CRUD operations and runs the FastAPI server
author: Dylan McCallum
date: 27NOV24
reference: FARMSTACK Tutorial from @bekbrace
'''

# Retrieving the required modules

from fastapi import FastAPI, HTTPException
#from pydantic import BaseModel
from model import Todo, TodoCreate

from database import (
    fetch_one_todo,
    fetch_all_todos,
    #create_todo,
    update_todo,
    remove_todo,
    todo_create,
)

# HTTP exception class to display exception information

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:3000",

]

# middleware defined
# Software that bridges a connection between an operating system or database and applications, especially on a network

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# Define various CRUD methods to use

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

# @app.post("/api/todo/", response_model=Todo)
# async def post_todo(todo: TodoCreate):
#     response = await create_todo(todo.model_dump())
#     if response:
#         return response
#     raise HTTPException(400, "Something went wrong")

@app.put("/api/todo/{title}/", response_model=Todo)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Todo successfully deleted"
    raise HTTPException(404, f"There is no todo with the title {title}")

@app.post("/api/todo/", response_model=TodoCreate)
async def create_todo_route(todo: Todo):
    
    created_item = await todo_create(todo)
    if created_item:
        return created_item
    else:
        raise HTTPException(status_code=400, details="Todo creation failed")
