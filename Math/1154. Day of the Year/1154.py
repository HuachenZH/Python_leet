class Solution:
    # ver alpha
    # runtime 60 ms 97.64%
    # memory 14 MB 24.3%
    def dayOfYearAlpha(self, date: str) -> int:
        # notice:
        # different months dont have same number of days
        # leap year, 29 days in fev

        # split, get day, month and year
        year = int(date.split("-")[0])
        month = int(date.split("-")[1])
        day = int(date.split("-")[2])
        
        # leap year or not
        # notice : 1900 is not leap year
        if year % 4 == 0 and year != 1900: # leap year, 366 days in a year, 29 days in fev
            # list of numbers of days each month
            # hashmap can also do the job
            # i add a 0 at the end, in case the month is jan
            mapp = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
            # how many days are there before this month
            res = 0
            for i in range(month-1):
                res += mapp[i] # if month is jan, month=1, mapp[i] gives 0
            # how many days before this day in this month
            res += day
            return res
        else: # normal year
            mapp = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
            # how many days are there before this month
            res = 0
            for i in range(month-1):
                res += mapp[i] # if month is jan, month=1, mapp[i] gives 0
            # how many days before this day in this month
            res += day
            return res
        return -1

    # ver beta
    # in ver aplha, a chunk of code is duplicated, so put them into a function
    # no wait no need to put into a function
    # the only difference is the variable mapp
    # i thought the performance would be exactly the same
    # in fact not
    # runtime 88 ms, 28 ms slower, 29.61%
    # memory 13.9 MB, 0.1 MB improved, 63.95%
    def dayOfYearBeta(self, date: str) -> int:
        # split, get day, month and year
        year = int(date.split("-")[0])
        month = int(date.split("-")[1])
        day = int(date.split("-")[2])
        
        # leap year or not
        # notice : 1900 is not leap year
        if year % 4 == 0 and year != 1900: # leap year, 366 days in a year, 29 days in fev
            # list of numbers of days each month
            # hashmap can also do the job
            # i add a 0 at the end, in case the month is jan
            mapp = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
        else: # normal year
            mapp = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
            # how many days are there before this month
        res = 0
        for i in range(month-1):
            res += mapp[i] # if month is jan, month=1, mapp[i] gives 0
        # how many days before this day in this month
        res += day
        return res

epsi = Solution()
print(epsi.dayOfYearBeta("1900-05-02"))
