tasks = []
def add_task(name):
    tasks.append({"name": name, "done": False})
def list_tasks():
    return tasks
def complete_task(index):
    tasks[index]["done"] = True
def add_task(name, priority="normal"):
    tasks.append({"name": name, "done": False, "priority": priority})
