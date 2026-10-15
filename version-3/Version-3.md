# 📋 Task Tracker CLI — Version 3

The third iteration of **Task Tracker CLI**, introducing task updates, deletion, and workflow status management.

Building on Version 1 (task creation) and Version 2 (task listing and filtering), Version 3 enables users to modify task descriptions, delete tasks, and manage task progress.

---

## 🚀 Version 3 Features

- **Task Creation (`add`):** Create tasks with auto-generated unique IDs and timestamps.
- **Task Listing & Filtering (`list`):** View all tasks or filter them by status: `todo`, `in-progress`, or `done`.
- **Description Updates (`update`):** Modify existing task descriptions and automatically refresh the `updatedAt` timestamp.
- **Task Deletion (`delete`):** Remove tasks permanently using their IDs.
- **Status Management (`mark-in-progress`, `mark-done`):** Update task workflow states effortlessly.
- **Persistent Local Storage:** Save changes to the local `tasks.json` file.

---

## 💻 Usage Guide

Ensure Python 3 is installed, then run the following commands in your terminal.

### 1. Add and List Tasks

```bash
python task_cli.py add "Buy groceries"
python task_cli.py add "Learn Python CLI"
python task_cli.py list
```

### 2. Update a Task Description

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

**Expected output:**

```text
Task 1 updated successfully.
```

### 3. Change Task Statuses

Mark a task as in progress:

```bash
python task_cli.py mark-in-progress 2
```

Mark a task as completed:

```bash
python task_cli.py mark-done 1
```

View completed tasks:

```bash
python task_cli.py list done
```

### 4. Delete a Task

```bash
python task_cli.py delete 2
```

**Expected output:**

```text
Task 2 deleted successfully.
```

---

## 🗂️ Data Storage

All tasks are stored locally in `tasks.json` with the following properties:

| Property | Description |
|---|---|
| `id` | Unique numeric task identifier. |
| `description` | Description of the task. |
| `status` | Current status: `todo`, `in-progress`, or `done`. |
| `createdAt` | Timestamp when the task was created. |
| `updatedAt` | Timestamp when the task was last modified. |

---

## 🛣️ What's Next in Version 4?

- Implement robust error handling for corrupted JSON files and unexpected edge cases.
- Validate invalid task IDs and missing command arguments.
- Add a built-in help menu with command usage instructions.

---

*Built with Python 3 as part of a progressive command-line application development project.*
