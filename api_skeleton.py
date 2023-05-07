from fastapi import FastAPI, Path, HTTPException
from typing import Optional # another method to remove required field
from pydantic import BaseModel

app = FastAPI()

# MODEL - usually put in a seperate file
class User(BaseModel):
    name: str
    email: str
    todo_id: list

class Todo(BaseModel):
    user_id: str
    title: str
    description: str

# DB METHODS
class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class UpdateTodo(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

# STATIC/DUMMY DATA
users = {
    "id1": User(name="Naruto Uzumaki", email ="naruto@mail.com", todo_id=['todo1', 'todo2']),
    "id2": User(name='Sasuke Uchiha', email='sasuke@mail.com', todo_id=[]),
    "id3": User(name='Sakura Haruno', email='sakura@mail.com', todo_id=['todo3'])
}

todos = {
    'todo1': Todo(user_id='id1', title='dinner', description='eat ramen with kakashi @ 6'),
    'todo2': Todo(user_id='id1', title='groceries', description='milk, eggs, udon'),
    'todo3': Todo(user_id='id3', title='homework', description='homework for iruka umino sensei')
}

# USER
# - create a user
@app.post("/signup")
async def add_user(id: str, user: User):
    if id in users:
        return {"error":"ID already exists"}
    users[id] = user
    return users[id]

# - return an existing user details
@app.get("/login")
async def get_user(name: str, email: str):
    for id in users:
        if users[id].email == email:
            return users[id]
    return {"error":"ID not found"}

# - update user information
@app.put("/profile/edit/{id}")
async def update_user(id: str, user: UpdateUser):
    if id not in users:
        return {"error":"ID not found"}
    if user.name != None:
        users[id].name = user.name
    if user.email != None:
        users[id].email = user.email
    
    return users[id]
    
# - deletes existing user
@app.delete("/profile/delete/{id}")
async def delete_user(id: str):
    if id not in users:
        return {"error":"ID not found"}
    del users[id]
    return {"msg":"user has been deleted successfully"}


# TODO
# - fetch all todos for currently 'logged in' user
@app.get('/todos/{id}')
async def get_todos(id: str):
    results = []
    for todo_id in todos:
        if todos[todo_id].user_id == id:
            results.append(todos[todo_id])
    return results


# - fetch a todo based on title
@app.get('/todos')
async def get_todo(*, title: str):
    for todo_id in todos:
        if todos[todo_id].title == title:
            return todos[todo_id]
    return {"error":"title not found"}

# - post new todo
@app.post('/todos/new/{todo_id}')
async def post_todo(id: str, todo_id: str, todo: Todo):
    if todo_id in todos:
        return {'error':'duplicate ID'}
    todos[todo_id] = todo
    users[id].todo_id.append(todo_id)
    return todos[todo_id]

# - updates todo
@app.put("/todos/edit/{todo_id}")
async def update_todo(todo_id: str, todo: UpdateTodo):
    if todo_id not in todos:
        return {'error':'ID not found'}

    if todo.title != None:
        todos[todo_id].title = todo.title
    if todo.description != None:
        todos[todo_id].description = todo.description
    
    return todos[todo_id]

# - removes an existing todo
@app.delete("/todos/delete/{todo_id}")
async def delete_todo(todo_id: str):
    if todo_id not in todos:
        return {"error":"ID not found"}
    del todos[todo_id]
    return {"msg":"todo has been deleted successfully"}
