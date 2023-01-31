from __future__ import annotations

from lesson_09.library.my_time import MyTime


class MyDateTime(MyTime):

    def __init__(self, year, month, day, hours, minutes, seconds):
        super().__init__(hours, minutes, seconds)

        self.year, self.month, self.day = year, month, day
        self.timestamp += year * 365 * 24 * 60 * 60 + month * 31 * 24 * 60 * 60 + day * 24 * 60 * 60

    def __add__(self, other) -> MyDateTime:
        timestamp = self.timestamp + other.timestamp
        return self.timestamp_to_datetime(timestamp)

    def __sub__(self, other) -> MyDateTime:
        timestamp = self.timestamp - other.timestamp
        return self.timestamp_to_datetime(timestamp)

    def __mul__(self, other: int):
        timestamp = self.timestamp * other
        return self.timestamp_to_datetime(timestamp)

    def __str__(self):
        return f"MyDateTime: {self.year}-{self.month}-{self.day} {self.hours}:{self.minutes}:{self.seconds}"

    @staticmethod
    def timestamp_to_datetime(seconds: int) -> MyDateTime:
        year = seconds // (365 * 24 * 60 * 60)
        month = seconds // (31 * 24 * 60 * 60)
        day = seconds // (24 * 60 * 60)
        hours = seconds // (60 * 60)
        minutes = (seconds % (60 * 60)) // 60
        seconds = seconds % 60
        return MyDateTime(year, month, day, hours,  minutes, seconds)