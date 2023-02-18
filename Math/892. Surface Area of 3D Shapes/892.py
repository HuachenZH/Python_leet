import numpy as np
class Solution:
    # ver beta
    # i didnt involve numpy in this version
    # the code is simple but performance is great
    # runtime 97.92%
    # memory 92.50%
    def surfaceArea(self, grid: list[list[int]]) -> int:
        ans = 0
        # count zeros
        count0 = 0
        for row in grid:
            count0 += row.count(0)
        ans += 2 * (len(grid)*len(grid[0]) - count0)
        
        # contruct new list
        for i in range(len(grid)):
            grid[i].append(0)
            grid[i].insert(0,0)
        # construct list of zeros
        zeros = []
        for i in range(len(grid[0])):
            zeros.append(0)
        # row_stack zeros to grid
        grid.append(zeros)
        grid.insert(0,zeros)
        
        # count surfaces
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                ans += abs(grid[i][j]-grid[i-1][j])+abs(grid[i][j]-grid[i][j-1])
        return ans
    
    # ver alpha
    # as it s a matrix approach, matlab is the best choice
    # performance is not optimized, so i developped ver beta above
    # runtime 12.92%
    # memory 5%
    def surfaceArea2(self, grid: list[list[int]]) -> int:
        ans = 0
        # top view / bottom view
        # check how many zeros are there
        count0 = 0
        for row in grid:
            count0 += row.count(0)
        print("count0 is %s" % count0)
        ans += 2 * (len(grid)*len(grid[0]) - count0)

        # construct a new matrix. Surround grid by 0

        # in each row, add 0 to the start and end position
        for i in range(len(grid)):
            grid[i].append(0)
            grid[i].insert(0,0)
            #              ^    position
            #                ^  value
        grid = np.array(grid)
        # row_stack vector of zeros
        zeros = np.zeros(len(grid[0]), dtype=int)
        grid = np.row_stack((zeros,grid,zeros))
        print(grid)
        
        # count surfaces
        for i in range(1,len(grid)):
            for j in range(1, len(grid[0])):
                # diff north
                ans += abs(grid[i][j] - grid[i-1][j])
                # diff west
                ans += abs(grid[i][j] - grid[i][j-1])
        return ans
epsi = Solution()
print(epsi.surfaceArea([[1,2],[3,4]]))



# 0   0 0 0
#   _______
# 0 | 1 2 0
# 0 | 3 4 0
# 0 | 0 0 0

