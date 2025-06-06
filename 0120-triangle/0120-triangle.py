class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            for j in range(len(triangle[i])):
                dp[j]=(min(dp[j],dp[j+1])+triangle[i][j])
        # print(dp) 
        return dp[0]    