import pytest
from datetime import date, timedelta
from tasks import Task, TaskList
from calendars import CalendarStub

# Fixture for today
@pytest.fixture
def today():
    return date(2000, 1, 1)

# Fixture for tomorrow
@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

# Fixture for yesterday
@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)

# Fixture for calendar, which depends on today
@pytest.fixture
def calendar(today):
    return CalendarStub(today)

# Fixture for sut (System Under Test), which depends on calendar
@pytest.fixture
def sut(calendar):
    return TaskList(calendar)


def test_creation(sut):
    # Act - No action needed, we are just checking initial values

    # Assert
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []


def test_adding_task_with_due_day_in_future(sut, tomorrow):
    # Arrange
    task = Task('Task with future due date', tomorrow)

    # Act
    sut.add_task(task)

    # Assert
    assert len(sut) == 1
    assert sut.due_tasks == [task]
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []


def test_adding_task_with_due_day_in_past(sut, yesterday):
    # Arrange
    task = Task('Task with past due date', yesterday)

    # Act and Assert
    try:
        sut.add_task(task)
        assert False, "Expected RuntimeError"
    except RuntimeError:
        pass


def test_task_becomes_finished(sut, tomorrow):
    # Arrange
    task = Task('description', tomorrow)
    sut.add_task(task)

    # Act
    task.finished = True

    # Assert
    assert task in sut.finished_tasks
    assert task not in sut.due_tasks
    assert sut.overdue_tasks == []


def test_task_becomes_overdue(sut, tomorrow, calendar):
    # Arrange
    next_week = date(2000, 1, 8)
    task = Task('description', tomorrow)
    sut.add_task(task)

    # Act
    calendar.today = next_week

    # Assert
    assert [task] == sut.overdue_tasks
