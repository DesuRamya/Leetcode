class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m,n=len(mat),len(mat[0])
        rc=[0]*m
        cc=[0]*n
        d={}
        for i in range(m):
            for j in range(n):
                d[mat[i][j]]=[i,j]
        print(rc,cc,d)
        for i in range(len(arr)):
            a,b=d[arr[i]]
            rc[a]+=1
            cc[b]+=1
            if rc[a]==n or cc[b]==m:
                return i
        return 0
