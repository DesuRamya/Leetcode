class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        l=sorted(nums)
        le=len(l)
        median = l[le//2]
        c=0
        for i in l:
            c+=(abs(median-i))
        return c 