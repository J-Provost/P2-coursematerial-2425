from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub


def test_creation():
    # Arrange
    today = date(2000, 1, 1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)

    # Act - No action needed, we are just checking initial values

    # Assert
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []


def test_adding_task_with_due_day_in_future():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    calendar = CalendarStub(today)
    task = Task('Task with future due date', tomorrow)
    sut = TaskList(calendar)

    # Act
    sut.add_task(task)

    # Assert
    assert len(sut) == 1
    assert sut.due_tasks == [task]
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []


def test_adding_task_with_due_day_in_past():
    # Arrange
    today = date(2000, 1, 1)
    yesterday = date(2000, 1, 1) - timedelta(days=1)
    calendar = CalendarStub(today)
    task = Task('Task with past due date', yesterday)
    sut = TaskList(calendar)

    # Act and Assert
    try:
        sut.add_task(task)
        assert False, "Expected RuntimeError"
    except RuntimeError:
        pass


def test_task_becomes_finished():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    # Act
    task.finished = True

    # Assert
    assert task in sut.finished_tasks
    assert task not in sut.due_tasks
    assert sut.overdue_tasks == []


def test_task_becomes_overdue():
    # Arrange
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    next_week = date(2000, 1, 8)
    calendar = CalendarStub(today)
    task = Task('description', tomorrow)
    sut = TaskList(calendar)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks
