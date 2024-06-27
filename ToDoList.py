def add():
    print("Enter the task you wanna add")
    task=input()
    to_do_list.append({"TASK":task,"STATUS":"Not Done"})
    print("You have successfully added a new task!")
    
def remove():
    print("Enter the task number you wanna remove")
    task=int(input())
    if task>len(to_do_list):
        print("Invalid task number")
    else:
        to_do_list.pop(task-1)
        print("The task has been removed successfully!")
    
def done():
    print("Enter the task you wanna mark as done")
    t=input()
    for task in to_do_list:
        if task["TASK"] == t:
            task["STATUS"]="Done"
            print("Task has been marked as done!")
        else:
            print("Task not found!")
    
def view():
    if(len(to_do_list)==0):
        print("Your To Do List Is Empty")
    else:
        for task in to_do_list:
            if task['STATUS']=='Done':
                status="\u2714"
            else:
                status="\u274C"
            print(f"Task:{task['TASK']},Status:{status}")

def clear():
    to_do_list.clear()
    print("There is no task in your to do lisk now!")
    
print("Enter 1 to create a to do list")
create_list=int(input())
if(create_list==1):
    to_do_list=[]
    
while(True):
    print("\nWANNA UPDATE YOUR LIST?")
    print("Enter your choice:")
    print("1.Add Task")
    print("2.Remove Task")
    print("3.Mark A Task As Done")
    print("4.View Tasks List")
    print("5.Clear The Tasks List")
    print("6.Exit\n")
    choice=int(input())
    if choice == 1 :
        add()
    elif choice == 2 :
        remove()
    elif choice == 3 :
        done()
    elif choice == 4 :
        view()
    elif choice == 5 :
        clear()
    elif choice == 6 :
        print("THANKS FOR USING TO_DO_LIST APP")
        break
    else:
        print("OOPS! Invalid Choice!\nChoice must be from 1 to 5")    
         
    