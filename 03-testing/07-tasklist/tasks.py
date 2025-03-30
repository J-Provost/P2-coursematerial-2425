from datetime import date

class Task:
    def __init__(self, description, due_date):
        self._description = description
        self._due_date = due_date
        self._finished = False
    
    @property
    def description(self):
        return self._description
    
    @property
    def due_date(self):
        return self._due_date
    
    @property
    def finished(self):
        return self._finished
    
    @finished.setter
    def finished(self, value):
        self._finished = value


class TaskList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        if task.due_date < date.today():
            raise RuntimeError("Due date cannot be in the past.")
        self.tasks.append(task)
    
    def __len__(self):
        return len(self.tasks)
    
    @property
    def finished_tasks(self):
        return [task for task in self.tasks if task.finished]
    
    @property
    def due_tasks(self):
        return [task for task in self.tasks if not task.finished]
    
    @property
    def overdue_tasks(self):
        return [task for task in self.tasks if not task.finished and task.due_date < date.today()]
