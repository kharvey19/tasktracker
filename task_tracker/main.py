import typer
import json 
import datetime
from typing import Optional


app = typer.Typer()

TASK_FILE = "tasks.json"

def load_tasks():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)["tasks"]
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump({"tasks": tasks}, file, indent=4, default=str)

@app.command()
def list(status: Optional[str] = None):
    """List all tasks or filter by status"""
    tasks = load_tasks()
    header = "\nAll Tasks" if not status else f"\n{status.capitalize()} Tasks"
    print(header)
    print("-" * len(header.strip()))
    for i, task in enumerate(tasks, 1):
        if not status or task["status"] == status:
            print(f"{i}: {task['description']}")
    print("\n")

@app.command()
def add(description: str):
    """Add a new task"""
    tasks = load_tasks()
    tasks.append({
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": ""
    })
    save_tasks(tasks)
    print(f"\nAdded '{description}' to your task list!\n")

@app.command()
def update(id: str, new_description: str):
    """Update a task's description"""
    tasks = load_tasks()
    print(tasks, "\n\n")
    for task in tasks:
        if task["id"] == id:
            task["description"] = new_description
            task["updatedAt"] = datetime.datetime.now().isoformat()
            break
    print(tasks)
    save_tasks(tasks)
    print(f"\nUpdated task {id} to '{new_description}'\n")

@app.command()
def delete(id: str):
    """Delete a task by ID"""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != id]
    save_tasks(tasks)
    print(f"\nDeleted task {id} from your list\n")

@app.command()
def mark(id: str, status: str):
    """Mark task as 'todo', 'in progress', or 'done'"""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == id:
            task["status"] = status
            task["updatedAt"] = datetime.datetime.now().isoformat()
            break
    save_tasks(tasks)
    print(f"\nMarked task {id} as '{status}'\n")

if __name__ == "__main__":
    app()