import sys

from utils import add_task, complete_task, delete_task, view_tasks


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
        sys.exit()
