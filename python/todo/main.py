from getpass import getuser
from os.path import exists

from util import TaskList, Task, clear_console, clear_line

if not exists("tasks.txt"):
    open("tasks.txt", "w").close()
file = open("tasks.txt", "r+", encoding="utf-8")
task_list = TaskList()
for string in file.read().split("\n"):
    if string != "":
        task_list.add_task(Task(string, task_list))


def main():
    try:
        clear_console()
        print("{code} - TODO List\n")
        print_menus()
    except KeyboardInterrupt:
        exit_dialog()


def print_menus():
    menus = ["Add task", "Remove task", "Print tasks", "Exit"]

    # TODO: add rename functionality

    for i, menu in enumerate(menus, start=1):
        print(f"{i}. {menu}")

    try:
        menu = int(input("\nEnter menu number: ").strip())
    except ValueError:
        menu = 0
    while menu not in range(1, len(menus) + 1):
        try:
            clear_line()
            menu = int(input("Enter menu number: ").strip())
        except ValueError:
            menu = 0

    if menu == 1:
        add_task()
    elif menu == 2:
        remove_task()
    elif menu == 3:
        print_tasks()
    elif menu == 4:
        exit_dialog()


def exit_program():
    clear_console()
    save_tasks()
    exit()


def exit_dialog():
    try:
        clear_console()

        answer = input("Are you sure you want to exit? (y/n) ").strip()
        while answer not in ("y", "n"):
            clear_line()
            answer = input("Are you sure you want to exit? (y/n) ").strip()

        if answer == "y":
            exit_program()
        else:
            main()
    except KeyboardInterrupt:
        exit_program()


def print_tasks():
    clear_console()
    print(f"Tasks of '{getuser()}':\n\n{str(task_list)}")
    input("\nPress enter to continue...")
    main()


def save_tasks():
    file.write("\n".join(map(lambda task: str(task), task_list.tasks)))


def add_task():
    try:
        clear_console()

        print("If you want to cancel this action, do CTRL + C\n")

        task_name = input("Enter task name: ").strip()
        while task_name == "":
            clear_line()
            task_name = input("Enter task name: ").strip()

            if task_list.find_task_by_name(task_name):
                print(f"Task '{task_name}' already exists")
                task_name = ""
                input("Press enter to continue...")
                clear_line()

        task_list.add_task(Task(task_name, task_list))
    except KeyboardInterrupt:
        pass
    finally:
        main()


def remove_task():
    try:
        clear_console()

        if len(task_list.tasks) == 0:
            print("No tasks to remove")
            input("\nPress enter to continue...")
            main()

        print("If you want to cancel this action, do CTRL + C\n")

        task_list_length = "1" if len(task_list.tasks) == 1 else f"1 - {len(task_list.tasks)}"

        try:
            task_number = int(input(f"Enter task number ({task_list_length}): ").strip())
        except ValueError:
            task_number = 0

        while task_number not in range(1, len(task_list.tasks) + 1):
            try:
                clear_line()
                task_number = int(input(f"Enter task number ({task_list_length}): ").strip())
            except ValueError:
                task_number = 0

        task = task_list.find_task_by_index(task_number - 1)

        clear_console()

        confirm = input(f"Are you sure you want to remove task '{task.name}'? (y/n) ").strip()
        while confirm not in ("y", "n"):
            clear_line()
            confirm = input(f"Are you sure you want to remove task '{task.name}'? (y/n) ").strip()

        if confirm == "y":
            task_list.remove_task(task)
    except KeyboardInterrupt:
        pass
    finally:
        main()


if __name__ == '__main__':
    main()
