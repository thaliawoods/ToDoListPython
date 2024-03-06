# menu
def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark as Done")
    print("4. Exit") 

# add task
def add_task(tasks):
    task = input("Enter task : ")
    tasks.append(task)
    print("Task added !") 

# view task
def view_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}") 

# done
def mark_task_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return


    view_tasks(tasks)  
    index = int(input("Enter task index to mark as done: ")) - 1


    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' marked as done and removed.")
    else:
        print("Invalid task index.") 

# main
def main():
    tasks = [] 


    while True:
        display_menu()


        choice = input("Enter your choice: ")


        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()

