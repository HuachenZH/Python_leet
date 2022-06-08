class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        # a list of odd numbers from 0 to 100... wait it's odd number but not prime number
        oddList=list(range(1,len(arr)+1,2))
        count=0
        # I dont make subarray. I sum it up directly
        for odd in oddList:  # odd will be 1, 3, 5 ...
            # subarray for each odd
            for startIndex in range(len(arr)-odd+1): # there must be +1, if not, false. Cuz range() excludes
                for i in range(odd):
                    count+=arr[startIndex+i] 
        return count

sol=Solution()
print(sol.sumOddLengthSubarrays([1,4,2,5,3]))
