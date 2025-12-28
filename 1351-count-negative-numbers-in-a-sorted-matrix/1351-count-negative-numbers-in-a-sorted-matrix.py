class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        i,j = 0,n-1
        c = 0
        while i<m and j>=0:
            if grid[i][j]<0:
                c+=m-i
                j-=1
            else:
                i+=1
        return c