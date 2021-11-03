from fastapi import APIRouter, HTTPException

from api.models.common import Todo, Fleet, Parts
from api.database.Todo import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

todo = APIRouter()

@todo.get("/")
def read_root():
    return {"Ping": "Pong"}

# @app.get("/{model}/{parts}/{usekbn}/{clasify}/{newmanukbn}/{stockkbn}", response_model=ClasifyData)
@todo.get("/clasify")
async def fetch_clasify_data(model: Fleet, parts: Parts):

    return {"model": model, "parts": parts}

@todo.get("/api/todo")
async def get_todo():
    res = await fetch_all_todos()
    return res

@todo.get("/api/todo/{title}", response_model=Todo)
async def get_todo_by_title(title:str):
    res = await fetch_one_todo(title)
    if res:
        return res
    raise HTTPException(404, f"there is no TODO item with this title{title}") 

@todo.post("/api/todo", response_model=Todo)
async def create_todo(todo:Todo):
    res = await create_todo(todo.dict())
    if res:
        return res
    raise HTTPException(400, "Something went wrong / Bad Request")

@todo.put("/api/todo/{title}")
async def update_todo(title:str, desc:str):
    res = await update_todo(title, desc)
    if res:
        return res
    raise HTTPException(404, f"there is no TODO item with this title{title}")

@todo.delete("/api/todo/{title}")
async def delete_todo(title):
    res = await remove_todo(title)
    if res:
        return "Succesfully deleted todo item !"
    raise HTTPException(404, f"there is no TODO item with this title{title}")
