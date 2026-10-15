import sys
import os
import json
from datetime import datetime

# Define the file where tasks will be stored
TODO_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. If it doesn't exist, return an empty list."""
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return [] # Handle case where file might be empty or corrupted

def save_tasks(tasks):
    """Save the list of tasks back to the JSON file with pretty formatting."""
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    """Add a new task to the list and save it."""
    tasks = load_tasks()
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    now = datetime.now().isoformat()
    
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

def list_tasks(status_filter=None):
    """List all tasks, or filter them by status if provided."""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return

    if status_filter:
        tasks = [t for t in tasks if t["status"] == status_filter]
        if not tasks:
            print(f"No tasks found with status '{status_filter}'.")
            return

    print(f"{'ID':<4} | {'Status':<12} | {'Description':<30} | {'Created At'}")
    print("-" * 75)
    
    for task in tasks:
        created_at = task['createdAt'].split('.')[0]
        print(f"{task['id']:<4} | {task['status']:<12} | {task['description']:<30} | {created_at}")

def update_task(task_id, new_description):
    """Update an existing task's description and updatedAt timestamp."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Error: Task with ID {task_id} not found.")

def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    initial_length = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    
    if len(tasks) == initial_length:
        print(f"Error: Task with ID {task_id} not found.")
        return
        
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully.")

def update_status(task_id, new_status):
    """Change a task's status (todo, in-progress, done)."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {new_status}.")
            return
    print(f"Error: Task with ID {task_id} not found.")

def main():
    """Main entry point to parse command-line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        return
        
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a description for the task.")
            return
        add_task(sys.argv[2])
        
    elif command == "list":
        status_filter = sys.argv[2] if len(sys.argv) > 2 else None
        valid_statuses = ["todo", "in-progress", "done"]
        if status_filter and status_filter not in valid_statuses:
            print(f"Error: Invalid status filter '{status_filter}'. Use: todo, in-progress, done")
            return
        list_tasks(status_filter)
        
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Please provide both task ID and new description.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        update_task(task_id, sys.argv[3])
        
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID to delete.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        delete_task(task_id)
        
    elif command in ["mark-in-progress", "mark-done"]:
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID.")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: Task ID must be an integer.")
            return
        
        status_map = {
            "mark-in-progress": "in-progress",
            "mark-done": "done"
        }
        update_status(task_id, status_map[command])
        
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
