class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        l=[0]*(n+1)
        l[-1],l[-2]=0,cost[-1]
        for i in range(n-2,-1,-1):
            l[i]=cost[i]+min(l[i+1],l[i+2])
        return min(l[0],l[1])