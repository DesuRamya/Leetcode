class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        hp=[(0,0,0)]
        visited=[[False]*n for i in range(m)]
        while hp:
            cost,x,y=heappop(hp)
            if visited[x][y]:
                continue
            visited[x][y]=True
            if (x,y)==(m-1,n-1):
                return cost
            for i,(a,b) in enumerate(dir):
                na,nb=x+a,y+b
                if 0<=na<m and 0<=nb<n:
                    nc=cost+(1 if i+1!=grid[x][y] else 0)
                    heappush(hp,(nc,na,nb)) 