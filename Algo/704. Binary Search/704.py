import math

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        leftIndex = 0
        rightIndex = len(nums)-1
        if leftIndex == rightIndex: # when the length of nums is 1
            if nums[0] == target :
            	return 0
            return -1
        counter = 0
        while leftIndex <= rightIndex :
            middleIndex = math.floor((leftIndex+rightIndex)/2)
            # print("middle index is %s, gives %s" % (middleIndex, nums[middleIndex]))
            if target == nums[middleIndex]:
                return middleIndex
            elif target < nums[middleIndex] :
                rightIndex = middleIndex - 1
                # print("comparing target %s with %s" % (target, nums[middleIndex]), end=' , ')
                # print('take the left interval')
            else:
                leftIndex = middleIndex + 1
                # print("comparing target %s with %s" % (target, nums[middleIndex]), end=' , ')
                # print('take the right interval')
            # print("%s iteration ends, left index gives %s, right index gives %s" % (counter, nums[leftIndex], nums[rightIndex]))
            # print("left index is %s, right index is %s" % (leftIndex, rightIndex))
            # print('')
            counter += 1

        return -1


if __name__ == '__main__':
    epsilon = Solution()
    print(epsilon.search([-1,0,3,5,9,12], 13))

# when the input is [-1,0,3,5,9,12], 13
# there will be an error (list index exceeded) with one print