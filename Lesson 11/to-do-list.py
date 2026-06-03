to_do_list = [
    "complete this review task",
    "Complete the len task",
    "Complete the in task",
    "Complete for loops tasks"
]

while True:
    user_input = input("Do you want to add or remove a task from the to-do list? (yes/no): ")
    if user_input == "yes":

    #Let user add to the list
        new_task = input("Enter a new task to add to the to-do list: ")
        to_do_list.append(new_task)
        print("Current to-do list:", to_do_list)

    #Let user remove from the list
        task_to_remove = input("Enter a task to remove from the to-do list: ")
        if task_to_remove in to_do_list:
            to_do_list.remove(task_to_remove)
            print("Current to-do list:", to_do_list)
    
    else:
        print("Final to-do list:", to_do_list)
        break