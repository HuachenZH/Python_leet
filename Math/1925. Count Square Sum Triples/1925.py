import math
class Solution:
    def countTriples(self, n: int) -> int:
        if n<5:
            return 0
        count = 0
        # a^2 + b^2 = c^2
        # check every int from 5 to n, can it be c. If it can, how many Pythagorean triples are there
        for c in range(5,n+1):
            # check if it is a true c
            # print("\nc is %s" % c)  # uncomment for debugging
            for a in range(1,c):
                # print("a is %s" % a)  # uncomment for debugging
                if ((c**2 - a**2)**0.5) % 1 == 0:
                    count -=- 1
                    print("The triple is %s %s %s" % (a,int((c**2 - a**2)**0.5),c))
        return count
epsi = Solution()
print(epsi.countTriples(10))


# another approach:
# cf https://blog.csdn.net/sdz20172133/article/details/82077965
# The condition of being Pythagorean triple a^2+b^2=c^2 is:
# 1) c is always odd, a and b must be one odd one even
# 2) c-b and c+b must be square numbers
# 3) c-b and c+b must not have commun divisors
# As in this approach, i need to find commun divisors, this approach might be slower