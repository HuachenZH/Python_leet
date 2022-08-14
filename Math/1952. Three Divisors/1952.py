import math
class Solution:
    def isThree0(self, n: int) -> bool:
        count=0
        for i in range(2,n):
            if n%i==0:
                count+=1
        if count==1:
            return True
        else:
            return False
    
    # solution 2, inspired by discussion. 
    # if n fulfill the condition, it must be the square of a prime number. We only need to iterate til its square root
    
    # comes from stackoverflow
    # https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
    def is_prime(self,n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        # since all primes > 3 are of the form 6n ± 1
        # start with f=5 (which is prime)
        # and test f, f+2 for being prime
        # then loop by 6. 
        f = 5
        while f <= r:
          print('\t',f)
          if n % f == 0: return False
          if n % (f+2) == 0: return False
          f += 6
        return True
    def isThree(self, n: int) -> bool:
        if math.sqrt(n)%1!=0:
            return False
        # check math.sqrt(n) is prime or not
        else:
            return self.is_prime(math.sqrt(n))


epsilon=Solution()
print(epsilon.isThree(3))
        
