import sys
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        r1,r2,ans=sum(grid[0]),0,sys.maxsize
        for i in range(n):
            # print(i,r2,r1,ans)
            r1-=grid[0][i]
            ans=min(ans,max(r1,r2))
            r2+=grid[1][i]
        return ans