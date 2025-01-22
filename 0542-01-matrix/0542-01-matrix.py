class Solution:
    def updateMatrix(self, isWater: List[List[int]]) -> List[List[int]]:
        m,n=len(isWater),len(isWater[0])
        op=[[-1 for _ in range(n)] for _ in range(m)]
        qu=deque()
        dx,dy=[0,0,1,-1],[1,-1,0,0]
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==0:
                    op[i][j]=0
                    qu.append([i,j])
        h=1
        while qu:
            size=len(qu)
            for _ in range(size):
                cur=qu.popleft()
                for d in range(4):
                    nx,ny=cur[0]+dx[d],cur[1]+dy[d]
                    if 0<=nx<m and 0<=ny<n and op[nx][ny]==-1:
                        qu.append([nx,ny])
                        op[nx][ny]=h
            h+=1
        return op