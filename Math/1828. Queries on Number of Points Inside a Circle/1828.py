# import numpy as np
class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        answer = []
        # iterate through queries, then test every point
        # go trough every query in queries
        for query in queries:
            # print("The query is %s" % query)
            # test every point
            nbPointsInCircle = 0
            for point in points:
                # print("Current point is %s" % point)
                # check whether the point is inside the circle
                # by calculating the euclidean distance between the point and circle center
                # distance = np.linalg.norm(np.array(point) - np.array(query[:-1]))
                distance = ((point[0]-query[0])**2 + (point[1]-query[1])**2)**0.5
                radius = query[2]
                if distance <= radius:
                    nbPointsInCircle -=- 1
            answer.append(nbPointsInCircle)
            # print('-- -- --')    
        return answer
epsi = Solution()
print(epsi.countPoints([[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]]))

# To calculate the distance between two points, another solution is the use numpy
# distance = np.linalg.norm(point1, point2)
# where point1 and point2 are np array
# It's clearer for syntax, however, time exceeded when i submit the solution
# solution numpy take twice more time