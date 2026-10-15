import sys
import os
import json
from datetime import datetime

# Define the file where tasks will be stored
TODO_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file with robust error handling for corrupted data."""
    if not os.path.exists(TODO_FILE):
        return []
    try:
        with open(TODO_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        print("Warning: 'tasks.json' was corrupted or invalid. Initializing empty task list.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def save_tasks(tasks):
    """Save the list of tasks back to the JSON file with pretty formatting."""
    try:
        with open(TODO_FILE, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(description):
    """Add a new task to the list and save it."""
    description = description.strip()
    if not description:
        print("Error: Task description cannot be empty.")
        return

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
    """List all tasks, or filter them by status if provided, with formatted output."""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return

    if status_filter:
        tasks = [t for t in tasks if t["status"] == status_filter]
        if not tasks:
            print(f"No tasks found with status '{status_filter}'.")
            return

    # Print clean table header
    print(f"{'ID':<4} | {'Status':<12} | {'Description':<35} | {'Created At'}")
    print("-" * 75)
    
    for task in tasks:
        created_at = task['createdAt'].split('.')[0]
        # Truncate overly long descriptions for clean display
        desc = task['description']
        if len(desc) > 33:
            desc = desc[:30] + "..."
        print(f"{task['id']:<4} | {task['status']:<12} | {desc:<35} | {created_at}")

def update_task(task_id, new_description):
    """Update an existing task's description and updatedAt timestamp."""
    new_description = new_description.strip()
    if not new_description:
        print("Error: Updated description cannot be empty.")
        return

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
            if task["status"] == new_status:
                print(f"Notice: Task {task_id} is already marked as '{new_status}'.")
                return
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {new_status}.")
            return
    print(f"Error: Task with ID {task_id} not found.")

def print_help():
    """Print usage instructions for the CLI."""
    print("Task Tracker CLI - Usage Guide:")
    print("  python task_cli.py add \"<description>\"           Add a new task")
    print("  python task_cli.py list                            List all tasks")
    print("  python task_cli.py list <status>                   List tasks by status (todo, in-progress, done)")
    print("  python task_cli.py update <id> \"<description>\"     Update task description")
    print("  python task_cli.py delete <id>                     Delete a task")
    print("  python task_cli.py mark-in-progress <id>           Mark task as in-progress")
    print("  python task_cli.py mark-done <id>                  Mark task as done")

def main():
    """Main entry point to parse command-line arguments safely."""
    if len(sys.argv) < 2:
        print_help()
        return
        
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 3:
            print("Error: Please provide a description for the task.")
            print("Usage: python task_cli.py add \"Buy groceries\"")
            return
        add_task(sys.argv[2])
        
    elif command == "list":
        status_filter = sys.argv[2] if len(sys.argv) > 2 else None
        valid_statuses = ["todo", "in-progress", "done"]
        if status_filter and status_filter not in valid_statuses:
            print(f"Error: Invalid status filter '{status_filter}'.")
            print("Valid statuses are: todo, in-progress, done")
            return
        list_tasks(status_filter)
        
    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: Please provide both task ID and new description.")
            print("Usage: python task_cli.py update <id> \"New description\"")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print(f"Error: Invalid Task ID '{sys.argv[2]}'. ID must be an integer.")
            return
        update_task(task_id, sys.argv[3])
        
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Please provide a task ID to delete.")
            print("Usage: python task_cli.py delete <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print(f"Error: Invalid Task ID '{sys.argv[2]}'. ID must be an integer.")
            return
        delete_task(task_id)
        
    elif command in ["mark-in-progress", "mark-done"]:
        if len(sys.argv) < 3:
            print(f"Error: Please provide a task ID for '{command}'.")
            print(f"Usage: python task_cli.py {command} <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print(f"Error: Invalid Task ID '{sys.argv[2]}'. ID must be an integer.")
            return
        
        status_map = {
            "mark-in-progress": "in-progress",
            "mark-done": "done"
        }
        update_status(task_id, status_map[command])
        
    else:
        print(f"Unknown command: '{command}'")
        print("Run 'python task_cli.py' without arguments to see the usage guide.")

if __name__ == "__main__":
    main()
