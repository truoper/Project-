class Task:
    def __init__(self, name, description, status='ToDo'):
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.name} - {self.status}\nDescription: {self.description}"

class ProjectManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)

    def update_status(self, task_name, new_status):
        for task in self.tasks:
            if task.name == task_name:
                task.status = new_status
                print(f"Task '{task_name}' status updated to '{new_status}'")
                return
        print(f"Task '{task_name}' not found")

def main():
    project_manager = ProjectManager()
    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Update Task Status\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            project_manager.add_task(name, description)
        elif choice == '2':
            project_manager.show_tasks()
        elif choice == '3':
            task_name = input("Enter task name to update status: ")
            new_status = input("Enter new status: ")
            project_manager.update_status(task_name, new_status)
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

