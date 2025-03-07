class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        l=[amount+1 for i in range(amount+1)]
        l[0]=0
        for i in range(1,amount+1):
            for j in coins:
                if j<=i:
                    l[i]=min(l[i],l[i-j]+1)
        return l[amount] if l[amount]!=amount+1 else -1