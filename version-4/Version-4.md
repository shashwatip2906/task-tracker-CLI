# 📋 Task Tracker CLI — Version 4 (Final Release)

The final release of **Task Tracker CLI**, a lightweight, zero-dependency command-line application built in Python.

Version 4 completes the application with robust error handling, JSON recovery, input validation, and a built-in help guide for a smoother user experience.

---

## 🚀 Version 4 Features & Enhancements

- **Complete Task Lifecycle:** Add, update, delete, and manage tasks.
- **Workflow Progress Tracking:** Manage task statuses: `todo`, `in-progress`, and `done`.
- **Flexible Listing & Filtering:** View all tasks or filter them by status.
- **Robust JSON Recovery:** Detect and handle corrupted or empty `tasks.json` files gracefully.
- **Advanced Input Validation:** Validate numeric task IDs and prevent empty task descriptions.
- **Built-In Help Guide:** Display usage instructions when the script runs without arguments.
- **Persistent Local Storage:** Save task records in `tasks.json`.
- **Zero Dependencies:** Built exclusively with Python's standard libraries: `sys`, `os`, `json`, and `datetime`.

---

## 💻 Usage & Command Guide

Ensure Python 3 is installed, then execute the following commands in your terminal.

### 1. View the Help Menu

```bash
python task_cli.py
```

### 2. Add a Task

```bash
python task_cli.py add "Buy groceries and cook dinner"
```

**Example output:**

```text
Task added successfully (ID: 1)
```

### 3. List Tasks

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

### 4. Update a Task Description

```bash
python task_cli.py update 1 "Buy groceries, cook dinner, and clean the kitchen"
```

**Example output:**

```text
Task 1 updated successfully.
```

### 5. Change Task Status

Mark a task as in progress:

```bash
python task_cli.py mark-in-progress 1
```

Mark a task as completed:

```bash
python task_cli.py mark-done 1
```

### 6. Delete a Task

```bash
python task_cli.py delete 1
```

**Example output:**

```text
Task 1 deleted successfully.
```

---

## 🗂️ Task Properties (`tasks.json`)

Each task is stored locally as a structured JSON object.

### Example JSON Structure

```json
[
    {
        "id": 1,
        "description": "Buy groceries",
        "status": "todo",
        "createdAt": "2026-10-15T11:43:00.123456",
        "updatedAt": "2026-10-15T11:43:00.123456"
    }
]
```

### Field Descriptions

| Property | Description |
|---|---|
| `id` | Unique numeric identifier for each task. |
| `description` | Text describing the task. |
| `status` | Current state: `todo`, `in-progress`, or `done`. |
| `createdAt` | Timestamp when the task was created. |
| `updatedAt` | Timestamp when the task was last modified. |

---

## 🛠️ Built With

- **Language:** Python 3
- **Libraries:** `sys`, `os`, `json`, `datetime`
- **Storage:** Local JSON file
- **Dependencies:** None

---

## 📄 License

This project is intended to be released under the MIT License. Add a `LICENSE` file to the repository if you choose this license.

---

*Built with Python 3 to demonstrate command-line development, file handling, JSON persistence, input validation, and error handling.*
