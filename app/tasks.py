tasks = []
def add_task(name):
    tasks.append({"name": name, "done": False})
def list_tasks():
    return tasks
