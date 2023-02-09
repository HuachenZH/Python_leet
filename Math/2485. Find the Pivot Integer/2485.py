class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = (n*(n+1)/2)**0.5
        if pivot % 1 != 0:
            return -1
        else:
            return int(pivot)
# the formula comes from
# (1+x)*x/2 = (x+n)*(n-x+1)/2
# with x = pivot
