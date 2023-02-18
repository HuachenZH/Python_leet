import datetime
class Solution:
    # runtime 37.62%
    # memory 65.69%
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dayset = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return dayset[datetime.datetime(year, month, day).weekday()]
