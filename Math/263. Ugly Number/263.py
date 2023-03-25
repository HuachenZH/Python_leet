
class Solution:
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
          
          if n % f == 0: return False
          if n % (f+2) == 0: return False
          f += 6
        return True
    
    def isUgly(self, n: int) -> bool:
        if n == 1 or n == 0:
            return True
        n = abs(n)
        # in an iteration, check find its factors. While finding, check whether each factor is prime or not
        # we dont need to iterate from 1 to n. From 1 to sqrt(n) is sufficient
        for i in range(7,n):
            # if i is a factor of n and bigger then 5, check if it s prime or not. Else, do nothing, so there is no else
            if n % i == 0:
                print("one of the factor is %s" % i)
                # check if i is prime or not
                if self.is_prime(i):
                    return False
        return True

epsi = Solution()
print(epsi.isUgly(-2147483648))
