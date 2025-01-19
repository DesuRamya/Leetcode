import heapq
class Solution(object):
    def trapRainWater(self, grid):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        hp=[]
        visited=[[False]*n for i in range(m)]
        if not grid or not grid[0]:
            return 0
        for i in range(m):
            for j in [0,n-1]:
                heapq.heappush(hp,(grid[i][j],i,j))
                visited[i][j]=True
        for j in range(n):
            for i in [0,m-1]:
                if not visited[i][j]:
                    heapq.heappush(hp,(grid[i][j],i,j))
                    visited[i][j]=True
        op=0
        while hp:
            cost,x,y=heapq.heappop(hp)
            for a,b in dir:
                na,nb=x+a,y+b
                if 0<=na<m and 0<=nb<n and not visited[na][nb]:
                    op+=max(0,cost-grid[na][nb])
                    heapq.heappush(hp,(max(cost,grid[na][nb]),na,nb))
                    visited[na][nb]=True
        return op