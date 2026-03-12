from datetime import datetime

tasks = []


# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass


# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Show dashboard
def show_dashboard():
    total = len(tasks)
    completed = sum(1 for t in tasks if "[x]" in t)
    pending = sum(1 for t in tasks if "[ ]" in t)

    print("\n===== Task Tracker Dashboard =====")
    print("Total Tasks:", total)
    print("Completed:", completed)
    print("Pending:", pending)
    print("==================================\n")


# Add task
def add_task():
    task = input("Enter new task: ")

    time = datetime.now().strftime("%d %b %Y %I:%M %p")

    task_entry = "[ ] " + task + " (Created: " + time + ")"

    tasks.append(task_entry)

    save_tasks()

    print("Task added successfully!\n")


# View tasks
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available.\n")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
        print()


# Mark task as completed
def complete_task():
    view_tasks()

    try:
        num = int(input("Enter task number to mark complete: "))

        if "[ ]" in tasks[num - 1]:
            tasks[num - 1] = tasks[num - 1].replace("[ ]", "[x]")

            save_tasks()

            print("Task marked as completed!\n")

        else:
            print("Task already completed.\n")

    except:
        print("Invalid task number.\n")


# Delete task
def delete_task():
    view_tasks()

    try:
        num = int(input("Enter task number to delete: "))

        tasks.pop(num - 1)

        save_tasks()

        print("Task deleted successfully!\n")

    except:
        print("Invalid task number.\n")


# Main menu
def main():

    load_tasks()

    while True:

        show_dashboard()

        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


# Run program
main()