tasks = []
completed = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            task_data = line.strip().split("|")
            if len(task_data) == 2:
                task, status = task_data
                tasks.append(task)
                completed.append(status == "True")
except FileNotFoundError:
    pass

print("Welcome to the To-Do List Manager!")
print("Options: add, show, delete, complete, q to quit")

while True:
    action = input("What would you like to do? ").strip().lower()

    if action == 'q':
        with open("tasks.txt", "w") as file:
            for i in range(len(tasks)):
                file.write(f"{tasks[i]}|{completed[i]}\n")
        print("Tasks saved. Exiting program...")
        break

    if action == 'add':
        task = input("Enter the task: ").strip()
        if task:
            tasks.append(task)
            completed.append(False)
            print("Task added:", task)
        else:
            print("Task cannot be empty!")

    elif action == 'show':
        if not tasks:
            print("No tasks in the list.")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):
                status = "✔" if completed[i] else " "
                print(f"{i + 1}. [{status}] {tasks[i]}")

    elif action == 'delete':
        if not tasks:
            print("No tasks to delete.")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):
                status = "✔" if completed[i] else " "
                print(f"{i + 1}. [{status}] {tasks[i]}")
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    completed.pop(index)
                    print("Task deleted:", removed_task)
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    elif action == 'complete':
        if not tasks:
            print("No tasks to mark as complete.")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):
                status = "✔" if completed[i] else " "
                print(f"{i + 1}. [{status}] {tasks[i]}")
            try:
                index = int(input("Enter the task number to mark as complete: ")) - 1
                if 0 <= index < len(tasks):
                    if completed[index]:
                        print("Task is already marked as complete!")
                    else:
                        completed[index] = True
                        print("Task marked as complete:", tasks[index])
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

    else:
        print("Invalid option! Use add, show, delete, complete, or q to quit.")