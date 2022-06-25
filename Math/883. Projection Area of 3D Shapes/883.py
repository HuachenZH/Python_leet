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
        # max of each row !

        # the projection in the yz plane is 3+4=7
        #  | 1   2  |
        #  | ______ |
        #  | |3  4| |
        #  | ------ |
        # max of each column!

        # xy plane
        xy=0
        for i in grid: # i is list
            for j in i: # j is int
                if j!=0:
                    xy+=1
                else:
                    pass
        
        # xz plane. max of each row
        xz=0
        for i in grid: # i is list. i is each row of grid
            xz+=max(i)
        
        # yz plane. max of each column
        yz=0
        for col in range(len(grid)):
            tmp=[]
            for rowList in grid:
                tmp.append(rowList[col])
            yz+=max(tmp)
            print(tmp)
        print(yz)
        return xy+xz+yz
sol=Solution()
print(sol.projectionArea([[1,0],[0,2]]))
# [[1,2],[3,4]]
# [[1,0],[0,2]]
# [[1,1,1],[1,0,1],[1,1,1]]

