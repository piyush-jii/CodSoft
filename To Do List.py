import json
import os

TODO_FILE = 'todo_list.json'

# Load tasks from file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Display all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    for i, task in enumerate(tasks):
        status = "✅" if task['completed'] else "❌"
        print(f"{i+1}. {task['task']} [{status}]")

# Add a task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({'task': task, 'completed': False})
    print("Task added!")

# Mark a task as complete
def complete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]['completed'] = True
        print("Task marked as complete.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Task '{removed['task']}' deleted.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == '__main__':
    main()
