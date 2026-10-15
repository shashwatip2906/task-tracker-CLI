# 📋 Task Tracker CLI

A lightweight, zero-dependency command-line application built in Python to track and manage daily tasks efficiently.

This project demonstrates core software engineering principles, including command-line argument parsing, file system interaction, JSON data persistence, and robust error handling.

---

## 🚀 Features

- **Task Lifecycle Management:** Add, update, and delete tasks with auto-generated unique IDs.
- **Workflow Progress Tracking:** Mark tasks as `todo`, `in-progress`, or `done`.
- **Flexible Listing Views:** View all tasks or filter them by status.
- **Persistent Local Storage:** Automatically initializes and manages a local `tasks.json` file.
- **Robust Error Handling:** Handles invalid inputs, missing arguments, non-integer IDs, and corrupted JSON files with helpful error messages.

---

## 🛠️ Built With

- **Python 3**
- **Standard Library:** `sys`, `os`, `json`, `datetime`

No external libraries or frameworks required.
Project-URL: https://github.com/shashwatip2906/task-tracker-CLI

---

## 💻 Installation & Getting Started

1. Ensure Python 3 is installed on your system.
2. Clone the repository:

   ```bash
   git clone https://github.com/your-username/task-tracker-cli.git
   ```

3. Navigate to the project directory:

   ```bash
   cd task-tracker-cli
   ```

4. Run the application using Python.

---

## 📖 Usage Guide

### 1. Add a Task

```bash
python task_cli.py add "Buy groceries and cook dinner"
```

**Output:**
```text
Task added successfully (ID: 1)
```

### 2. List Tasks

View all tasks:

```bash
python task_cli.py list
```

Filter tasks by status:

```bash
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

### 3. Update a Task Description

```bash
python task_cli.py update 1 "Buy groceries, cook dinner, and wash dishes"
```

**Output:**
```text
Task 1 updated successfully.
```

### 4. Change Task Status

Mark a task as in progress:

```bash
python task_cli.py mark-in-progress 1
```

Mark a task as completed:

```bash
python task_cli.py mark-done 1
```

### 5. Delete a Task

```bash
python task_cli.py delete 1
```

**Output:**
```text
Task 1 deleted successfully.
```

---

## 📂 Task Properties (`tasks.json`)

Each task is stored locally as a structured JSON object.

### Example

```json
{
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2026-10-15T11:30:00.123456",
    "updatedAt": "2026-10-15T11:30:00.123456"
}
```

### Field Descriptions

| Property | Description |
|---|---|
| `id` | A unique, auto-incrementing numeric identifier. |
| `description` | A text description of the task. |
| `status` | The current task status: `todo`, `in-progress`, or `done`. |
| `createdAt` | The ISO-formatted timestamp when the task was created. |
| `updatedAt` | The ISO-formatted timestamp when the task was last modified. |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to open an issue or submit a pull request to improve the project.

---

## 📄 License

This project is open source and available under the **MIT License**.
