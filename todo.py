"""
CLI To-Do App
Usage:
  python todo.py add "Buy groceries"
  python todo.py list
  python todo.py complete 1
  python todo.py delete 1
"""

import argparse
import json
import os
from datetime import datetime

DATA_FILE = "todos.json"


# ---------- Storage ----------

def load_todos():
    """Load tasks from JSON file. Returns empty list if file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_todos(todos):
    """Persist tasks to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(todos, f, indent=2)


# ---------- Core logic ----------

def add_todo(title):
    todos = load_todos()
    todo = {
        "id": len(todos) + 1,
        "title": title,
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    todos.append(todo)
    save_todos(todos)
    print(f"✅ Added: \"{title}\"  (id={todo['id']})")


def list_todos():
    todos = load_todos()
    if not todos:
        print("📭 No tasks yet. Add one with: python todo.py add \"Your task\"")
        return

    print(f"\n{'ID':<5} {'Status':<10} {'Created':<18} Title")
    print("-" * 60)
    for t in todos:
        status = "✅ done" if t["done"] else "⬜ todo"
        print(f"{t['id']:<5} {status:<10} {t['created_at']:<18} {t['title']}")
    print()

    done_count = sum(1 for t in todos if t["done"])
    print(f"  {done_count}/{len(todos)} completed\n")


def complete_todo(todo_id):
    todos = load_todos()
    for t in todos:
        if t["id"] == todo_id:
            if t["done"]:
                print(f"ℹ️  Task {todo_id} is already marked as done.")
                return
            t["done"] = True
            save_todos(todos)
            print(f"✅ Completed: \"{t['title']}\"")
            return
    print(f"❌ No task found with id={todo_id}")


def delete_todo(todo_id):
    todos = load_todos()
    original_len = len(todos)
    todos = [t for t in todos if t["id"] != todo_id]
    if len(todos) == original_len:
        print(f"❌ No task found with id={todo_id}")
        return
    save_todos(todos)
    print(f"🗑️  Deleted task id={todo_id}")


def clear_done():
    todos = load_todos()
    remaining = [t for t in todos if not t["done"]]
    removed = len(todos) - len(remaining)
    if removed == 0:
        print("ℹ️  No completed tasks to clear.")
        return
    save_todos(remaining)
    print(f"🧹 Cleared {removed} completed task(s).")


# ---------- CLI wiring ----------

def main():
    parser = argparse.ArgumentParser(
        description="A simple CLI to-do app",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python todo.py add \"Buy groceries\"\n"
            "  python todo.py list\n"
            "  python todo.py complete 1\n"
            "  python todo.py delete 1\n"
            "  python todo.py clear-done\n"
        ),
    )

    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task description")

    # list
    subparsers.add_parser("list", help="Show all tasks")

    # complete
    complete_parser = subparsers.add_parser("complete", help="Mark a task as done")
    complete_parser.add_argument("id", type=int, help="Task ID")

    # delete
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # clear-done
    subparsers.add_parser("clear-done", help="Remove all completed tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_todo(args.title)
    elif args.command == "list":
        list_todos()
    elif args.command == "complete":
        complete_todo(args.id)
    elif args.command == "delete":
        delete_todo(args.id)
    elif args.command == "clear-done":
        clear_done()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
