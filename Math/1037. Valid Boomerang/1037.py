class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        # i really hate this question
        # ..|..

        # check if there are identical points
        if points[0]==points[1] or points[0]==points[2]:
            # two identical points
            return False
        try: # there might be error of division by zero (points are vertically aligned)
            return not (points[1][1]-points[0][1]) / (points[1][0]-points[0][0]) == (points[2][1]-points[0][1]) / (points[2][0]-points[0][0])
        except: # there is division by zero
            if points[0][0] == points[1][0] == points[2][0]:
                return False
            return True

    # distance approach: if the three points can form a triangle, then it s boomerang
    # does not work due to computing accuracy problem.
    def distance(self, point1: list[int], point2: list[int]) -> float:
        # distance between two points: sqrt( (x1-x2)² + (y1-y2)² )
        return ( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 )**0.5
    def isBoomerangPoubelle(self, points: list[list[int]]) -> bool:
        
        if points[0]==points[1] or points[0]==points[2]:
            # two identical points
            return False

        # distance approach
        # suppose from bot left to top right, there are A B C three points.
        # if they are in the same line, then we have AB + BC = AC
        # print("AB+AC is %s" % str(self.distance(points[0],points[1]) + self.distance(points[1],points[2])))
        # print("AC is %s" % str(self.distance(points[0],points[2])))
        a = round(self.distance(points[0],points[1]),4)
        print("a is %s" % str(a))
        b = round(self.distance(points[1],points[2]),4)
        print("b is %s" % str(b))
        c = round(self.distance(points[0],points[2]),4)
        print("c is %s" % str(c))
        # return not self.distance(points[0],points[1]) + self.distance(points[1],points[2]) == self.distance(points[0],points[2])
        if a<b+c and a>abs(b-c):
            # then it s a triangle
            return True
        return False



epsi = Solution()
print(epsi.isBoomerang(  [[19,82],[73,73],[97,69]]  ))
