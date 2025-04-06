class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n=len(questions)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            p=questions[i][0]
            power=questions[i][1]
            next_q=i+power+1
            take=p+(dp[next_q] if next_q<n else 0)
            skip=dp[i+1]
            dp[i]=max(take,skip)
        return dp[0]