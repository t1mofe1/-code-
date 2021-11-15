import os
import sys


class Task:
    def __init__(self, name: str, task_list):
        self.name = name.strip()
        self.task_list = task_list

    def __str__(self):
        return self.name

    def change_name(self, name: str):
        self.name = name.strip()

    def complete(self):
        self.task_list.remove_task(self)


class TaskList:
    def __init__(self):
        self.tasks = []

    def __str__(self):
        tasks_str = ""
        for i, task in enumerate(self.tasks, start=1):
            tasks_str += f"{i} | {task.name}\n"
        return tasks_str[:-1] if tasks_str else "There is no tasks"

    def add_task(self, task):
        if self.find_task_by_name(task.name):
            return { "error": "Task with this name already exists" }

        self.tasks.append(task)
        return { "success": "Task added" }

    def rename_task(self, task):
        # TODO: add implementation
        pass

    def remove_task(self, task):
        if not self.find_task_by_name(task.name):
            return { "error": "Task not found" }

        self.tasks.remove(task)
        return { "success": "Task removed" }

    def find_task_by_name(self, name: str):
        for task in self.tasks:
            if task.name == name.strip():
                return task
        return None

    def find_task_by_index(self, index: int):
        return self.tasks[index]


def clear_console():
    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(command)


def clear_line(n: int = 1):
    for _ in range(n):
        sys.stdout.write("\033[F")  # back to previous line
        sys.stdout.write("\033[K")  # clear line
