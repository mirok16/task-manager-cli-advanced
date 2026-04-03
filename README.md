# Task Manager CLI Advanced

A simple yet powerful command-line task manager written in Python.

## 🚀 Features

- Add tasks with priority levels
- Mark tasks as completed
- Delete tasks
- Filter tasks by status and priority
- View statistics (total tasks, completion rate)
- Persistent storage using JSON
- Modular project structure
- Basic unit tests

---

## 📁 Project Structure
app/
tasks.py # Core task logic
filters.py # Filtering functions
stats.py # Statistics functions
storage.py # Save/load logic

tests/
test_tasks.py
test_stats.py

data.json # Stored data

app/
tasks.py # Core task logic
filters.py # Filtering functions
stats.py # Statistics functions
storage.py # Save/load logic

tests/
test_tasks.py
test_stats.py

data.json # Stored data

▶️ Usage

Run the application:

python app/tasks.py

Example:

add_task("Buy groceries", "high")
add_task("Read book", "low")


🧪 Running Tests

Make sure pytest is installed:

pip install pytest

Run tests:

pytest
📊 Example Output
Buy groceries (high)
Read book (low)
💾 Data Storage

All tasks are automatically saved in data.json
