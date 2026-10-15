# 📋 Task Tracker CLI — Version 1

The foundational release of **Task Tracker CLI**, a lightweight, zero-dependency command-line application built in Python.

Version 1 establishes the core architecture: project setup, automatic local JSON file initialization, command-line argument parsing, and task creation.

---

## 🚀 Version 1 Features

- **Automated Storage Initialization:** Creates `tasks.json` in the current directory if it doesn't exist.
- **Add Task Command:** Accepts task descriptions through command-line arguments.
- **Auto-Incrementing IDs:** Generates unique numeric identifiers for new tasks.
- **Structured JSON Records:** Stores tasks with metadata: `id`, `description`, `status`, `createdAt`, and `updatedAt`.
- **Zero Dependencies:** Uses only Python's standard libraries: `sys`, `os`, `json`, and `datetime`.

---

## 💻 Quick Start & Usage

Ensure Python 3 is installed, then run the following command in your terminal:

```bash
python task_cli.py add "Buy groceries"
```

**Expected output:**

```text
Task added successfully (ID: 1)
```

---

## 🗂️ Task Properties (`tasks.json`)

Each task is stored in the local `tasks.json` file using the following structure:

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
| `id` | Unique numeric identifier for the task. |
| `description` | Description of the task. |
| `status` | Initial task status, set to `todo`. |
| `createdAt` | Timestamp when the task was created. |
| `updatedAt` | Timestamp when the task was last modified. |

---

## 🛣️ What's Next in Version 2?

- Implement the `list` command to display all tasks.
- Add status-based filtering: `todo`, `in-progress`, and `done`.

---

*Built with Python 3 as part of a progressive command-line application development project.*
