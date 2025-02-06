class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m,d=0,0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                m+=prices[i]-prices[i-1]
        return m