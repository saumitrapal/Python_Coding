#TODO APPLICATION

task_list = []


# add task in list
def add_task():
    user_task = input("Enter task: ")
    task_list.append(user_task)
    print(task_list)

# remove task from list
def remove_task():
    user_task = (int(input("Enter the task no: ")) - 1)

    task_list.pop(user_task)    #delete from list using index
    print(task_list)
    
    
    
task_continue = True
while task_continue:
    user_option = input("Enter option: ").lower()

    if user_option == "add":
        add_task()
    elif user_option == "remove":
        remove_task()
    
    continue_operation = input("Do you continue your operation(yes/ no): ").lower()
    if continue_operation == "yes":
        continue
    else:
        break

    
