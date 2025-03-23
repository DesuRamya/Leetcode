class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n=len(rowSum)
        m=len(colSum)
        curRowSum=[0]*n
        curColSum=[0]*m
        op=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                op[i][j]=min(rowSum[i]-curRowSum[i],colSum[j]-curColSum[j])
                curRowSum[i]+=op[i][j]
                curColSum[j]+=op[i][j]
        return op