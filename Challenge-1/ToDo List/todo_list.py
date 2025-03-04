import click  # It is a UV package to create a CLI
import json  # It is a built-in feature in UV for save and load tasks from a file
import os  # operating system to check if the file exists or not

# Save data from JSON File
TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []  # Return an empty list if the file doesn't exist

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Click is initialized and group is a decorator
@click.group()
def cli():
    """This is a CLI for a simple TODO list application"""
    pass

# Add Task
@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the TODO list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task '{task}' added successfully")


# List Of Tasks
@click.command()
def list():
    """List all tasks in the TODO list"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks in the TODO list")
        return
    for i, task in enumerate(tasks, 1):
        status = "Done" if task["done"] else "Not Done"
        click.echo(f"{i}. {task['task']} - {status}")

# Complete Task
@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} marked as completed.")
    else:
        click.echo("Invalid task number: {task_number}")

# Delete Task
@click.command()
@click.argument("task_number", type=int)
def delete(task_number):
    """Delete a task from the TODO list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        del tasks[task_number - 1]
        save_tasks(tasks)
        click.echo(f"Task {task_number} deleted successfully")
    else:
            click.echo("Invalid task number: {task_number}")


cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(delete)

if __name__ == "__main__":
    cli()