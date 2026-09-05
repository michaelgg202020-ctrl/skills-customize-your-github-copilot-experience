from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")

# In-memory task store
TASKS = [
    {"id": 1, "title": "Write project plan", "completed": False},
    {"id": 2, "title": "Review API design", "completed": True},
]


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class Task(TaskCreate):
    id: int


@app.get("/health")
def health_check():
    return {"status": "ok"}


# TODO: Add endpoints for listing tasks, creating a task, updating a task,
# fetching one task by ID, and deleting a task.
# Use the `TASKS` list and the Pydantic models above as your starting point.
