class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        if self.is_prime(area):
            return [area,1]
        else:
            if (area**0.5)%1 == 0: # square root is integer
                return [int(area**0.5), int(area**0.5)]
            else:
                n=int(area**0.5)
                while n>1:
                    if area%n==0:
                        return [int(area/n), n]
                    n-=1
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


epsilon=Solution()
print(epsilon.constructRectangle())