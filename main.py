from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

todos = []


class Todo(BaseModel):
    title: str
    description: str


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    finished_at: str = None
    created_at: str
    updated_at: str = None
    deleted_at: str = None


@app.post("/todo", response_model=TodoResponse)
def create_todo(todo: Todo):
    if not todo.title or not todo.description:
        raise HTTPException(status_code=400, detail="Title and description are required")

    todo_id = len(todos) + 1
    created_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    todo_obj = TodoResponse(
        id=todo_id,
        title=todo.title,
        description=todo.description,
        created_at=created_at,
    )
    todos.append(todo_obj)
    return todo_obj


@app.get("/todo", response_model=list[TodoResponse])
def get_all_todos():
    return todos


@app.get("/todo/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int):
    todo = next((t for t in todos if t.id == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todo/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, updated_todo: Todo):
    todo = next((t for t in todos if t.id == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    if not updated_todo.title or not updated_todo.description:
        raise HTTPException(status_code=400, detail="Title and description are required")

    todo.title = updated_todo.title
    todo.description = updated_todo.description
    todo.updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return todo



@app.put("/todo/{todo_id}/finish", response_model=TodoResponse)
def finish_todo(todo_id: int):
    todo = next((t for t in todos if t.id == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.finished_at is None:
        todo.finished_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return todo


@app.delete("/todo/{todo_id}", response_model=TodoResponse)
def delete_todo(todo_id: int):
    todo = next((t for t in todos if t.id == todo_id), None)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    if todo.deleted_at is not None:
        raise HTTPException(status_code=400, detail="Todo already deleted")

    todo.deleted_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return todo
