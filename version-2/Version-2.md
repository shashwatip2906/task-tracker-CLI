# 📋 Task Tracker CLI — Version 2

The second iteration of **Task Tracker CLI**, expanding the lightweight Python application with task viewing and filtering capabilities.

Building on Version 1's task creation and data persistence, Version 2 introduces the `list` command to display all tasks or filter them by status.

---

## 🚀 Version 2 Features

- **Task Creation (`add`):** Add tasks with automatically generated unique IDs and timestamps.
- **Full Task Listing (`list`):** Display tasks in a formatted terminal table showing ID, status, description, and creation time.
- **Status-Based Filtering (`list <status>`):** Filter tasks by workflow state: `todo`, `in-progress`, or `done`.
- **Persistent Local Storage:** Store and retrieve tasks using a local `tasks.json` file.
- **Zero Dependencies:** Built exclusively with Python's standard libraries: `sys`, `os`, `json`, and `datetime`.

---

## 💻 Usage Guide

Ensure Python 3 is installed and run the following commands in your terminal.

### 1. Add Tasks

```bash
python task_cli.py add "Buy groceries"
python task_cli.py add "Read a data science chapter"
python task_cli.py add "Write Python script"
```

### 2. View All Tasks

```bash
python task_cli.py list
```

**Example Output:**

```text
ID   | Status       | Description                    | Created At
---------------------------------------------------------------------------
1    | todo         | Buy groceries                  | 2026-10-15T11:43:00
2    | todo         | Read a data science chapter    | 2026-10-15T11:43:10
3    | todo         | Write Python script            | 2026-10-15T11:43:25
```

### 3. Filter Tasks by Status

View tasks that need to be completed:

```bash
python task_cli.py list todo
```

View tasks currently in progress:

```bash
python task_cli.py list in-progress
```

View completed tasks:

```bash
python task_cli.py list done
```

---

## 🗂️ Data Storage

Tasks are stored in `tasks.json`. Each task contains the following fields:

| Property | Description |
|---|---|
| `id` | Unique numeric task identifier. |
| `description` | Task description. |
| `status` | Current status: `todo`, `in-progress`, or `done`. |
| `createdAt` | Timestamp when the task was created. |
| `updatedAt` | Timestamp when the task was last modified. |

---

## 🛣️ What's Next in Version 3?

- Implement task description updates using `update`.
- Add task deletion using `delete`.
- Introduce status-transition commands: `mark-in-progress` and `mark-done`.

---

*Built with Python 3 as part of a progressive command-line application development project.*
