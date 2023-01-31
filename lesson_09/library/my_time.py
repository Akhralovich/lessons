from __future__ import annotations


class MyTime:

    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.timestamp = seconds + minutes * 60 + hours * 60 * 60

    def __eq__(self, other) -> bool:
        return self.timestamp == other.timestamp

    def __add__(self, other) -> MyTime:
        timestamp = self.timestamp + other.timestamp
        return self.timestamp_to_time(timestamp)

    def __sub__(self, other) -> MyTime:
        timestamp = self.timestamp - other.timestamp
        return self.timestamp_to_time(timestamp)

    def __mul__(self, other: int):
        timestamp = self.timestamp * other
        return self.timestamp_to_time(timestamp)

    def __str__(self):
        return f"MyTime: {self.hours}:{self.minutes}:{self.seconds}"

    @staticmethod
    def timestamp_to_time(seconds: int) -> MyTime:
        hours = seconds // (60 * 60)
        minutes = (seconds % (60 * 60)) // 60
        seconds = seconds % 60
        return MyTime(hours,  minutes, seconds)