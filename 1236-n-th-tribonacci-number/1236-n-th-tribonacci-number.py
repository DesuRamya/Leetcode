class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        dp=[-1]*(n+1)
        return self.fun(n,dp)
    def fun(self,n,dp):
        dp[0],dp[1],dp[2]=0,1,1
        if dp[n]!=-1:
            return dp[n]
        dp[n] = self.fun(n-1,dp)+self.fun(n-2,dp)+self.fun(n-3,dp)
        return dp[n]