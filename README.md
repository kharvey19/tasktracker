# 📝 Task Tracker CLI
![Alt Text](task.png)

This is a command-line based task tracker I built inspired by the [Task Tracker project on roadmap.sh](https://roadmap.sh/projects/task-tracker).  
It helped me get hands-on practice with file I/O, CLI argument parsing, and structuring a simple yet functional program in Python.

---

## Motivation

My goal was to create a simple tool to track tasks using the command line, while learning how to:
- Parse user input via CLI arguments
- Store and retrieve structured data using JSON
- Write modular and readable code
- Implement basic CRUD operations
---

## Features

1. Add new tasks with descriptions
2. List all tasks or filter them by status (`todo`, `in-progress`, `done`)
3. Update or delete tasks by ID
4. Store tasks persistently in a local `tasks.json` file

---

## Usage 

Adding a new task
```
task-cli add "Buy groceries"
```

Updating and deleting tasks
```
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1
```

Marking a task as in progress or done
```
task-cli mark-in-progress 1
task-cli mark-done 1
```

Listing all tasks
```
task-cli list
```

Listing tasks by status
```
task-cli list done
task-cli list todo
task-cli list in-progress
```