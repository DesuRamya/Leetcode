class Solution:
    def minPartitions(self, n: str) -> int:
        l=list(set(n))
        return int(max(l))