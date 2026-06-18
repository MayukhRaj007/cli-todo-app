# CLI To-Do App

A lightweight command-line task manager built with Python. No external libraries required — just Python's standard library.

## Features

- Add tasks with a title
- List all tasks with status and creation time
- Mark tasks as complete
- Delete individual tasks
- Clear all completed tasks
- Data persisted locally in JSON

## Usage

```bash
# Add a task
python todo.py add "Buy groceries"

# List all tasks
python todo.py list

# Mark task #1 as done
python todo.py complete 1

# Delete task #2
python todo.py delete 2

# Remove all completed tasks
python todo.py clear-done

# Show help
python todo.py --help
```

## Example output

```
ID    Status     Created            Title
------------------------------------------------------------
1     ✅ done     2026-06-18 17:00   Buy groceries
2     ⬜ todo     2026-06-18 17:01   Write README
3     ⬜ todo     2026-06-18 17:01   Push to GitHub

  1/3 completed
```

## Project structure

```
cli-todo-app/
├── todo.py          # Main application
├── tests/
│   └── test_todo.py # Unit tests
└── README.md
```

## Running tests

```bash
python -m pytest tests/
```

## What I learned

- CLI argument parsing with `argparse`
- JSON file I/O for simple persistence
- Structuring a Python CLI project
- Writing a useful README

## Tech stack

- Python 3.8+
- No external dependencies

---

Part of my [50 GitHub Projects](https://github.com/MayukhRaj007) portfolio challenge.
