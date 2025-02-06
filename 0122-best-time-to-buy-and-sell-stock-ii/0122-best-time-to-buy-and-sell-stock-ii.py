class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m,d=0,0
        n=len(prices)
        for i in range(1,n):
            d=max(0,prices[i]-prices[i-1])
            m+=d
        return m