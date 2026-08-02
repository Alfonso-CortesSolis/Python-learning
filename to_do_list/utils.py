import json
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.json")


def _normalize_completed(value):
    if isinstance(value, bool):
        return value

    if isinstance(value, str):
        return value.strip().lower() == "true"

    return bool(value)


def _normalize_tasks(tasks):
    if isinstance(tasks, list):
        normalized = []
        for task in tasks:
            if isinstance(task, dict):
                normalized.append(
                    {
                        "title": task.get("title", ""),
                        "completed": _normalize_completed(task.get("completed", False)),
                    }
                )
            elif isinstance(task, str):
                normalized.append({"title": task, "completed": False})
        return normalized

    if isinstance(tasks, dict):
        return [
            {
                "title": tasks.get("title", ""),
                "completed": _normalize_completed(tasks.get("completed", False)),
            }
        ]

    if isinstance(tasks, str):
        return [{"title": tasks, "completed": False}]

    return []


def load_tasks():
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            return _normalize_tasks(json.load(file))
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    normalized_tasks = _normalize_tasks(tasks)

    with TASKS_FILE.open("w", encoding="utf-8") as file:
        json.dump(normalized_tasks, file, indent=2)


def view_tasks():
    tasks = load_tasks()
    pending_titles = []

    if not tasks:
        print("No tasks found.")
        return pending_titles

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        if not task.get("completed", False):
            pending_titles.append(task["title"])
            print(f"{index}. {task['title']}")
    print()
    return pending_titles


def view_completed_tasks():
    tasks = load_tasks()
    pending_titles = []

    if not tasks:
        print("No tasks found.")
        return pending_titles

    print("\nYour CompletedTasks:")
    for index, task in enumerate(tasks, start=1):
        if task.get("completed", True):
            pending_titles.append(task["title"])
            print(f"{index}. {task['title']}")
    print()
    return pending_titles


def add_task():
    title = input("Enter the task title: ").strip()
    if title:
        tasks = load_tasks()
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(f"Task '{title}' added.")
    else:
        print("Task title cannot be empty.")


def complete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[task_number - 1]['title']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
