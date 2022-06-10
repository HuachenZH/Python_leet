class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        # diffX=0
        # diffY=0 # if it's matlab, add these two lines will make the code faster... just a bit
        dist=0
        for i in range(len(points)-1):
            diffX=abs(points[i][0]-points[i+1][0]) # difference of x axis
            diffY=abs(points[i][1]-points[i+1][1]) # difference of y axis
            dist+=max(diffX,diffY)
        return dist
sol=Solution()
print(sol.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
