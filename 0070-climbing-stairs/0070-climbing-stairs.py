class Solution:
    def __init__(self):
        self.d={}
    def climbStairs(self, n: int) -> int:
        if n in self.d:
            return self.d[n]
        if n==0:
            return 1
        if n<0:
            return 0
        self.d[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return self.d[n]