from tasks_program import run_program

if __name__ == "__main__":
    print(""""
        ==== To-Do List ====

        1. View Uncompleted Tasks
        2. Add Task
        3. Complete Task
        4. Delete Task
        5. Search Task
        6. View Completed Tasks
        7. View Tasks Sorted Alphabetically
        8. Quit
    """)

    choice = input("What would you like to do? ")
    run_program(choice)
