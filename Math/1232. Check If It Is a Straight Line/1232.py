class Solution:
    # runtime 69 ms 28.56%
    # memory 14.5 MB 20.54%
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        # it makes me think of linear regression. I think there would be a parameter which can tell if it s linear or not
        # to be more simple, we just need to calculate the slope
        
        # if there are only two points, by default they are in the same line
        if len(coordinates) == 2:
            return True
        
        # there is the problem of division by zero, so two cases, vertical line or oblique line
        # case 1: vertical line =======================================
        if coordinates[1][0] - coordinates[0][0] == 0:
            # if it should be a vertical line, then we cannot calculate the slope
            # we only need to check, for every points, whether they have the same x coordinate
            for i in range(2,len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    # print("17")
                    return False
            # print("19")
            return True

        # case 2 : oblique line ========================================
        # take the first two points, calculate the slope
        slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        #              ^^ y2                ^^ y1               ^^ x2               ^^ x1
        # then iterate from the third point to the last point
        # calculate the slope with the first point
        # and check if the slopes are the same
        for i in range(2,len(coordinates)):
            # there is still problem of division by zero, so check it first
            if coordinates[i][0] - coordinates[0][0] == 0:
                # as in this case, it s supposed to be an oblique line
                # if division by zero occurs, it means that two points form a vertical line
                # print("34")
                # print("i is %s" %i)
                # print("two coor are %s and %s" % (coordinates[i], coordinates[0]))
                return False
            newSlope = (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0])
            #               ^^ yi                ^^ y1               ^^ xi               ^^ x1
            # if the slope is not the same, then they are not in the same line, no need to proceed the iteration
            if newSlope != slope:
                # print("40")
                return False
            # else, do nothing and proceed to the next iteration, so there is no else
        # print('43')
        return True

epsi = Solution()
# print(epsi.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))