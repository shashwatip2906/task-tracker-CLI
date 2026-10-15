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
    
    # Generate a unique ID: if tasks exist, take the last task's ID + 1, otherwise start at 1
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    
    # Get current timestamp
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

    # Filter tasks if a status argument was passed
    if status_filter:
        tasks = [t for t in tasks if t["status"] == status_filter]
        if not tasks:
            print(f"No tasks found with status '{status_filter}'.")
            return

    # Print header
    print(f"{'ID':<4} | {'Status':<12} | {'Description':<30} | {'Created At'}")
    print("-" * 75)
    
    for task in tasks:
        # Format timestamp for clean readability (showing date and time without microseconds)
        created_at = task['createdAt'].split('.')[0]
        print(f"{task['id']:<4} | {task['status']:<12} | {task['description']:<30} | {created_at}")

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
        description = sys.argv[2]
        add_task(description)
        
    elif command == "list":
        # Check if an optional status filter was provided (e.g., 'python task_cli.py list done')
        status_filter = sys.argv[2] if len(sys.argv) > 2 else None
        
        # Validate status filter if given
        valid_statuses = ["todo", "in-progress", "done"]
        if status_filter and status_filter not in valid_statuses:
            print(f"Error: Invalid status filter '{status_filter}'. Use: todo, in-progress, done")
            return
            
        list_tasks(status_filter)
        
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
