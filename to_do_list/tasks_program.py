import sys

from utils import add_task, complete_task, delete_task, view_completed_tasks, view_tasks


def run_program(choice):
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        search_term = input("Enter a search term: ").strip().lower()
        tasks = view_tasks()
        matching_tasks = [task for task in tasks if search_term in task.lower()]

        if matching_tasks:
            print("\nMatching Tasks:")
            for index, task in enumerate(matching_tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No matching tasks found.")
    elif choice == "6":
        view_completed_tasks()
    elif choice == "7":
        sys.exit()
