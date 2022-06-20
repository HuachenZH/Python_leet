class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        # we need to get the projection in three 2D planes: xy plane, xz plane and yz plane
        # Let's take example of [[1,2],[3,4]]
        #  | 1  2 |
        #  | 3  4 |
        # the projection in the xy plane is 4, corresponds to the number of element of the matrix
        # ...if there is no zero
        
        # the projection in the xz plane is 2+4=6, 
        #  |   /^\  |
        #  | 1 |2|  |
        #  | 3 |4|  |
        #  |   \-/  |

        # the projection in the yz plane is 3+4=7
        #  | 1   2  |
        #  | ______ |
        #  | |3  4| |
        #  | ------ |

        # xy plane
        xy=0
        for i in grid:
            for j in grid:
                if grid[i][j]!=0:
                    xy+=1
                else:
                    pass
        
        # xz plane
        xz=0
        for row in grid:
            xz+=row[len(grid[0])-1] # the last element of the row
        
        # yz plane
        yz=sum(grid[len(grid)-1]) # last row
        return xy+xz+yz
sol=Solution()
print(sol.projectionArea([[1,0],[0,2]]))
# [[1,2],[3,4]]
# [[1,0],[0,2]]

