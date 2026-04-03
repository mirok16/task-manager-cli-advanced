def done_tasks(tasks):
    return [t for t in tasks if t["done"]]
def by_priority(tasks, level):
    return [t for t in tasks if t["priority"] == level]
