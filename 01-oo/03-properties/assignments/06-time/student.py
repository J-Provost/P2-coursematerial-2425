# Write your code here
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def seconds(self):
        return self.__seconds
    
    @hours.setter
    def hours(self, value):
        if 0<=value<=23:
            self.__hours = value
        else:
            raise ValueError
        
    @minutes.setter
    def minutes(self, value):
        if 0<=value<=59:
            self.__minutes = value
        else:
            raise ValueError
        
    @seconds.setter
    def seconds(self, value):
        if 0<=value<=59:
            self.__seconds = value
        else:
            raise ValueError