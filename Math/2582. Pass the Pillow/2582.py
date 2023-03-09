class Solution:
    # runtime 23 ms 97.23%
    # memory 13.7 MB 94.28%
    def passThePillow(self, n: int, time: int) -> int:
        # the problem is like a periodic function
        # the first step is to simplify the problem into one period
        period = 2 * (n - 1)
        print("period is %s" % str(period))
        time = time % period
        print("new time is %s" % str(time))

        # then make the mapping between "how many times" and "index of person"
        # if n equals 5, five people
        # how many times    index of person
        #       1       -->       2
        #       2       -->       3
        #       3       -->       4
        #       4       -->       5
        #       5       -->       4
        #       6       -->       3
        #       7       -->       2
        #       8       -->       1
        # as period is two times something, it's even
        # so no need to split into two cases, even and odd
        if time == period:
            return 1
        if time <= period / 2:
            return time + 1
        return period - time + 1

epsi = Solution()
print(epsi.passThePillow(5,3))

