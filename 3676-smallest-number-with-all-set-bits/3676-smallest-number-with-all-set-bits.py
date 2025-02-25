class Solution:
    def smallestNumber(self, n: int) -> int:
        n=bin(n)[2:]
        l=len(n)
        return int("1"*l,2)