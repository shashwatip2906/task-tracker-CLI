# 📋 Task Tracker CLI

A lightweight, zero-dependency command-line interface (CLI) application built in Python to track and manage your daily tasks efficiently. 

Designed entirely without external libraries or frameworks, this project demonstrates core software engineering principles including terminal argument parsing, native file system interaction, structured JSON data persistence, and robust error handling.

---

## 🚀 Features

- **Task Lifecycle Management:** Add, update, and delete tasks seamlessly with auto-generated unique IDs.
- **Workflow Progress Tracking:** Update task states by marking them as `todo`, `in-progress`, or `done`.
- **Flexible Listing Views:** View all active tasks at a glance or filter them instantly by status.
- **Persistent Local Storage:** Automatically initializes and manages a local `tasks.json` file in the current directory.
- **Robust Error Handling:** Gracefully handles invalid inputs, missing arguments, non-integer IDs, and corrupted JSON files with helpful usage prompts.

---

## 🛠️ Built With

- **Python 3** (Uses Python Standard Library only: `sys`, `os`, `json`, `datetime`)

---

## 💻 Installation & Getting Started

1. Ensure you have **Python 3** installed on your system.
2. Clone this repository or download the `task_cli.py` script into your project directory:
   ```bash
   git clone [https://github.com/your-username/task-tracker-cli.git](https://github.com/your-username/task-tracker-cli.git)
   cd task-tracker-cli
📖 Usage Guide
Run commands directly from your terminal using Python:

1. Add a Task
Bash
python task_cli.py add "Buy groceries and cook dinner"
# Output: Task added successfully (ID: 1)
2. List Tasks
Bash
# View all tasks
python task_cli.py list

# Filter tasks by status (valid options: todo, in-progress, done)
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
3. Update a Task Description
Bash
python task_cli.py update 1 "Buy groceries, cook dinner, and wash dishes"
# Output: Task 1 updated successfully.
4. Change Task Status
Bash
# Mark a task as in-progress
python task_cli.py mark-in-progress 1

# Mark a task as done
python task_cli.py mark-done 1
5. Delete a Task
Bash
python task_cli.py delete 1
# Output: Task 1 deleted successfully.
## Task Properties (tasks.json)
Each task is stored locally as a structured JSON object with the following schema:

JSON
{
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-10-15T11:30:00.123456",
    "updatedAt": "2026-10-15T11:30:00.123456"
}
id: A unique auto-incrementing numeric identifier.

description: Text description of the task.

status: The current state of the task (todo, in-progress, done).

createdAt: ISO timestamp when the task was created.

updatedAt: ISO timestamp when the task was last modified.

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page or submit a pull request.

## License
This project is open source and available under the MIT License.
