class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False  # Initialize task as not completed

    def mark_completed(self):
        self.completed = True  # Mark the task as completed

    def mark_incomplete(self):
        self.completed = False  # Mark the task as incomplete

    def __str__(self):
        status = "✔️" if self.completed else "❌"
        return f"{status} {self.title}"  # Display task status and title


class TaskList:
    def __init__(self):
        self.tasks = []  # Initialize an empty list of tasks

    def add_task(self, title):
        new_task = Task(title)  # Create a new task
        self.tasks.append(new_task)  # Add the task to the list
        print(f"Task added: {new_task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)  # Remove task by index
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task index.")

    def edit_task(self, index, new_title):
        if 0 <= index < len(self.tasks):
            self.tasks[index].title = new_title  # Edit task title
            print(f"Task updated: {self.tasks[index]}")
        else:
            print("Invalid task index.")

    def toggle_task_completion(self, index):
        if 0 <= index < len(self.tasks):
            if self.tasks[index].completed:
                self.tasks[index].mark_incomplete()  # Mark as incomplete
            else:
                self.tasks[index].mark_completed()  # Mark as completed
            print(f"Task toggled: {self.tasks[index]}")
        else:
            print("Invalid task index.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Task List:")
            for index, task in enumerate(self.tasks):
                print(f"{index}: {task}")  # Display all tasks with their index


def main():
    task_list = TaskList()  # Create a new task list

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Edit Task")
        print("4. Toggle Task Completion")
        print("5. Show Tasks")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            title = input("Enter task title: ")
            task_list.add_task(title)
        elif choice == '2':
            task_list.show_tasks()
            index = int(input("Enter the task index to remove: "))
            task_list.remove_task(index)
        elif choice == '3':
            task_list.show_tasks()
            index = int(input("Enter the task index to edit: "))
            new_title = input("Enter new task title: ")
            task_list.edit_task(index, new_title)
        elif choice == '4':
            task_list.show_tasks()
            index = int(input("Enter the task index to toggle completion: "))
            task_list.toggle_task_completion(index)
        elif choice == '5':
            task_list.show_tasks()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()