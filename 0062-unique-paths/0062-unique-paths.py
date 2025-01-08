class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def countPaths(i,j,m,n,dp):
            if i==(m-1) and j==(n-1):
                return 1
            if i>=m or j>=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            else:
                dp[i][j]=countPaths(i+1,j,m,n,dp)+countPaths(i,j+1,m,n,dp)
                return dp[i][j]
        dp=[[-1 for i in range(n)]for j in range(m)]
        num = countPaths(0, 0, m, n, dp)
        if m == 1 and n == 1:
            return num
        return dp[0][0]