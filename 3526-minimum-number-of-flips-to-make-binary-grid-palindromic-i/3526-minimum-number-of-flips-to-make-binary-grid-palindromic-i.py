class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        r,c=0,0
        for i in range(m):
            for j in range(n//2):
                if grid[i][j]!=grid[i][n-j-1]:
                    r+=1
        for i in range(n):
            for j in range(m//2):
                if grid[j][i]!=grid[m-j-1][i]:
                    c+=1
        return min(r,c)