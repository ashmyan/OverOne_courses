class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0, str_time='', other_time=None):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        self.__other_time = other_time

        if str(str_time):
            lst_time = str_time.split(':')
            self.__hours = int(lst_time[0])
            self.__minutes = int(lst_time[1])
            self.__seconds = int(lst_time[2])

    def hours(self):
        return self.__hours

    def minutes(self):
        return self.__minutes

    def secunds(self):
        return self.__seconds

    def other_time(self):
        return self.__other_time

    def __add__(self, other):
        return MyTime(self.__hours + other.__hours,
                      self.__minutes + other.__minutes,
                      self.__seconds + other.__seconds)

    def __sub__(self, other):
        return MyTime(self.__hours - other.__hours,
                      self.__minutes - other.__minutes,
                      self.__seconds - other.__seconds)

    def __eq__(self, other):
        if self.__hours == other.__hours and self.__minutes == other.__minutes and self.__seconds == other.__seconds:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__hours != other.__hours and self.__minutes != other.__minutes and self.__seconds != other.__seconds:
            return True
        else:
            return False

    def __str__(self):
        if self.__hours > 23 or self.__minutes > 59 or self.__seconds > 59:
            while self.__hours > 23 or self.__minutes > 59 or self.__seconds > 59:
                self.__minutes += self.__seconds // 60
                self.__hours += self.__minutes // 60
                self.__minutes = self.__minutes % 60
                self.__seconds = self.__seconds % 60
                self.__hours = self.__hours % 23
                if len(str(self.__hours)) < 2:
                    self.__hours = '0' + str(self.__hours)
                return f'Hours: {self.__hours}, Minutes: {self.__minutes}, Seconds: {self.__seconds}'
        else:
            return f'Hours: {self.__hours}, Minutes: {self.__minutes}, Seconds: {self.__seconds}'


mytime1 = MyTime(12, 35, 17)
mytime2 = MyTime(str_time='12:15:10')
mytime3 = MyTime(other_time=mytime1)
print(mytime3.hours())

print(mytime2.__str__())
