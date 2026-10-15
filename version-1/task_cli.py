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

def main():
    """Main entry point to parse command-line arguments."""
    # Check if a command was provided (sys.argv[0] is the script name itself)
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        return
        
    command = sys.argv[1]
    
    if command == "add":
        # Ensure the user provided a description for the task
        if len(sys.argv) < 3:
            print("Error: Please provide a description for the task.")
            return
        description = sys.argv[2]
        add_task(description)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
