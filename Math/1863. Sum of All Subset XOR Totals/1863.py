from itertools import combinations
class Solution:
    def subArrays(self, arr: list[int]) -> list:
        '''Returns all subarrays of an array (order doesnt matter)'''
        # example, arr is [5,1,6,4], we want to obtain
        # [5],[1],[6],[4] ------------> subarray of length of 1
        # [5,1],[5,6],[5,4]----------\
        # [1,6],[1,4]-----------------> subarray of length of 2
        # [6,4]----------------------/
        # [5,1,6],[5,1,4],[5,6,4]----\
        # [1,6,4]--------------------/ subarray of length of 3
        # [5,1,6,4]------------------> subarray of length of 4
        res=[]
        for i in range(1,len(arr)+1): # i will be 1,2,3,4. i is the length of subarray
            comb=combinations(arr,i) # comb is a list of tuples
            res.append([elem for elem in comb]) # without [], res will be like:<generator object Solution.subArrays.<locals>.<genexpr> at 0x00000219CEF92030>       
        return res
    def subsetXORSum(self, nums: list[int]) -> int:
        res=0
        arr=self.subArrays(nums)
        for i in arr[0]: # first sublist, tuples with only one element
            res+=i[0] # i is like (5,) 
        for i in range(1,len(arr)): # sublist of list. Begins with the second sublist. The first sublist is covered in the previous for loop 
            for j in range(len(arr[i])): # tuple of sublist
                tmp=arr[i][j][0]
                for k in range(1,len(arr[i][j])): # element of tuple
                    print(str(tmp)+" xor "+str(arr[i][j][k])+" is "+str(tmp^arr[i][j][k]))
                    tmp=tmp^arr[i][j][k]
                print("--")
                res+=tmp

        print(arr)
        return res


sol=Solution()
print(sol.subsetXORSum([5,1,6]))
