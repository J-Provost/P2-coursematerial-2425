from datetime import date

class Calendar:
    @property
    def today(self):
        return date.today()


class CalendarStub:
    def __init__(self, initial_date):
        self._today = initial_date

    @property
    def today(self):
        return self._today

    @today.setter
    def today(self, value):
        self._today = value
