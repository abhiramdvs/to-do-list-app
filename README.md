# To-Do List
The To-Do List App is a simple command-line-based application that allows users to manage their tasks effectively. Users can add new tasks, view existing tasks, and mark tasks as completed using this app.

# How to Run
1. Make sure you have Python installed on your computer.
2. Download or clone the repository to your local machine.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the following command to start the To-Do List App:
   
       python ToDo_List.py

# Features
**Add Task:** Users can add new tasks to their To-Do list. Each task can have a description and is set to not completed by default.
**View Tasks:** Users can view their current To-Do list, which displays the tasks along with their completion status.
**Complete Task:** Users can mark a task as completed once it's done. The completion status will be updated for the specific task.

# Usage
1. Upon running the app, you will be presented with a menu of options:

              Welcome to the To-Do List App!
              
              1. Add Task
              2. View Tasks
              3. Complete Task
              4. Exit
              Enter your choice (1/2/3/4):
1. To add a new task, choose option 1 and enter the task description when prompted.
2. To view the current tasks in your To-Do list, choose option 2.
3. To mark a task as completed, choose option 3 and enter the task number when prompted.
4. To exit the app, choose option 4.

# Data Storage
The app uses a file named "taskList.txt" to store the tasks. Each task is stored as a JSON-formatted dictionary on a new line in the file.

# Contributing
This is a simple project, but contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
