def count(tasks):
    return len(tasks)
def completion_rate(tasks):
    done = len([t for t in tasks if t["done"]])
    return done / len(tasks) if tasks else 0
import json
