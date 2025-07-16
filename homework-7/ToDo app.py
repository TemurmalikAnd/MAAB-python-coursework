import csv
import json
import os
from abc import ABC, abstractmethod
from datetime import datetime

class Task:
    """Represents a single task with its attributes."""
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"

class FileHandler(ABC):
    """Abstract base class for handling different file formats."""
    @abstractmethod
    def save(self, tasks, filename):
        pass

    @abstractmethod
    def load(self, filename):
        pass

class CSVHandler(FileHandler):
    """Handles task storage in CSV format."""
    def save(self, tasks, filename):
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['task_id', 'title', 'description', 'due_date', 'status'])
                for task in tasks:
                    writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])
        except Exception as e:
            print(f"Error saving to CSV: {e}")

    def load(self, filename):
        tasks = []
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        tasks.append(Task(
                            row['task_id'],
                            row['title'],
                            row['description'],
                            row['due_date'],
                            row['status']
                        ))
        except Exception as e:
            print(f"Error loading from CSV: {e}")
        return tasks

class JSONHandler(FileHandler):
    """Handles task storage in JSON format."""
    def save(self, tasks, filename):
        try:
            task_list = [
                {
                    'task_id': task.task_id,
                    'title': task.title,
                    'description': task.description,
                    'due_date': task.due_date,
                    'status': task.status
                } for task in tasks
            ]
            with open(filename, 'w') as file:
                json.dump(task_list, file, indent=4)
        except Exception as e:
            print(f"Error saving to JSON: {e}")

    def load(self, filename):
        tasks = []
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    task_list = json.load(file)
                    for task_data in task_list:
                        tasks.append(Task(
                            task_data['task_id'],
                            task_data['title'],
                            task_data['description'],
                            task_data['due_date'],
                            task_data['status']
                        ))
        except Exception as e:
            print(f"Error loading from JSON: {e}")
        return tasks

class ToDoManager:
    """Manages tasks and coordinates with file handlers."""
    def __init__(self, file_handler, filename):
        self.tasks = []
        self.file_handler = file_handler
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from file using the specified file handler."""
        self.tasks = self.file_handler.load(self.filename)

    def save_tasks(self):
        """Save tasks to file using the specified file handler."""
        self.file_handler.save(self.tasks, self.filename)

    def is_unique_id(self, task_id):
        """Check if task ID is unique."""
        return not any(task.task_id == task_id for task in self.tasks)

    def add_task(self, task_id, title, description, due_date, status):
        """Add a new task with validation."""
        try:
            if not self.is_unique_id(task_id):
                print("Error: Task ID already exists!")
                return
            if not title:
                print("Error: Title cannot be empty!")
                return
            if due_date:
                try:
                    datetime.strptime(due_date, '%Y-%m-%d')
                except ValueError:
                    print("Error: Invalid due date format! Use YYYY-MM-DD.")
                    return
            if status not in ['Pending', 'In Progress', 'Completed']:
                print("Error: Status must be Pending, In Progress, or Completed!")
                return
            task = Task(task_id, title, description, due_date, status)
            self.tasks.append(task)
            self.save_tasks()
            print("Task added successfully!")
        except Exception as e:
            print(f"Error adding task: {e}")

    def view_all_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks found!")
            return
        print("Tasks:")
        for task in self.tasks:
            print(task)

    def update_task(self, task_id):
        """Update a task's details by task ID."""
        for task in self.tasks:
            if task.task_id == task_id:
                print(f"Current details: {task}")
                try:
                    title = input("Enter new title (leave blank to keep current): ") or task.title
                    description = input("Enter new description (leave blank to keep current): ") or task.description
                    due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ") or task.due_date
                    status = input("Enter new status (Pending/In Progress/Completed, leave blank to keep current): ") or task.status
                    if title and status in ['Pending', 'In Progress', 'Completed']:
                        if due_date:
                            try:
                                datetime.strptime(due_date, '%Y-%m-%d')
                            except ValueError:
                                print("Error: Invalid due date format! Use YYYY-MM-DD.")
                                return
                        task.title = title
                        task.description = description
                        task.due_date = due_date
                        task.status = status
                        self.save_tasks()
                        print("Task updated successfully!")
                    else:
                        print("Error: Title cannot be empty and status must be valid!")
                except Exception as e:
                    print(f"Error updating task: {e}")
                return
        print("Task not found!")

    def delete_task(self, task_id):
        """Delete a task by task ID."""
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                self.tasks.pop(i)
                self.save_tasks()
                print("Task deleted successfully!")
                return
        print("Task not found!")

    def filter_tasks(self, status):
        """Filter and display tasks by status."""
        if status not in ['Pending', 'In Progress', 'Completed']:
            print("Error: Status must be Pending, In Progress, or Completed!")
            return
        filtered = [task for task in self.tasks if task.status == status]
        if not filtered:
            print(f"No tasks found with status {status}!")
            return
        print(f"Tasks with status {status}:")
        for task in filtered:
            print(task)

    def run_menu(self):
        """Run the interactive menu for the To-Do application."""
        while True:
            print("\nWelcome to the To-Do Application!")
            print("1. Add a new task")
            print("2. View all tasks")
            print("3. Update a task")
            print("4. Delete a task")
            print("5. Filter tasks by status")
            print("6. Save tasks")
            print("7. Load tasks")
            print("8. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    task_id = input("Enter Task ID: ")
                    title = input("Enter Title: ")
                    description = input("Enter Description: ")
                    due_date = input("Enter Due Date (YYYY-MM-DD, leave blank if none): ")
                    status = input("Enter Status (Pending/In Progress/Completed): ")
                    self.add_task(task_id, title, description, due_date, status)
                elif choice == 2:
                    self.view_all_tasks()
                elif choice == 3:
                    task_id = input("Enter Task ID to update: ")
                    self.update_task(task_id)
                elif choice == 4:
                    task_id = input("Enter Task ID to delete: ")
                    self.delete_task(task_id)
                elif choice == 5:
                    status = input("Enter Status to filter (Pending/In Progress/Completed): ")
                    self.filter_tasks(status)
                elif choice == 6:
                    self.save_tasks()
                    print("Tasks saved successfully!")
                elif choice == 7:
                    self.load_tasks()
                    print("Tasks loaded successfully!")
                elif choice == 8:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice! Please enter a number between 1 and 8.")
            except ValueError:
                print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    # Initialize with JSONHandler by default; can be switched to CSVHandler
    file_handler = JSONHandler()  # or CSVHandler()
    manager = ToDoManager(file_handler, "tasks.json")  # or "tasks.csv"
    manager.run_menu()