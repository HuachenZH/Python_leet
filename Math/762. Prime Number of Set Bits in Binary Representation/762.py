class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res=0
        for i in range(left, right+1):
            # I. get the number of set bits
            # I.1 number in binary
            binstr=str(bin(i))[2:]
            # I.2 number of set bits : sum all the 1
            summ=0
            for j in range(len(binstr)):
                summ+=int(binstr[j])
            # print(binstr+'  '+str(summ))
            # print('The set bit of '+str(i)+' is \t: '+str(summ))
            # II. determine wether summ is prime or not
            flag=True # prime
            for j in range(2,summ):
                if summ%j==0:
                    flag=False # not prime
                    break
            if summ==1:
                flag=False
            if summ==2:
                flag=True
            if flag==True:
                res+=1
            # print('res is now '+str(res))
        return res

sol=Solution()
print(sol.countPrimeSetBits(10,15))
