import sys

from utils import add_task, complete_task, delete_task, load_tasks, view_completed_tasks, view_tasks


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
        tasks = load_tasks()
        sorted_tasks = sorted(tasks, key=lambda x: x['title'])
        print("\nTasks Sorted Alphabetically:")
        for index, task in enumerate(sorted_tasks, start=1):
            print(f"{index}. {task}") 
    elif choice == "8":  
        tasks = load_tasks()
        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if task['completed'])
        uncompleted_tasks = total_tasks - completed_tasks
        percent_completed = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0

        print("\nStatistics:")
        print(f"Total tasks: {total_tasks}")
        print(f"Completed tasks: {completed_tasks}")
        print(f"Uncompleted tasks: {uncompleted_tasks}")
        print(f"Completion rate: {percent_completed:.2f}%") 
    elif choice == "9":
        sys.exit()
