tasks = []


while True: 
    print('1.Add Task')
    print('2.Delete Task')
    print('3.Update Task')
    print('4.Exit')

        #This fuction is to add user input to add a description to the task list.
    Choice = input('Choose a option: ')
    if Choice == '1':
        tasks_description = input('Please enter the task description: ')
        tasks.append(tasks_description)
        print('Task Added Successfully!')

        # option to remove task by task name, and by numric location in list.
    elif Choice == '2':
        task_to_remove = input('Enter the task to remove(by description): ')
        if task_to_remove in tasks: 
            tasks.remove(task_to_remove)
            print(f'Removed Task:{task_to_remove}')
        else:
            try:
                task_index = int(input('Enter the index of task to be removed: '))-1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f'Removed Task: {removed_task}')
                else:
                    print('Invalid index.')
            except ValueError:
                print('Please enter a valid number for the index.')


    elif Choice == '3':
        print('current task: ')
        for i, tasks in enumerate(tasks, start=1):
            print(f"{i}.{tasks}")
        try:
            task_index  = int(input('Enter the index of task to be removed: '))-1
            if 0 <= task_index < len(tasks):
                new_task = int('Enter new description or task: ')
                tasks[task_index] = new_task
                print('task updated successfully!')
            else: 
                print('invalid index')
        except ValueError:
            print('Please enter a valid number for the index.')

       
    elif Choice  == '4':
        print('Exiting...')
        break

    else: 
        print('error: Invalid input.')
