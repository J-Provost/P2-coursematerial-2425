from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub


def test_task_becomes_overdue():
    # Setup a CalendarStub that starts with today's date
    calendar = CalendarStub(date.today())
    
    # Create a Task due tomorrow
    tomorrow = date.today() + timedelta(days=1)
    task = Task('some description', tomorrow)
    
    # Create TaskList with the calendar stub
    tasks = TaskList(calendar)
    
    # Add the task to the task list
    tasks.add_task(task)
    
    # At this point, the task is not overdue
    assert tasks.overdue_tasks == []
    
    # Now we simulate the passage of two days
    calendar.today = date.today() + timedelta(days=2)
    
    # Now the task is overdue
    assert tasks.overdue_tasks == [task]
