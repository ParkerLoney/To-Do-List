# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []

# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks
def view_tasks(tasks):
    print(tasks)

# Step 4: Delete a task
def delete_task(location, tasks):
    tasks.pop(location)

# Step 5: Mark task complete
def mark_complete(completeLocation, tasks):
    tasks[completeLocation] += "✅"

# Step 6: Save/load tasks (extra stretch for today)

# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    add_task("Say hello to silas")
    delete_task(1, tasks)
    view_tasks(tasks)
    completeLocation = input("Which task did you complete? (index): ")
    mark_complete(0, tasks)
    view_tasks(tasks)