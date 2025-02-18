class Duration:
    def __init__(self, seconds):
        self._seconds = seconds

    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds)

    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes * 60)

    @staticmethod
    def from_hours(hours):
        return Duration(hours * 3600)

    @property
    def seconds(self):
        return self._seconds

    @property
    def minutes(self):
        return self._seconds / 60

    @property
    def hours(self):
        return self._seconds / 3600