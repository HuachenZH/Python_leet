class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # get all the digits and add them into a list
        digitList=[]
        n_str=str(n)
        for i in range(len(n_str)):
            digitList.append(int(n_str[i]))
        # get the product and the sum
        product=1
        summ=0
        for digit in digitList:
            product*=digit
            summ+=digit
        # get the substraction
        result=product-summ
        return result
sol=Solution()
sol.subtractProductAndSum(125)
