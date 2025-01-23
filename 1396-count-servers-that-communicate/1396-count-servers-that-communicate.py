class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        rc,cc=[0]*m,[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    rc[i]+=1
                    cc[j]+=1
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (rc[i]>=2 or cc[j]>=2):
                    ans+=1
        return ans