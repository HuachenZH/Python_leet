import numpy as np
class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        # create a m*n zero matrix
        mat=np.zeros((m,n))
        for i in indices: # i will be [0,1], then [1,1]
            # increment the row
            mat[i[0]]=mat[i[0]]+np.ones((1,n))
            # increment the column
            # py is not like matlab, i cant add two columns directly
            tmp=mat.transpose()
            tmp[i[1]]=tmp[i[1]]+np.ones((1,m))[0]
            mat=tmp.transpose() # all this shit... just to avoid using for
        print(mat)
        # count how many odd numbers. I havent found an approach without for
        res=0
        for row in mat:
            for element in row:
                if element%2==1:
                    res+=1
        return res
sol=Solution()
print(sol.oddCells(2,3,[[0,1],[1,1]]))

# according to the runtime and memory use, this is not a very good approach...
