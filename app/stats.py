def count(tasks):
    return len(tasks)
def completion_rate(tasks):
    done = len([t for t in tasks if t["done"]])
    return done / len(tasks) if tasks else 0
import json
def save(data):
    with open("data.json", "w") as f:
        json.dump(data, f)
def load():
    try:
        with open("data.json") as f:
            return json.load(f)
    except:
        return []
tasks = load()
save(tasks)
if __name__ == "__main__":
    add_task("Test")
    print(list_tasks())
