import json

tasks = []


# Function to add the task
def addTask(task):
    f1 = open("taskList.txt", "a")
    td = {"task": task, "completed": False}
    f1.write(json.dumps(td) + "\n")
    print("Task", task, " added to the To-Do list.")
    f1.close()


# Function to view the tasks
def viewTasks():
    f2 = open("taskList.txt", "r")
    lines = f2.readlines()
    if not lines:
        print("To-Do list is empty.")
    else:
        print("To-Do List:")
        for i, task_line in enumerate(lines, start=1):
            task = json.loads(task_line.strip())
            if task["completed"]:
                status = "✓"
            else:
                status = " "
            print(f"{i}. [{status}] {task['task']}")
        f2.close()


# Function to mark the task as completed
def completeTask(task_index):
    f3 = open("taskList.txt", "r")
    lines = f3.readlines()
    f3.close()

    if 1 <= task_index <= len(lines):
        task = json.loads(lines[task_index - 1].strip())
        task["completed"] = True
        lines[task_index - 1] = json.dumps(task) + "\n"
        f4 = open("taskList.txt", "w")
        f4.writelines(lines)
        print(f"Task '{task['task']}' marked as completed.")
        f4.close()
    else:
        print("Invalid task number.")


def main():
    print("Welcome to the To-Do List App!")
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task description: ")
            addTask(task)

        elif choice == '2':
            viewTasks()

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as complete: "))
            completeTask(task_index)

        elif choice == '4':
            print("Thank you for using!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
