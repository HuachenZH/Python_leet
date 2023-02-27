class Solution:
    # ver alpha
    # runtime 207 ms 46.15%
    # memory 15.4 MB 90.7%
    def largestPerimeterAlpha(self, nums: list[int]) -> int:
        # sort the list, descending
        nums.sort(reverse=True)
        print(nums)
        # iterate through the sorted list
        # first side, the longest
        for i in range(len(nums)-2):
            # Triple Quad Formula
            # Q=4AB−(A+B−C)^2
            # if Q > 0 : a real triangle
            # if Q == 0 : degenerate triangle, means three colinear points 
            # if Q < 0 : impossible triangle
            if 4 * nums[i]**2 * nums[i+1]**2 - (nums[i]**2+nums[i+1]**2-nums[i+2]**2)**2 > 0:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0
    
    # ver zeta
    # fast solution on leetcode
    # i nearly got it... it just uses a < b + c (assuming a is the longest) instead of Q 
    def largestPerimeterBeta(self, nums: list[int]) -> int:
        # sort the list, descending
        nums.sort(reverse=True)
        print(nums)  # i forgot to delete this line, it's been bit slower
        # iterate through the sorted list
        # first side, the longest
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2] :
                return nums[i]+nums[i+1]+nums[i+2]
        return 0
epsi = Solution()
print(epsi.largestPerimeterAlpha([1,2,1,10,3,2,1]))

# firstly i think of something like this, a triple loop

# for i in range(len(nums)-2):
#     # second side, the middle
#     for j in range(i+1, len(nums)-1):
#         # third side, the smallest
#         for k in range(i+2, len(nums)):
#             # checking...

# then i found it's not necessary since the list is sorted