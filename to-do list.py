import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task(tasks):
    name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High, Medium, Low): ")
    tasks.append({"name": name, "due_date": due_date, "priority": priority})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if tasks:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['name']} (Due: {task['due_date']}, Priority: {task['priority']})")
    else:
        print("No tasks found.")

def update_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["name"] = input("Enter updated task name: ")
            tasks[index]["due_date"] = input("Enter updated due date (YYYY-MM-DD): ")
            tasks[index]["priority"] = input("Enter updated priority (High, Medium, Low): ")
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def main():
    tasks = load_tasks()
    while True:
        print("\n======= To-Do List =======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
