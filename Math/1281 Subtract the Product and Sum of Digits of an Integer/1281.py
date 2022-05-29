class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # get all the digits and add them into a list
        digitList=[]
        n_str=str(n)
        for i in range(len(n_str)):
            digitList.append(int(n_str[i]))
        # get the product
        # get the sum
        # get the substraction
sol=Solution()
sol.subtractProductAndSum(125)
