todo_list = [] 


def add_task():
    task = input("Enter the new task : ")
    todo_list.append({"task" : task , "status" : "pending"})
    print("New task added") 

def view_task():
    if len(todo_list) == 0 :
        print("No Task There")
    else:
        for index , task in enumerate(todo_list , 1):
            print(f"{index} : {task['task']} - {task['status']}")
    print("\n")

def delete_task():
    if len(todo_list) == 0 :
        print("No Task To Delete")
    else:
        try:
            index = int(input("Enter the index of task to delete : ")) - 1 
            if index >= len(todo_list) :
                print("No Task To Delete Of that Index")
            else:
                removed_task = todo_list.pop(index) 
                print(f"Removed Task : {removed_task['task']}")
        except ValueError:
            print("Enter Valid Task Number . ")

def mark_task_done():
    if len(todo_list) == 0 :
        print("No Task To Mark Done")
    else: 
        try:
            index = int(input("Enter the index of task to mark as done : ")) - 1 
            if index < 0 or index >= len(todo_list) :
                print("No Task To Mark Done Of that Index")
            else:
                todo_list[index]['status'] = "done"
                print(f"{todo_list[index]['task']} : {todo_list[index]['status']}")
        except ValueError:
            print("Enter Valid Task Number . ")

def menu():
    while(True) :
        print("* * * MAIN OPTION * * *")
        print("1. add a new task")
        print("2. view all task")
        print("3. delete a task")
        print("4. mark as complete")
        print("5. exit")
        try:
            choice = int(input("Enter Your Choice : "))
        except ValueError:
            print("Please enter a number")
            continue
        if(choice == 1):
            add_task() 
        elif(choice == 2):
            view_task()
        elif(choice == 3):
            delete_task() 
        elif(choice == 4):
            mark_task_done()
        elif(choice == 5):
            print("Goodbye!")
            break
        else:
            print("invalid input")

menu()