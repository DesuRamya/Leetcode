class Solution:
    def rob(self, nums: List[int]) -> int:
        r,nr,tr=0,0,0
        for i in range(len(nums)):
            tr=max(r,nr)
            r=nr+nums[i]
            nr=tr
        return max(r,nr)