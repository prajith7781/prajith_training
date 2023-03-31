import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def read_tasks():
    """Reads the tasks from the file and returns a list of tasks."""
    tasks = []
    with open('pyex.txt', 'r') as f:
        for line in f:
            tasks.append(line.strip())
    return tasks

def write_tasks(tasks):
    """Writes the tasks to the file."""
    with open('pyex.txt', 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def print_tasks(tasks):
    """Prints the tasks to the console."""
    print('Tasks:')
    for i, task in enumerate(tasks):
        print(f'{i + 1}. {task}')

def add_task():
    """Adds a new task to the list."""
    clear_screen()
    task = input('Enter a new task: ')
    tasks = read_tasks()
    tasks.append(task)
    write_tasks(tasks)
    print('Task added successfully!')

def update_task():
    """Updates an existing task in the list."""
    clear_screen()
    tasks = read_tasks()
    print_tasks(tasks)
    task_index = int(input('Enter the number of the task to update: ')) - 1
    new_task = input('Enter the new task: ')
    tasks[task_index] = new_task
    write_tasks(tasks)
    print('Task updated successfully!')

def delete_task():
    """Deletes an existing task from the list."""
    clear_screen()
    tasks = read_tasks()
    print_tasks(tasks)
    task_index = int(input('Enter the number of the task to delete: ')) - 1
    del tasks[task_index]
    write_tasks(tasks)
    print('Task deleted successfully!')

def main():
    """The main function that runs the application."""
    while True:
        clear_screen()
        tasks = read_tasks()
        print_tasks(tasks)
        print('\nMenu:')
        print('1. Add task')
        print('2. Update task')
        print('3. Delete task')
        print('4. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            add_task()
        elif choice == '2':
            update_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            clear_screen()
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
