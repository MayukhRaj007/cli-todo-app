"""
Unit tests for todo.py
Run with: python -m pytest tests/
"""

import os
import pytest
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import todo


@pytest.fixture(autouse=True)
def use_test_file(monkeypatch, tmp_path):
    """Redirect DATA_FILE to a temp location so tests don't touch todos.json."""
    test_data = tmp_path / "todos.json"
    monkeypatch.setattr(todo, "DATA_FILE", str(test_data))
    yield


def test_add_creates_task(capsys):
    todo.add_todo("Test task")
    todos = todo.load_todos()
    assert len(todos) == 1
    assert todos[0]["title"] == "Test task"
    assert todos[0]["done"] is False


def test_add_multiple_tasks():
    todo.add_todo("Task A")
    todo.add_todo("Task B")
    todos = todo.load_todos()
    assert len(todos) == 2
    assert todos[1]["title"] == "Task B"


def test_complete_marks_task_done():
    todo.add_todo("Finish project")
    todo.complete_todo(1)
    todos = todo.load_todos()
    assert todos[0]["done"] is True


def test_complete_nonexistent_id(capsys):
    todo.complete_todo(999)
    captured = capsys.readouterr()
    assert "No task found" in captured.out


def test_delete_removes_task():
    todo.add_todo("To delete")
    todo.delete_todo(1)
    todos = todo.load_todos()
    assert len(todos) == 0


def test_clear_done_removes_only_completed():
    todo.add_todo("Keep me")
    todo.add_todo("Delete me")
    todo.complete_todo(2)
    todo.clear_done()
    todos = todo.load_todos()
    assert len(todos) == 1
    assert todos[0]["title"] == "Keep me"


def test_load_returns_empty_when_no_file():
    todos = todo.load_todos()
    assert todos == []
