from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Management API")


class Task(BaseModel):
    id: int
    title: str
    status: str
    priority: str


# In-memory database
tasks = [
    {
        "id": 1,
        "title": "Complete Cloud Computing Assignment",
        "status": "Pending",
        "priority": "High"
    },
    {
        "id": 2,
        "title": "Prepare for FastAPI Practical",
        "status": "In Progress",
        "priority": "Medium"
    }
]


# Root endpoint
@app.get("/")
def root():
    return {"message": "Task Management API is running"}


# GET - Retrieve all tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# GET - Retrieve a specific task by ID
@app.get("/tasks/{task_id}")
# pip install fastapi uvicorn pydantic
# uvicorn task_api:app --reload
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


# POST - Create a new task
@app.post("/tasks", status_code=201)
def create_task(task: Task):
    for existing in tasks:
        if existing["id"] == task.id:
            raise HTTPException(
                status_code=400,
                detail="Task with this ID already exists"
            )
    tasks.append(task.dict())
    return {
        "message": "Task created successfully",
        "task": task
    }


# PUT - Update an existing task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for index, existing in enumerate(tasks):
        if existing["id"] == task_id:
            tasks[index] = task.dict()
            return {
                "message": "Task updated successfully",
                "task": tasks[index]
            }
    raise HTTPException(status_code=404, detail="Task not found")


# DELETE - Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
