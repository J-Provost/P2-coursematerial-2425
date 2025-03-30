from datetime import date, timedelta
from tasks import Task, TaskList

# Create task list
tasks = TaskList()

# Get today's date and tomorrow's date
tomorrow = date.today() + timedelta(days=1)
yesterday = date.today() - timedelta(days=1)

# Add task with due date in the future
task = Task('some description', tomorrow)
tasks.add_task(task)
print(len(tasks))  # Output: 1

# Finished tasks should be empty
print(tasks.finished_tasks)  # Output: []

# Due tasks should have the task
print(tasks.due_tasks)  # Output: [task]

# Overdue tasks should be empty
print(tasks.overdue_tasks)  # Output: []

# Mark task as finished
task.finished = True
print(tasks.finished_tasks)  # Output: [task]
print(tasks.due_tasks)  # Output: []
print(tasks.overdue_tasks)  # Output: []

# Add task with a due date in the past (should raise an error)
task_in_past = Task('past task', yesterday)
try:
    tasks.add_task(task_in_past)
except RuntimeError as e:
    print(e)  # Output: Due date cannot be in the past.
