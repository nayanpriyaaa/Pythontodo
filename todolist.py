import json
import os

tasks =[]
filename = 'tasks.txt'

def load_tasks():
    global tasks
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            tasks = json.load(f)

def save_tasks():
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=4)

print("Hey!Welcome to-do list app \n")
load_tasks()

def addTask():
    task = input("Enter a task:")
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' is added to the list.")

def deleteTask():
    try: 
        todelete= int(input("Enter a # to delete "))
        if todelete>=0 and todelete< len(tasks):
            tasks.pop(todelete)
            print(f"Task #{todelete} has been removed.")
        else:
            print(f"Task #{todelete} was not found.")
    except:
            print("Invalid input.")

def viewTask():
    if not tasks:
       print("There are no tasks currently.")
    else:
       print("Current Tasks:")
       for index, task in enumerate(tasks):
         print(f"Task #{index}. {task}")

def checkoff():
      if not tasks:
        print("There are no tasks currently.")
      else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"Task #{index}. {task['task']} [{status}]")
        
        try:
            checkoff = int(input("Enter the task number to check off: "))
            if 0 <= checkoff < len(tasks):
                tasks[checkoff]["completed"] = True
                print(f"Task '{tasks[checkoff]['task']}' marked as completed.")
            else:
                print(f"Task #{checkoff} was not found.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

while True:
     print("What would you like to do today? \n")
     print("1. Add a task ")
     print("2. Delete a task")
     print("3. List tasks")
     print("4. Check off a task")
     print("5. Quit")
     req= input("Enter your choice: ")
     if req == "5":
        break
     if req == "1":
        addTask()
     elif req == "3" :
        viewTask()
     elif req== "2":
        deleteTask()
     elif req== "4":
        checkoff()
     else :
        print("Invalid request. Please Try Again")
        break
