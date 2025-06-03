import os

TODO_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

# Show menu
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

# Main app loop
def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks found.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            new_task = input("Enter the new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added.")

        elif choice == "3":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to mark as complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1] = "✅ " + tasks[task_num - 1]
                    save_tasks(tasks)
                    print("Task marked as complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Deleted task: {deleted}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
